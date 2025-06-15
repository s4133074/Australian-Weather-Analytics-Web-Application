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
            margin-left: 25px;
            text-decoration: none;
            color: #1a1a1a;
            font-weight: 600;
            font-size: 1.1rem;
            transition: color 0.2s;
        }
        nav a:hover {
            color: #0077cc;
        }
        .content-box {
            margin: 40px 80px;
            background: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        h2 {
            color: #2c3e50;
            border-bottom: 2px solid #ccc;
            padding-bottom: 8px;
        }
        ol {
            padding-left: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>
            <img src="https://github.co.jp/assets/images/customer-stories/logo-awl.png" alt="AUSTRALIAN WEATHER Logistics">
            AUSTRALIAN WEATHER Logistics
        </h1>
        <nav>
            <a href="/">Page 1A</a>
            <a href="/page2a">Page 1B</a>
            <a href="/page3a">Page 1C</a>
            <a href="/page1b">Page 2A</a>
            <a href="/page2b">Page 2B</a>
            <a href="/page3b">Page 2C</a>
        </nav>
    </header>

    <div class="content-box">
        <h2>About the Project</h2>
        <p>The purpose of our website "Australian Weather Logistics" is that it supports Australian farmers, especially those who are in rural regions. They are helped by providing them easy access to long-term historical weather data from BOM.</p>

        <p><strong>The social challenge addressed:</strong><br>
        Farmers from rural communities are struggling with unpredictable weather due to climate change. By using this site, they can understand drought cycles, compare the rainfall and temperature data, and decide which crop they want to plant accordingly.</p>

        <p><strong>How the site can be used:</strong></p>
        <ol>
            <li>The user can select a climate metric.</li>
            <li>They can enter the range of weather site IDs.</li>
            <li>They can assign a start date and end date to define the period of interest.</li>
            <li>By selecting "Search" they can view the summary table and the site data table.</li>
        </ol>
    </div>
</body>
</html>
"""
    return page_html
