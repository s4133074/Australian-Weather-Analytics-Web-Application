import sqlite3
from datetime import datetime
import os
import http.server
import urllib.parse
import socketserver

PORT = 8000
DATABASE_FILENAME = 'climate.db'
DATABASE_DIR = 'database'
DB_PATH = os.path.join(DATABASE_DIR, DATABASE_FILENAME)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  
    return conn

def get_page_html(form_data):
    print("About to return page 3")

    results_html = ""

    def _get_single_form_value(data_dict, key, default=''):
        value = data_dict.get(key) 
        if value is None:
            return default
        if isinstance(value, list):
            return value[0] if value else default 
        return value

    submitted_metric = _get_single_form_value(form_data, 'metric', '')
    submitted_ref_station = _get_single_form_value(form_data, 'referenceStation', '')
    submitted_start1 = _get_single_form_value(form_data, 'start1', '')
    submitted_end1 = _get_single_form_value(form_data, 'end1', '')
    submitted_start2 = _get_single_form_value(form_data, 'start2', '')
    submitted_end2 = _get_single_form_value(form_data, 'end2', '')
    submitted_topN = _get_single_form_value(form_data, 'topN', '3') 

    if form_data: 
        metric = submitted_metric
        reference_station = submitted_ref_station
        start1 = submitted_start1
        end1 = submitted_end1
        start2 = submitted_start2
        end2 = submitted_end2
        topN = submitted_topN

        if all([metric, reference_station, start1, end1, start2, end2, topN]):
            try:
                topN = int(topN) 
                conn = get_db_connection()
                cursor = conn.cursor()

                sql_query = f"""
                WITH
                Period1 AS (
                    SELECT Location, AVG(CAST(
                        CASE '{metric}'
                            WHEN 'MaxTemp' THEN MaxTemp
                            WHEN 'MinTemp' THEN MinTemp
                            WHEN 'Precipitation' THEN Precipitation
                            WHEN 'Evaporation' THEN Evaporation
                        END AS REAL)) AS avg_p1
                    FROM recordings
                    WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?
                    GROUP BY Location
                ),
                Period2 AS (
                    SELECT Location, AVG(CAST(
                        CASE '{metric}'
                            WHEN 'MaxTemp' THEN MaxTemp
                            WHEN 'MinTemp' THEN MinTemp
                            WHEN 'Precipitation' THEN Precipitation
                            WHEN 'Evaporation' THEN Evaporation
                        END AS REAL)) AS avg_p2
                    FROM recordings
                    WHERE date(substr(DMY,7,4) || '-' || substr(DMY,4,2) || '-' || substr(DMY,1,2)) BETWEEN ? AND ?
                    GROUP BY Location
                ),
                Changes AS (
                    SELECT p1.Location, p1.avg_p1, p2.avg_p2,
                           CASE WHEN p1.avg_p1 = 0 THEN NULL
                                ELSE ((p2.avg_p2 - p1.avg_p1) / p1.avg_p1) * 100
                           END AS pct_change
                    FROM Period1 p1
                    JOIN Period2 p2 ON p1.Location = p2.Location
                ),
                RefChange AS (
                    SELECT pct_change AS ref_pct_change
                    FROM Changes
                    WHERE Location = ?
                )
                SELECT ws.site_id AS station_id, ws.name AS station_name,
                       c.avg_p1, c.avg_p2, c.pct_change,
                       ABS(c.pct_change - rc.ref_pct_change) AS similarity_diff
                FROM Changes c
                JOIN RefChange rc ON 1=1
                JOIN weather_station ws ON ws.site_id = c.Location
                WHERE c.Location != ?
                ORDER BY similarity_diff ASC
                LIMIT ?;
                """
                cursor.execute(sql_query, (start1, end1, start2, end2, reference_station, reference_station, topN))
                data = cursor.fetchall()

                ref_station_name_query = "SELECT name FROM weather_station WHERE site_id = ?"
                cursor.execute(ref_station_name_query, (reference_station,))
                ref_station_data = cursor.fetchone()
                reference_station_display_name = ref_station_data['name'] if ref_station_data else reference_station

                conn.close()

                if data:
                    table_rows = []
                    for row in data:
                        station_id = row['station_id']
                        station_name = row['station_name']
                        avg_p1_formatted = f"{row['avg_p1']:.2f}" if row['avg_p1'] is not None else 'N/A'
                        avg_p2_formatted = f"{row['avg_p2']:.2f}" if row['avg_p2'] is not None else 'N/A'
                        pct_change_formatted = f"{row['pct_change']:.2f}%" if row['pct_change'] is not None else 'N/A'
                        similarity_diff_formatted = f"{row['similarity_diff']:.2f}" if row['similarity_diff'] is not None else 'N/A'
                        table_rows.append(f"""
                            <tr>
                                <td>{station_name} ({station_id})</td>
                                <td>{avg_p1_formatted}</td>
                                <td>{avg_p2_formatted}</td>
                                <td>{pct_change_formatted}</td>
                                <td>{similarity_diff_formatted}</td>
                            </tr>
                        """)
                    results_html = f"""
                        <h2>Top {topN} Most Similar Stations to {reference_station_display_name}</h2>
                        <div class="table-container">
                        <table>
                            <tr>
                                <th>Station</th>
                                <th>Avg ({start1}–{end1})</th>
                                <th>Avg ({start2}–{end2})</th>
                                <th>% Change</th>
                                <th>Similarity to Ref (%)</th>
                            </tr>
                            {''.join(table_rows)}
                        </table>
                        </div>
                    """
                else:
                    results_html = "<p>No similar stations found for the given criteria or reference station.</p>"

            except Exception as e:
                results_html = f"<p style='color: red;'>An error occurred while fetching data: {e}</p>"
                print(f"Error processing form data: {e}")
        else:
            results_html = "<p style='color: orange;'>Please fill in all the form fields to get results.</p>"
    else:
        results_html = "<p> </p>"

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Database Web-App Demo</title>
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
<h1> Weather Station Analyser:</h1>
(To Identify weather station locations with similar change in metric percentages)
<div class="container">
    <form id="similarStationsForm" method="get" action="/page3a">
        <label for="metric">Climate Metric:</label>
        <select id="metric" name="metric" required>
            <option value="MaxTemp" {'selected' if submitted_metric == 'MaxTemp' else ''}>Max Temperature</option>
            <option value="MinTemp" {'selected' if submitted_metric == 'MinTemp' else ''}>Min Temperature</option>
            <option value="Precipitation" {'selected' if submitted_metric == 'Precipitation' else ''}>Precipitation</option>
            <option value="Evaporation" {'selected' if submitted_metric == 'Evaporation' else ''}>Evaporation</option>
        </select>
        <br>
        <br>


        <label for="referenceStation">Reference Station ID:</label>
        <input type="text" id="referenceStation" name="referenceStation" required placeholder="e.g. 76031" value="{submitted_ref_station}">
        
        <br>
        <br>


        <label for="start1">Time Period 1: Start Date</label>
        <input type="date" id="start1" name="start1" required value="{submitted_start1}">


        <label for="end1">Time Period 1: End Date</label>
        <input type="date" id="end1" name="end1" required value="{submitted_end1}">

        <br>
        <br>        

        <label for="start2">Time Period 2: Start Date</label>
        <input type="date" id="start2" name="start2" required value="{submitted_start2}">
      

        <label for="end2">Time Period 2: End Date</label>
        <input type="date" id="end2" name="end2" required value="{submitted_end2}">

        <br>
        <br>        

        <label for="topN">Number of Similar Stations:</label>
        <input type="number" id="topN" name="topN" min="1" max="20" value="{submitted_topN}" required>

        <br>
        <br>        

        <button type="submit">Search 🔍</button>
    </form>

    <div id="results">
        {results_html}
    </div>
</div>

</body>
</html>"""
    return page_html


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_string = parsed_path.query

        if path == '/page3a':
            raw_form_data = urllib.parse.parse_qs(query_string)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(get_page_html(raw_form_data).encode('utf-8'))
            print(f"Served page3a (GET) with form data: {raw_form_data}")
        elif path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Welcome!</h1><p>Navigate to <a href=\"/page3a\">Fishermen Page</a>.</p>")
        else:
            super().do_GET()

if __name__ == '__main__':
    if not os.path.exists(DATABASE_DIR):
        os.makedirs(DATABASE_DIR)
    if not os.path.exists(DB_PATH):
        print(f"WARNING: Database '{DB_PATH}' not found. Creating table schema.")
        print("You will need to manually populate your database with data.")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_data (
                Location TEXT,
                DMY TEXT,
                MaxTemp REAL,
                MinTemp REAL,
                Precipitation REAL,
                Evaporation REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_station (
                site_id TEXT PRIMARY KEY,
                name TEXT
            )
        ''')
        conn.commit()
        conn.close()