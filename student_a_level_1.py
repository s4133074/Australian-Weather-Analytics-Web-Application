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

    <div class="container">
        <div class="main-content">
            <div class="top-box">
                <h2>About:</h2>
                <p>This web application is designed to help users explore and understand the impact of anthropomorphic (human-induced) climate change across Australia from 1970 to 2020. Using official datasets from the Australian Bureau of Meteorology, this platform provides access to temperature, rainfall, and other key climate variables collected from weather stations across the nation, including external and Antarctic territories. The site caters to a wide range of users — from the general public to researchers and policymakers — offering both high-level summaries and detailed data insights. The goal is to support informed, respectful, and unbiased discussions about climate trends, based on transparent evidence and scientific data.</p>
            </div>

            <div style="display: flex; gap: 20px; margin-top: 30px; max-width: 1200px;">
              <div class="box">
                <h2>Natural Language Description of Data Attributes</h2>
                <div class="table-container">
                  <table>
                    <thead><tr><th>Field</th><th>Description</th></tr></thead>
                    <tbody>"""

    # Dynamic table rows from SQL database
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

              <div class="box">
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
</body>
</html>
"""
    return page_html




