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