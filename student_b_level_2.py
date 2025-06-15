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
        .input-group {
            margin: 15px 0;
        }
        label {
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }
        select, input[type="date"], input[type="number"], button {
            padding: 8px;
            width: 250px;
            margin-bottom: 15px;
        }
        button {
            font-weight: bold;
            background-color: #1976d2;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #155fa0;
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
            <label for="climateMetric">Climate Metrics:</label>
            <select id="climateMetric" name="climateMetric">
                <option value="">Select</option>
                <option value="precipitation">Precipitation</option>
                <option value="evaporation">Evaporation</option>
                <option value="temperature">Temperature</option>
                <option value="sunshine">Sunshine</option>
                <option value="cloud">Cloud Cover</option>
            </select>
        </div>

        <div class="section">
            <label for="centerFrom">Center ID Range - From:</label>
            <input type="number" id="centerFrom" name="centerFrom" min="0">

            <label for="centerTo">To:</label>
            <input type="number" id="centerTo" name="centerTo" min="0">
        </div>

        <div class="section">
            <label for="startDate">Start Date:</label>
            <input type="date" id="startDate" name="startDate"><br>

            <label for="endDate">End Date:</label>
            <input type="date" id="endDate" name="endDate">
        </div>

        <div class="section">
            <button onclick="searchData()">🔍 Search</button>
        </div>

        <div class="section container">
            <div class="box">
                <h2>Station Data Table</h2>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Station ID</th>
                                <th>Date</th>
                                <th>Precipitation (mm)</th>
                            </tr>
                        </thead>
                        <tbody id="stationData">
                            <!-- Station data rows will go here -->
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="box">
                <h2>Monthly Summary Table</h2>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Month/Year</th>
                                <th>State</th>
                                <th>Precipitation Total (mm)</th>
                            </tr>
                        </thead>
                        <tbody id="summaryData">
                            <!-- Summary data rows will go here -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script>
        function searchData() {
            alert("Search button clicked. You can link this to dynamic logic.");
        }
    </script>
</body>
</html>
"""
    return page_html
