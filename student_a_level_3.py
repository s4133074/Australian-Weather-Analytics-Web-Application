def get_page_html(form_data):
    print("About to return page 2")

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Station Comparison</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #fff;
            border-bottom: 1px solid #ccc;
        }}
        .nav-top {{
            display: flex;
            gap: 15px;
        }}
        .nav-bar {{
            display: flex;
            justify-content: space-around;
            background-color: #ddd;
            padding: 10px;
        }}
        .login-signup {{
            display: flex;
            gap: 10px;
        }}
        .container {{
            padding: 20px;
        }}
        form {{
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        label, select, input, button {{
            display: block;
            margin: 10px 0;
            padding: 8px;
            width: 100%;
        }}
        button {{
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }}
        h2 {{
            color: #003366;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
            background-color: #fff;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #cce5ff;
        }}
        .selected {{
            font-weight: bold;
            color: green;
        }}
    </style>
</head>
<body>

    <header>
        <div class="nav-top">
            <strong><img src="images/pic4.png" style="width: 20%; height: auto;"></strong>
        </div>
        <div class="login-signup">
            <button>LOG IN</button>
            <button>SIGN UP</button>
        </div>
    </header>

    <nav class="nav-bar">
        <p><a href="/">Home</a></p>
        <p><a href="/page2a">Go to page 2A</a></p>
        <p><a href="/page3a">Go to page 3A</a></p>
        <p><a href="/page1b">Go to page 1B</a></p>
        <p><a href="/page2b">Go to page 2B</a></p>
        <p><a href="/page3b">Go to page 3B</a></p>
    </nav>

    <div class="container">
        <h2>Weather Station Similarity Finder</h2>

        <form action="/process_query" method="POST">
            <label for="reference_station">Reference Weather Station:</label>
            <select id="reference_station" name="reference_station">
                <option value="Melbourne Airport">Melbourne Airport</option>
                <option value="Ballarat">Ballarat</option>
                <option value="Bendigo">Bendigo</option>
            </select>

            <label for="climate_metric">Climate Metric:</label>
            <select id="climate_metric" name="climate_metric">
                <option value="avg_temp">Average Temperature</option>
                <option value="rainfall">Rainfall</option>
                <option value="wind_speed">Wind Speed</option>
            </select>

            <label for="start_period">Start Date (Period 1):</label>
            <input type="date" id="start_period" name="start_period">

            <label for="end_period">End Date (Period 1):</label>
            <input type="date" id="end_period" name="end_period">

            <label for="start_period_2">Start Date (Period 2):</label>
            <input type="date" id="start_period_2" name="start_period_2">

            <label for="end_period_2">End Date (Period 2):</label>
            <input type="date" id="end_period_2" name="end_period_2">

            <label for="num_results">Number of Similar Stations to Show:</label>
            <input type="number" id="num_results" name="num_results" value="2" min="1" max="10">

            <button type="submit">Find Similar Stations</button>
        </form>

        <!-- Static sample result table for preview -->
        <table>
            <tr>
                <th>Weather Station</th>
                <th>Average Temp<br>(2005–2009)</th>
                <th>Average Temp<br>(2010–2015)</th>
                <th>% Change</th>
                <th>Difference from<br>Melbourne Airport</th>
            </tr>
            <tr>
                <td class="selected">Melbourne Airport</td>
                <td>22.5 °C</td>
                <td>22.7 °C</td>
                <td>+0.88%</td>
                <td>0.0% <span class="selected">(selected)</span></td>
            </tr>
            <tr>
                <td>Ballarat</td>
                <td>17.2 °C</td>
                <td>17.6 °C</td>
                <td>+0.23%</td>
                <td>-0.65%</td>
            </tr>
            <tr>
                <td>Bendigo</td>
                <td>16.9 °C</td>
                <td>17.0 °C</td>
                <td>+0.59%</td>
                <td>-0.29%</td>
            </tr>
        </table>

    </div>
</body>
</html>
"""
    return page_html
