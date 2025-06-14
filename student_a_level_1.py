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
            padding-bottom: 10px;
        }
        header h1 {
            color: black;
        }
        nav a {
            margin-left: 30px;
            text-decoration: none;
            color: black;
            font-weight: bold;
        }
        .content-container {
            margin-left: 80px;
            margin-right: 80px;
            /* optional: margin-top: 20px; if you want space below header */
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
        <h1>🌤️    AUSTRALIAN WEATHER Insight</h1>
        <nav class="nav-bar">
            <a href="/">Home</a>
            <a href="/page2a">Page 1B</a>
            <a href="/page3a">Page 1C</a>
            <a href="/page1b">Page 2A</a>
            <a href="/page2b">Page 2B</a>
            <a href="/page3b">Page 2C</a>
        </nav>
    </header>
    </body>
</body>
</html>
    """
    return page_html