import pyhtml

def get_page_html(form_data):
    print("About to return home page...")

    page_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather Report Application</title>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        background-color: #f4f7fb;
        color: #333;
    }
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(to right, #c6e2ff, #f0f8ff);
        padding: 20px 40px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    header h1 {
        display: flex;
        align-items: center;
        font-size: 1.8rem;
    }
    header h1 img {
        height: 50px;
        margin-right: 15px;
    }
    nav a {
        margin-left: 10px;
        text-decoration: none;
        color: #1a1a1a;
        font-weight: 600;
        font-size: 1.0rem;
        transition: color 0.2s;
    }
    nav a:hover {
        color: #0077cc;
    }
    .container {
        display: flex;
        justify-content: space-between;
        gap: 30px;
        padding: 40px 60px;
        flex-wrap: wrap;
    }
    .top-box {
        margin: 30px 60px 10px 60px;
        padding: 20px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    }
    .top-box h2 {
        margin-top: 0;
        color: #2c3e50;
        border-bottom: 2px solid #ccc;
        padding-bottom: 5px;
    }
    .box {
        flex: 1;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        min-width: 300px;
        transition: transform 0.2s ease-in-out;
    }
    .box:hover {
        transform: translateY(-5px);
    }
    .table-container {
        max-height: 300px;
        overflow-y: auto;
        margin-top: 15px;
        border: 1px solid #e0e0e0;
        font-size: 13px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        padding: 8px 12px;
        border-bottom: 1px solid #eee;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
        position: sticky;
        top: 0;
    }
    tr:nth-child(even) {
        background-color: #fafafa;
    }
    ul {
        padding-left: 18px;
    }
    li {
        margin-bottom: 8px;
    }
    .image-box img {
        width: 100%;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
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
            <a href="/page2a">Station Data</a>
            <a href="/page3a">Similar Stations</a>
            <a href="/page1b">Mission Page</a>
            <a href="/page2b">Metric Data</a>
            <a href="/page3b">Metric Similarities</a>
        </nav>
    </header>

    <div class="top-box">
        <h2>About:</h2>
        <p>Australian Weather Logistics is a web-based climate insights tool developed to simplify access to essential weather station data across Australia. The application provides a streamlined interface to filter, retrieve, and view information related to geographic weather stations and climatic metrics such as temperature, precipitation, and sunshine. This was built for users such as environmental scientists, educators, students, and weather analysts who require fast access to organized climate and station-level data without needing complex visualizations or tools.</p>
    </div>

    <div class="container">
        <div class="box"
            <h2>Description of Data Attributes:</h2>
            <div class="table-container">
                <table>
                    <thead><tr><th>Field</th><th>Description</th></tr></thead>
                    <tbody>"""

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
            <h2>Data Snapshot:</h2>
            <div class="image-box">
            </div>
            <ul>
                <li>Climate data spans from January 1st, 1970 to December 31st, 2020 — covering 50 years of Australian weather observations.</li>
                <li>The coldest recorded temperature in the dataset is −23.0°C, observed at Charlotte Pass in New South Wales during July 1994.</li>
                <li>The highest recorded daily rainfall occurred at Bellenden Ker Top Station in Queensland, where 960 mm of rain fell within a single day in January 1979.</li>
                <li>New South Wales has the largest number of weather stations in the dataset, with over 70 active stations, making it the most densely monitored region.</li>
                <li>The station with the most complete data coverage over the 50-year period is Melbourne Regional Office, offering continuous daily records for temperature, rainfall, and humidity.</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
    return page_html
