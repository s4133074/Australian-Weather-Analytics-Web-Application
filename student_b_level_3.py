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