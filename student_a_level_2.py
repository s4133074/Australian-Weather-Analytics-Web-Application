def get_page_html(form_data):
    print("About to return home page...")
    page_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather Insights Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 10px;
            background-color: #f9f9f9;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #ddd;
            padding-bottom: 10px;
        }
        header h1 {
            color: black;
        }
        nav a {
            margin-left: 30px;
            text-decoration: none;
            color: black;
            font-weight: bold;
        }
        .content-container {
            margin-left: 80px;
            margin-right: 80px;
            /* optional: margin-top: 20px; if you want space below header */
        }
        .section {
            margin-top: 30px;
        }
        .section h2 {
            color: #222;
            border-bottom: 2px solid #ccc;
            padding-bottom: 5px;
        }
        .container {
            display: flex;
            justify-content: space-between;
            gap: 30px;
            flex-wrap: wrap;
        }
        .box {
            flex: 1;
            background-color: #fff;
            padding: 20px;
            border: 1px solid #bbb;
            border-radius: 5px;
            min-width: 300px;
        }
        .image-box {
            flex: 1;
            text-align: center;
            min-width: 300px;
        }
        .image-box img {
            max-width: 100%;
            height: auto;
            object-fit: contain;
        }
    </style>
</head>
<body>
    <header>
        <h1>🌤️    AUSTRALIAN WEATHER Insight</h1>
        <nav class="nav-bar">
            <a href="/">Home</a>
            <a href="/page2a">Page 1B</a>
            <a href="/page3a">Page 1C</a>
            <a href="/page1b">Page 2A</a>
            <a href="/page2b">Page 2B</a>
            <a href="/page3b">Page 2C</a>
        </nav>
    </header>
    </body>

        <div class="content">
            <div style="width: 150%;">
                <h2>Explore Climate Data by Weather Station</h2>

                <form id="climateForm" onsubmit="return fetchClimateData();">
                    <label for="state">Select State:</label>
                    <select id="state" name="state">
                        <option value="AAT">AAT</option>
                        <option value="AET">AET</option>
                        <option value="NSW">NSW</option>
                        <option value="NT">NT</option>
                        <option value="QLD">QLD</option>
                        <option value="SA">SA</option>
                        <option value="TSA">TSA</option>
                        <option value="VIC">VIC</option>
                        <option value="WA">WA</option>
                    </select>
                    <br>
                    <br>

                    <label for="latStart">Start Latitude:</label>
                    <input type="number" id="latStart" name="latStart" step="0.0001">
                    <br>
                    <br>

                    <label for="latEnd">End Latitude:</label>
                    <input type="number" id="latEnd" name="latEnd" step="0.0001">
                    <br>
                    <br>

                    <label for="metric">Climate Metric:</label>
                    <select id="metric" name="metric">
                        <option value="MaxTemp">Max Temperature</option>
                        <option value="MinTemp">Min Temperature</option>
                        <option value="Precipitation">Precipitation</option>
                        <option value="Evaporation">Evaporation</option>
                    </select><br>
                    <br>

                    <button type="submit">Submit</button>
                </form>

                <div id="results"></div>
            </div>
        </div>
    </div>

    <script>
        function fetchClimateData() {{
            const state = document.getElementById("state").value;
            const latStart = document.getElementById("latStart").value;
            const latEnd = document.getElementById("latEnd").value;
            const metric = document.getElementById("metric").value;

            fetch(`/api/climate-data?state=${{state}}&latStart=${{latStart}}&latEnd=${{latEnd}}&metric=${{metric}}`)
                .then(res => res.json())
                .then(data => {{
                    document.getElementById("results").innerHTML = renderTables(data);
                }});

            return false; // prevent page reload
        }}

        function renderTables(data) {{
            const table1Rows = data.table1.map(row => `
                <tr>
                    <td>${{row.siteName}}</td>
                    <td>${{row.region}}</td>
                    <td>${{row.latitude}}</td>
                </tr>`).join("");

            const table2Rows = data.table2.map(row => `
                <tr>
                    <td>${{row.region}}</td>
                    <td>${{row.numStations}}</td>
                    <td>${{row.avgMetric.toFixed(2)}}</td>
                </tr>`).join("");

            return `
                <h3>Table 1: Weather Stations in ${{data.selectedState}}</h3>
                <table>
                    <tr><th>Site Name</th><th>Region</th><th>Latitude</th></tr>
                    ${{table1Rows}}
                </table>

                <h3>Table 2: Summary by Region</h3>
                <table>
                    <tr><th>Region</th><th>Number of Stations</th><th>Avg ${{data.metric}}</th></tr>
                    ${{table2Rows}}
                </table>`;
        }}
    </script>

</body>
</html>
"""
    return page_html