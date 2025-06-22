import sqlite3

def get_results_from_query(db_path, query, params=()):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"Database query error: {e}")
        return []


def get_page_html(form_data):
    print("About to return page 2")

    start_site_id = form_data.get("start_site_id")
    end_site_id = form_data.get("end_site_id")
    start_date = form_data.get("start_date")
    end_date = form_data.get("end_date")
    selected_climate = form_data.get("metric")

    if isinstance(start_site_id, list): start_site_id = start_site_id[0]
    if isinstance(end_site_id, list): end_site_id = end_site_id[0]
    if isinstance(start_date, list): start_date = start_date[0]
    if isinstance(end_date, list): end_date = end_date[0]
    if isinstance(selected_climate, list): selected_climate = selected_climate[0]

    table1_html = ""
    table2_html = ""

    if start_site_id and end_site_id and start_date and end_date and selected_climate:
        try:
            start_site_id = int(start_site_id)
            end_site_id = int(end_site_id)
            start_date = str(start_date)
            end_date = str(end_date)

            allowed_metrics = ["MaxTemp", "MinTemp", "Precipitation", "Evaporation", "Sunshine"]
            if selected_climate not in allowed_metrics:
                raise ValueError("Invalid climate metric selected.")

            query1 = f"""
                SELECT ws.site_id, cm.DMY, cm.{selected_climate}
                FROM weather_station ws
                JOIN recordings cm ON cm.location = ws.site_id
                WHERE ws.site_id BETWEEN ? AND ?
                AND (
                    strftime('%Y-%m-%d',
                        substr(cm.DMY, 7, 4) || '-' ||
                        printf('%02d', CAST(substr(cm.DMY, 4, 2) AS INT)) || '-' ||
                        printf('%02d', CAST(substr(cm.DMY, 1, 2) AS INT))
                    ) BETWEEN ? AND ?
                )
                ORDER BY ws.site_id, cm.DMY;
            """
            params1 = (start_site_id, end_site_id, start_date, end_date)
            results1 = get_results_from_query("database/climate.db", query1, params1)

            if results1:
                table1_html += f"""
                    <h2>Climate Data for Selected Range</h2>
                    <div class="table-container">
                    <table>
                        <tr>
                            <th>Site ID</th>
                            <th>Date</th>
                            <th>{selected_climate}</th>
                        </tr>
                """
                for row in results1:
                    table1_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n"
                table1_html += "</table></div>"
            else:
                table1_html = "<p>No data found for the given filters.</p>"

            month = start_date[5:7]
            year = start_date[0:4]

            query2 = f"""
                SELECT ws.state_id AS State, SUM(cm.Precipitation) AS "Total Precipitation (mm)"
                FROM weather_station ws
                JOIN recordings cm ON cm.location = ws.site_id
                WHERE substr(cm.DMY, 4, 2) = ? AND substr(cm.DMY, 7, 4) = ?
                GROUP BY ws.state_id
                ORDER BY ws.state_id;
            """
            params2 = (month, year)
            results2 = get_results_from_query("database/climate.db", query2, params2)

            if results2:
                table2_html += f"""
                    <h2>State-wise Summary for {month}/{year}</h2>
                    <div class="table-container">
                    <table>
                        <tr>
                            <th>State</th>
                            <th>Total {selected_climate} (mm)</th>
                        </tr>
                """
                for row in results2:
                    table2_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>\n"
                table2_html += "</table></div>"
            else:
                table2_html = "<p>No state-wise data found for the selected month and year.</p>"

        except Exception as e:
            table1_html = f"<p>Error: {e}</p>"

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
            margin-left: 10px;
        text-decoration: none;
        color: #1a1a1a;
        font-weight: 600;
        font-size: 1.0rem;
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
            <img src="https://github.co.jp/assets/images/customer-stories/logo-awl.png" alt="AUSTRALIAN WEATHER Logistics" width="150px">
            AUSTRALIAN WEATHER Logistics
        </h1>
        <nav>
            <a href="/">Home</a>
            <a href="/page2a">Station Data</a>
            <a href="/page3a">Similar Stations</a>
            <a href="/page1b">Mission Page</a>
            <a href="/page2b">Metric Data</a>
            <a href="/page3b">Metric Similarities</a>
        </nav>
    </header>

    <main class="main-content" style="padding: 20px 60px;">
        <h1>Climate Metric Data:</h1>
        (Present infromation about climate changes for specific climate metric measurement across all States)
<div class="container">
        <form method="GET">
            <table>
                <tr><td><label for="start_site_id">Start Station ID:</label></td><td><input type="number" id="start_site_id" name="start_site_id" step="1" required></td></tr>
                <tr><td><label for="end_site_id">End Station ID:</label></td><td><input type="number" id="end_site_id" name="end_site_id" step="1" required></td></tr>
                <tr><td><label for="start_date">Start Date (YYYY-MM-DD):</label></td><td><input type="date" id="start_date" name="start_date" required></td></tr>
                <tr><td><label for="end_date">End Date (YYYY-MM-DD):</label></td><td><input type="date" id="end_date" name="end_date" required></td></tr>
                <tr><td><label for="metric">Climate Metric:</label></td><td><select id="metric" name="metric">
                    <option value="MaxTemp">Max Temperature</option>
                    <option value="MinTemp">Min Temperature</option>
                    <option value="Precipitation">Precipitation</option>
                    <option value="Evaporation">Evaporation</option>
                    <option value="Sunshine">Sunshine</option>
                </select></td></tr>
                <tr><td colspan="2" style="text-align:center;"><button type="submit">Search 🔍</button></td></tr>
            </table>
        </form>

        <div id="results">
            {table1_html}
            <br><br>
            {table2_html}
        </div>
    </main>
</body>
</html>
"""
    return page_html