import pyhtml

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
            padding-bottom: 1px;
        }
        header h1 {
            color: black;
            display: flex;
            align-items: center;
            font-size: 2rem;
        }
        header h1 img {
            height: 40px;
            margin-right: 10px;
            vertical-align: middle;
        }
        nav a {
            margin-left: 30px;
            text-decoration: none;
            color: black;
            font-weight: bold;
            font-size: 1.2rem;
        }
        .content-container {
            margin-left: 80px;
            margin-right: 80px;
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
        .table-container {
            max-height: 300px;
            overflow-y: auto;
            margin-top: 10px;
            background-color: #fff;
            border: 1px solid #ccc;
            max-width: 600px;
            font-size: 13px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }
        th, td {
            padding: 6px 10px;
            border: 1px solid #bbb;
            text-align: left;
        }
        th {
            background-color: #f5f5f5;
            position: sticky;
            top: 0;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
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

        .form-and-side {
            display: flex;
            gap: 40px;
            align-items: flex-start;
        }
        form {
            flex: 1;
        }
        #side-table {
            flex: 1;
        }
        .section {
            margin-top: 30px;
        }
        .section h2 {
            color: #222;
            border-bottom: 0px solid #ccc;
            padding-bottom: 5px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 15px;
            table-layout: auto;
        }
        th, td {
            border: 1px solid #999;
            padding: 8px;
            text-align: left;
            white-space: nowrap; /* Prevent wrapping to keep columns wide */
        }
        .table-container {
            width: 100%;
            overflow-x: auto; /* Make horizontally scrollable */
        }
        .table-container table {
            min-width: 700px; /* Force table wider than container to enable scrolling */
        }
        .natural-language-box {
            flex: 2;
            max-width: 100%;
        }
        .data-snapshot-box {
            flex: 1;
        }
        .box {
            background-color: #fff;
            padding: 20px;
            border: 1px solid #bbb;
            border-radius: 5px;
            margin-top: 30px;
        }
        .flex-row {
            display: flex;
            gap: 20px;
            max-width: 1200px;
        }
    </style>
</head>
<body>
    <header>
        <h1>
            <img src="https://logodix.com/logo/1158014.png" alt="AUSTRALIAN WEATHER Logistics" style="width: 100px; height: auto;">
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
        <div class="content-container">
        <div class="section">
            <h2>Explore Climate Data by Weather Station</h2>

            <div class="form-and-side">
                <form id="climateForm" onsubmit="return fetchClimateData();">
                    <label for="state">State:</label>
                    <select id="state" name="state">
                        <option value="Select">Select</option>
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
                    <br><br>

                    <label for="latStart">Start Latitude:</label>
                    <input type="number" id="latStart" name="latStart" step="0.0001">
                    <br><br>

                    <label for="latEnd">End Latitude:</label>
                    <input type="number" id="latEnd" name="latEnd" step="0.0001">
                    <br><br>

                    <label for="metric">Climate Metric:</label>
                    <select id="metric" name="metric">
                        <option value="Select">Select</option>
                        <option value="MaxTemp">Max Temperature</option>
                        <option value="MinTemp">Min Temperature</option>
                        <option value="Precipitation">Precipitation</option>
                        <option value="Evaporation">Evaporation</option>
                    </select><br><br>

                    <button type="submit">Search 🔍</button>
                </form>

                <div id="side-table"></div>
            </div>

            <div id="results" style="margin-top: 30px;"></div>

            <div class="flex-row">
                <div class="box natural-language-box">
                    <h2>Natural Language Description of Data Attributes</h2>
                    <div class="table-container">
                        <table>
                            <thead><tr><th>Field</th><th>Description</th></tr></thead>
                            <tbody>"""

    # SQL query to fetch field names and descriptions
    sql_query = "SELECT field_name, description FROM natural_language;"
    results = pyhtml.get_results_from_query("database/climate.db", sql_query)

    for row in results:
        field, description = row
        page_html += f"<tr><td>{field}</td><td>{description}</td></tr>\n"

    page_html += """
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="box data-snapshot-box">
                    <h2>Data Snapshot</h2>
                    <ul>
                        <li>Climate data spans from January 1st, 1970 to December 31st, 2020 — covering 50 years of Australian weather observations.</li>
                        <li>The coldest recorded temperature in the dataset is −23.0°C, observed at Charlotte Pass in New South Wales during July 1994.</li>
                        <li>The highest recorded daily rainfall occurred at Bellenden Ker Top Station in Queensland, where 960 mm of rain fell within a single day in January 1979.</li>
                        <li>New South Wales has the largest number of weather stations in the dataset, with over 70 active stations, making it the most densely monitored region.</li>
                        <li>The station with the most complete data coverage over the 50-year period is Melbourne Regional Office, offering continuous daily records for temperature, rainfall, and humidity.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        function fetchClimateData() {
            const state = document.getElementById("state").value;
            const latStart = document.getElementById("latStart").value;
            const latEnd = document.getElementById("latEnd").value;
            const metric = document.getElementById("metric").value;

            fetch(`/api/climate-data?state=${state}&latStart=${latStart}&latEnd=${latEnd}&metric=${metric}`)
                .then(res => res.json())
                .then(data => {
                    renderTables(data);
                });

            return false;
        }

        function renderTables(data) {
            const table1Rows = data.table1.map(row => `
                <tr>
                    <td>${row.siteName}</td>
                    <td>${row.region}</td>
                    <td>${row.latitude}</td>
                </tr>`).join("");

            const table2Rows = data.table2.map(row => `
                <tr>
                    <td>${row.region}</td>
                    <td>${row.numStations}</td>
                    <td>${row.avgMetric.toFixed(2)}</td>
                </tr>`).join("");

            document.getElementById("side-table").innerHTML = `
                <h3>Table 1: Weather Stations in ${data.selectedState}</h3>
                <table>
                    <tr><th>Site Name</th><th>Region</th><th>Latitude</th></tr>
                    ${table1Rows}
                </table>`;

            document.getElementById("results").innerHTML = `
                <h3>Table 2: Summary by Region</h3>
                <table>
                    <tr><th>Region</th><th>Number of Stations</th><th>Avg ${data.metric}</th></tr>
                    ${table2Rows}
                </table>`;
        }
    </script>
</body>
</html>
"""
    return page_html