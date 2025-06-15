import sqlite3

# Helper function to run a query
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

# Main page HTML generator
def get_page_html(form_data):
    print("About to return page 2")

    selected_state = form_data.get("state")
    lat_start = form_data.get("latStart")
    lat_end = form_data.get("latEnd")
    selected_climate = form_data.get("metric")

    if isinstance(selected_state, list): selected_state = selected_state[0]
    if isinstance(lat_start, list): lat_start = lat_start[0]
    if isinstance(lat_end, list): lat_end = lat_end[0]
    if isinstance(selected_climate, list): selected_climate = selected_climate[0]

    table1_html = ""
    table2_html = ""

    if selected_state and lat_start and lat_end and selected_climate:
        try:
            lat_start = float(lat_start)
            lat_end = float(lat_end)
            lat_min, lat_max = sorted([lat_start, lat_end])

            query1 = """
                SELECT 
                    ws.site_id,
                    ws.name AS station_name,
                    r.name AS region,
                    ws.latitude
                FROM 
                    weather_station ws
                JOIN 
                    state s ON ws.state_id = s.id
                JOIN 
                    region r ON ws.region_id = r.id
                WHERE 
                    s.name = ? AND ws.latitude BETWEEN ? AND ?
                ORDER BY 
                    ws.site_id;
            """
            params1 = (selected_state, lat_min, lat_max)
            results1 = get_results_from_query("database/climate.db", query1, params1)

            if results1:
                table1_html += f"""
                    <h2>Weather Stations in {selected_state} between {lat_start} and {lat_end}</h2>
                    <div class="table-container">
                    <table>
                        <tr>
                            <th>Site ID</th>
                            <th>Station Name</th>
                            <th>Region</th>
                            <th>Latitude</th>
                        </tr>
                """
                for row in results1:
                    table1_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>\n"
                table1_html += "</table></div>"
            else:
                table1_html = "<p>No weather stations found for the given filters.</p>"

            allowed_metrics = ["MaxTemp", "MinTemp", "Precipitation", "Evaporation", "Sunshine"]
            if selected_climate not in allowed_metrics:
                raise ValueError("Invalid climate metric selected.")

            query2 = f"""
                SELECT 
                    r.name AS region, 
                    COUNT(r.name) AS number_ws, 
                    AVG(cm.{selected_climate}) AS avg_metric
                FROM 
                    weather_station ws 
                JOIN 
                    state s ON ws.state_id = s.id 
                JOIN 
                    region r ON ws.region_id = r.id 
                LEFT OUTER JOIN 
                    climate_metric cm ON ws.site_id = cm.location 
                WHERE 
                    s.name = ? AND ws.latitude BETWEEN ? AND ?
                GROUP BY 
                    r.name;
            """
            params2 = (selected_state, lat_min, lat_max)
            results2 = get_results_from_query("database/climate.db", query2, params2)

            if results2:
                table2_html += f"""
                    <h2>Number of weather stations in {selected_state} - Average({selected_climate})</h2>
                    <div class="table-container">
                    <table>
                        <tr>
                            <th>Region</th>
                            <th>Number of Weather Stations</th>
                            <th>Average {selected_climate}</th>
                        </tr>
                """
                for row in results2:
                    region, num_ws, avg_value = row
                    avg_str = f"{avg_value:.2f}" if avg_value is not None else "N/A"
                    table2_html += f"<tr><td>{region}</td><td>{num_ws}</td><td>{avg_str}</td></tr>\n"
                table2_html += "</table></div>"
            else:
                table2_html = "<p>No regional summary data found for the given filters.</p>"

        except Exception as e:
            table1_html = f"<p style='color:red;'>Error retrieving data: {e}</p>"

    # ✅ f-string fix applied here:
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
        .table-container {{
            max-height: 400px;
            overflow-y: auto;
            margin-top: 10px;
            background-color: #fff;
            border: 1px solid #ccc;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
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
    </style>
</head>
<body>
    <header>
        <h1>
            <img src="https://github.co.jp/assets/images/customer-stories/logo-awl.png" alt="AUSTRALIAN WEATHER Logistics" width="150px">
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

    <main class="main-content">
        <h1>Focused view of climate change by Weather Station:</h1>

        <form method="GET">
            <table>
                <tr>
                    <td><label for="state">Select State:</label></td>
                    <td>
                        <select id="state" name="state" required>
                            <option value="">--Select--</option>
                            <option value="A.A.T.">A.A.T</option>
                            <option value="A.E.T.">A.E.T.</option>
                            <option value="N.S.W.">N.S.W.</option>
                            <option value="N.T.">N.T.</option>
                            <option value="QLD">QLD</option>
                            <option value="S.A.">S.A.</option>
                            <option value="TAS">TAS</option>
                            <option value="VIC">VIC</option>
                            <option value="W.A.">W.A.</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td><label for="latStart">Start Latitude:</label></td>
                    <td><input type="number" id="latStart" name="latStart" step="0.01" required></td>
                </tr>
                <tr>
                    <td><label for="latEnd">End Latitude:</label></td>
                    <td><input type="number" id="latEnd" name="latEnd" step="0.01" required></td>
                </tr>
                <tr>
                    <td><label for="metric">Climate Metric:</label></td>
                    <td>
                        <select id="metric" name="metric">
                            <option value="">--Select--</option>
                            <option value="MaxTemp">Max Temperature</option>
                            <option value="MinTemp">Min Temperature</option>
                            <option value="Precipitation">Precipitation</option>
                            <option value="Evaporation">Evaporation</option>
                            <option value="Sunshine">Sunshine</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td colspan="2" style="text-align:center;">
                        <button type="submit">Search 🔍</button>
                    </td>
                </tr>
            </table>
        </form>

        <div id="results">
            {table1_html}
            <br>
            {table2_html}
        </div>
    </main>
</body>
</html>
"""
    return page_html


