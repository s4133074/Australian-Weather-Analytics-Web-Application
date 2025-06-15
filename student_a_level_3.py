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
            border-bottom: 0px solid #ccc;
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

    <div class="section">
        <h2>Weather Station Analyser:</h2>
        <form action="/process_query" method="POST">
            <label for="reference_station">Reference Weather Station:</label>
            <select id="reference_station" name="reference_station">
                <option value="Melbourne Airport">Melbourne Airport</option>
                <option value="Ballarat">Ballarat</option>
                <option value="Bendigo">Bendigo</option>
            </select>
            <br>
            <br>
            <label for="climate_metric">Climate Metric:</label>
            <select id="climate_metric" name="climate_metric">
                <option value="avg_temp">Average Temperature</option>
                <option value="rainfall">Rainfall</option>
                <option value="wind_speed">Wind Speed</option>
            </select>
            <br>
            <br>
            <label for="start_period">Start Date (Period 1):</label>
            <input type="date" id="start_period" name="start_period">
            <br>
            <br>
            <label for="end_period">End Date (Period 1):</label>
            <input type="date" id="end_period" name="end_period">
            <br>
            <br>
            <label for="start_period_2">Start Date (Period 2):</label>
            <input type="date" id="start_period_2" name="start_period_2">
            <br>
            <br>
            <label for="end_period_2">End Date (Period 2):</label>
            <input type="date" id="end_period_2" name="end_period_2">
            <br>
            <br>
            <label for="num_results">Number of Similar Stations to Show:</label>
            <input type="number" id="num_results" name="num_results" value="2" min="1" max="10">
            <br>
            <br>
            <button type="submit">Find Similar Stations</button>
        </form>
    </div>
</body>
</html>
"""
    return page_html
