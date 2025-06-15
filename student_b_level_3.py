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
    </header>
        <div class="content-container">
        <h2>COMPARING WEATHER DATA</h2>

        <form action="#" method="get">
            <label for="metric">Reference Climatic Metric:</label>
            <select id="metric" name="metric">
                <option value="">Select</option>
                <option value="sunshine">Sunshine</option>
                <option value="cloud cover">Cloud Cover</option>
                <option value="precipitation">Precipitation</option>
                <option value="temperature">Temperature</option>
                <option value="evaporation">Evaporation</option>
            </select>

            <h3>Time Period 1</h3>
            <div style="display: flex; gap: 20px; align-items: center;">
                <label for="start1">Start Date:</label>
                <input type="date" id="start1" name="start1" placeholder="DD/MM/YYYY">
                <label for="end1">End Date:</label>
                <input type="date" id="end1" name="end1" placeholder="DD/MM/YYYY">
            </div>

            <h3>Time Period 2</h3>
            <div style="display: flex; gap: 20px; align-items: center;">
                <label for="start2">Start Date:</label>
                <input type="date" id="start2" name="start2" placeholder="DD/MM/YYYY">
                <label for="end2">End Date:</label>
                <input type="date" id="end2" name="end2" placeholder="DD/MM/YYYY">
            </div>

            <label for="metrics" style="margin-top: 20px;">Number of Metrics to Compare Metric:</label>
            <select id="metrics" name="metrics">
                <option value="">Select</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
            </select>

            <div style="margin-top: 20px;">
                <button type="submit" style="
                    background-color: #d3d6ce;
                    color: black;
                    font-size: 18px;
                    padding: 10px 25px;
                    border: 1px solid #aaa;
                    border-radius: 5px;
                    cursor: pointer;">
                    <b>Search</b> 🔍
                </button>
            </div>
        </form>

        <div style="margin-top: 40px;">
            <h3>Detailed Data:</h3>
            <div style="border: 2px solid #888; height: 200px; width: 90%; max-width: 700px; background: #fff; margin-top: 10px;">
                <!-- This box simulates a chart or detailed data section -->
                <svg width="100%" height="100%">
                    <line x1="0" y1="0" x2="100%" y2="100%" stroke="#aaa" stroke-width="2"/>
                    <line x1="100%" y1="0" x2="0" y2="100%" stroke="#aaa" stroke-width="2"/>
                </svg>
            </div>
        </div>
    </div>

</html>
"""
    return page_html