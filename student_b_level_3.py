import sqlite3
from datetime import datetime
import os
import http.server
import urllib.parse
import socketserver

PORT = 8001
DATABASE_FILENAME = 'climate.db'
DATABASE_DIR = 'database'
DB_PATH = os.path.join(DATABASE_DIR, DATABASE_FILENAME)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_page_html(form_data):
    print("About to return page 3B")

    results_html = ""

    def _get_single_form_value(data_dict, key, default=''):
        value = data_dict.get(key)
        if value is None:
            return default
        if isinstance(value, list):
            return value[0] if value else default
        return value

    metric = _get_single_form_value(form_data, 'referenceMetric')
    start1 = _get_single_form_value(form_data, 'start1')
    end1 = _get_single_form_value(form_data, 'end1')
    start2 = _get_single_form_value(form_data, 'start2')
    end2 = _get_single_form_value(form_data, 'end2')
    topN = int(_get_single_form_value(form_data, 'topN', '3'))

    if all([metric, start1, end1, start2, end2]):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = f"""
            WITH totals AS (
                SELECT
                    'Precipitation' AS metric,
                    (SELECT SUM(CAST(Precipitation AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?) AS total1,
                    (SELECT SUM(CAST(Precipitation AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?) AS total2
                UNION ALL
                SELECT 'Evaporation',
                    (SELECT SUM(CAST(Evaporation AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?),
                    (SELECT SUM(CAST(Evaporation AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?)
                UNION ALL
                SELECT 'MaxTemp',
                    (SELECT AVG(CAST(MaxTemp AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?),
                    (SELECT AVG(CAST(MaxTemp AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?)
                UNION ALL
                SELECT 'Sunshine',
                    (SELECT SUM(CAST(Sunshine AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?),
                    (SELECT SUM(CAST(Sunshine AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?)
                UNION ALL
                SELECT 'Okta12',
                    (SELECT SUM(CAST(Okta12 AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?),
                    (SELECT SUM(CAST(Okta12 AS REAL)) FROM recordings
                     WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?)
            ),
            changes AS (
                SELECT metric, total1, total2,
                    CASE WHEN total1 = 0 THEN NULL ELSE ((total2 - total1) / total1) * 100 END AS pct_change
                FROM totals
            ),
            ref AS (
                SELECT pct_change AS ref_change FROM changes WHERE metric = ?
            )
            SELECT c.metric, c.total1, c.total2, c.pct_change,
                   ABS(c.pct_change - r.ref_change) AS similarity_diff
            FROM changes c, ref r
            WHERE c.metric != ?
            ORDER BY similarity_diff ASC
            LIMIT ?;
            """

            params = (
                start1, end1, start2, end2,  # Precip
                start1, end1, start2, end2,  # Evap
                start1, end1, start2, end2,  # MaxTemp
                start1, end1, start2, end2,  # Sunshine
                start1, end1, start2, end2,  # Okta12
                metric, metric, topN
            )

            cursor.execute(sql, params)
            rows = cursor.fetchall()
            conn.close()

            if rows:
                table = "".join(f"""
                    <tr>
                        <td>{row['metric']}</td>
                        <td>{row['total1']:.2f}</td>
                        <td>{row['total2']:.2f}</td>
                        <td>{row['pct_change']:.2f}%</td>
                        <td>{row['similarity_diff']:.2f}</td>
                    </tr>
                """ for row in rows)

                results_html = f"""
                    <h2>Metrics Most Similar to {metric}</h2>
                    <div class="table-container">
                    <table>
                        <tr>
                            <th>Metric</th>
                            <th>Total/Avg Period 1</th>
                            <th>Total/Avg Period 2</th>
                            <th>% Change</th>
                            <th>Difference from {metric} (%)</th>
                        </tr>
                        {table}
                    </table>
                    </div>
                """
            else:
                results_html = "<p>No matching data found.</p>"

        except Exception as e:
            results_html = f"<p style='color:red;'>Error occurred: {e}</p>"
            print(e)

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Compare Metric Similarities</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            background-color: #f4f7fb;
            color: #333;
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(to right, #c6e2ff, #f0f8ff);
            padding: 20px 40px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        header h1 {{
            display: flex;
            align-items: center;
            font-size: 1.8rem;
        }}
        header h1 img {{
            height: 50px;
            margin-right: 15px;
        }}
        nav a {{
            margin-left: 25px;
            text-decoration: none;
            color: #1a1a1a;
            font-weight: 600;
            font-size: 1.1rem;
            transition: color 0.2s;
        }}
        nav a:hover {{
            color: #0077cc;
        }}
        .container {{
            display: flex;
            justify-content: space-between;
            gap: 30px;
            padding: 40px 60px;
            flex-wrap: wrap;
        }}
        .top-box {{
            margin: 30px 60px 10px 60px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        }}
        .top-box h2 {{
            margin-top: 0;
            color: #2c3e50;
            border-bottom: 2px solid #ccc;
            padding-bottom: 5px;
        }}
        .box {{
            flex: 1;
            background-color: #ffffff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            min-width: 300px;
            transition: transform 0.2s ease-in-out;
        }}
        .box:hover {{
            transform: translateY(-5px);
        }}
        .table-container {{
            max-height: 300px;
            overflow-y: auto;
            margin-top: 15px;
            border: 1px solid #e0e0e0;
            font-size: 13px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 8px 12px;
            border-bottom: 1px solid #eee;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            position: sticky;
            top: 0;
        }}
        tr:nth-child(even) {{
            background-color: #fafafa;
        }}
        ul {{
            padding-left: 18px;
        }}
        li {{
            margin-bottom: 8px;
        }}
        .image-box img {{
            width: 100%;
            border-radius: 8px;
            margin-bottom: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
</style>
</head>
<body>

</head>
<body>
    <header>
        <h1>
            <img src="https://github.co.jp/assets/images/customer-stories/logo-awl.png" alt="AUSTRALIAN WEATHER Logistics" width = 150px>
            AUSTRALIAN WEATHER Logistics
        </h1>
        <nav class="nav-bar">
            <a href="/">Home</a>
            <a href="/page2a">Page 1B</a>
            <a href="/page3a">Page 1C</a>
            <a href="/page1b">Page 2A</a>
            <a href="/page2b">Page 2B</a>
            <a href="/page3b">Page 2C</a>
        </nav>
    </header>
<h1>Explore Climate Metrics Similarities:</h1>
<div class="container">
    <form method="get" action="/page3b">
        <label>Reference Metric:</label>
        <select name="referenceMetric" required>

        <br>
        <br>        
            <option value="Precipitation" {'selected' if metric == 'Precipitation' else ''}>Precipitation</option>
            <option value="Evaporation" {'selected' if metric == 'Evaporation' else ''}>Evaporation</option>
            <option value="MaxTemp" {'selected' if metric == 'MaxTemp' else ''}>Max Temperature</option>
            <option value="Sunshine" {'selected' if metric == 'Sunshine' else ''}>Sunshine</option>
            <option value="Okta12" {'selected' if metric == 'Okta12' else ''}>Cloud Cover (Okta)</option>
        </select>

        <br>
        <br>

        <label>Time Period 1: Start Date</label>
        <input type="date" name="start1" value="{start1}" required>
        <label>End Date</label>
        <input type="date" name="end1" value="{end1}" required>

        <label>   Time Period 2: Start Date</label>
        <input type="date" name="start2" value="{start2}" required>
        <label>End Date </label>
        <input type="date" name="end2" value="{end2}" required>

        <br>
        <br>        

        <label>Number of Metrics to Find:</label>
        <input type="number" name="topN" min="1" max="5" value="{topN}" required>

        <br>
        <br>        

        <button type="submit">Search 🔍</button>
    </form>

    <div id="results">
        {results_html}
    </div>
</div>

</body>
</html>
"""
    return page_html

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        form_data = urllib.parse.parse_qs(parsed.query)

        if path == "/page3b":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(get_page_html(form_data).encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    if not os.path.exists(DATABASE_DIR):
        os.makedirs(DATABASE_DIR)
    if not os.path.exists(DB_PATH):
        print("Creating climate.db and tables (empty)")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS climate_metric (
                DMY TEXT,
                Location TEXT,
                Precipitation REAL,
                Evaporation REAL,
                MaxTemp REAL,
                Sunshine REAL,
                Okta12 REAL
            )
        ''')
        conn.commit()
        conn.close()

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()



