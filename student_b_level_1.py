import pyhtml  # Assuming pyhtml contains get_results_from_query()

def get_page_html(form_data):
    print("About to return home page...")

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Compare Metric Similarities</title>
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
        .nav-bar {{
            display: flex;
            justify-content: space-around;
            background-color: #ddd;
            padding: 10px;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }}
        form {{
            background-color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            width: 100%;
            max-width: 600px;
            margin-bottom: 20px;
        }}
        label {{
            display: block;
            margin: 10px 0 5px;
            font-weight: bold;
        }}
        input[type="text"],
        input[type="date"],
        input[type="number"],
        select {{
            width: 100%;
            padding: 10px;
            font-size: 14px;
            border: 2px solid #ccc;
            border-radius: 8px;
            box-sizing: border-box;
            margin-bottom: 10px;
        }}
        button {{
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: #45a049;
        }}
        .table-container {{
            max-height: 400px;
            overflow-y: auto;
            background-color: #fff;
            border: 1px solid #ccc;
            width: 100%;
            max-width: 900px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        th, td {{
            padding: 8px 12px;
            border: 1px solid #bbb;
            text-align: left;
        }}
        th {{
            background-color: #f5f5f5;
            position: sticky;
            top: 0;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
    </style>
</head>
<body>

<header>
</header>

<nav class="nav-bar">
    <p><a href="/">Home</a></p>
    <p><a href="/page2a">Go to Page 2A</a></p>
    <p><a href="/page3a">Go to Page 3A</a></p>
    <p><a href="/page1b">Mission Statement</a></p>
    <p><a href="/page2b">Go to Page 2B</a></p>
    <p><a href="/page3b">Go to Page 3B</a></p>
</nav>


<div class="layout">
    <div class="main-content">
        <div class="box">
            <h3>How to Use Website</h3>
            <p>The Metric Similarity Comparison page helps you see how different climate factors—like rainfall, temperature, and sunshine—have changed over two time periods. First, pick one climate metric as your main focus from the dropdown menu (for example, Rainfall or Max Temperature). Then, enter two sets of start and end dates to compare how that metric has changed over time.

You can also choose how many similar metrics you want to compare—up to 5. After you hit submit, the page will show a table with the totals or averages for each time period, how much they changed, and how closely other metrics follow the same pattern as your chosen one. This makes it easy for users like environmental consultants or students to quickly understand trends and make better decisions using real climate data.</p>
        </div>
    """
    # PERSONAS
    try:
        print("Fetching personas...")
        persona_query = "SELECT name FROM persona;"
        persona_results = pyhtml.get_results_from_query("database/climate.db", persona_query)

        page_html += """
        <div class="box">
            <h2>Target Personas</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>

                    </tr>
                </thead>
                <tbody>
        """
        if persona_results:
            for name in persona_results:
                page_html += f"""
                <tr>
                    <td>{name}</td>

                </tr>
                """
        else:
            page_html += "<tr><td colspan='4'>No personas found.</td></tr>"
        page_html += "</tbody></table></div>"
    except Exception as e:
        print(f"Error fetching personas: {e}")
        page_html += f"<p style='color:red;'>Error loading personas: {e}</p>"

    page_html += "</div></div></body></html>"
    
    # TEAM MEMBERS
    try:
        print("Fetching team members...")
        team_query = "SELECT student_id, student_name FROM team_members;"
        team_results = pyhtml.get_results_from_query("database/climate.db", team_query)

        page_html += "<div class='box'><h2>Team Members</h2><ul>"
        if team_results:
            for student_id, student_name in team_results:
                page_html += f"<li><strong>{student_name}</strong> – Student ID: {student_id}</li>\n"
        else:
            page_html += "<li>No team members found.</li>"
        page_html += "</ul></div>"
    except Exception as e:
        print(f"Error fetching team members: {e}")
        page_html += f"<p style='color:red;'>Error loading team members: {e}</p>"


    page_html += "</div></div></body></html>"
    return page_html