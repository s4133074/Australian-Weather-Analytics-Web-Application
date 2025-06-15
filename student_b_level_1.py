import pyhtml  # Assuming pyhtml contains get_results_from_query()

def get_page_html(form_data):
    print("About to return home page...")

    styles = """
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

    """

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Database Web-App Demo</title>
    <style>{styles}</style>

</head>
<body>
    <header>
        <h1>
            <img src="https://github.co.jp/assets/images/customer-stories/logo-awl.png" alt="AUSTRALIAN WEATHER Logistics" width = 150px>
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


    <div class="top-box">
        <h2>Social Challenges:</h2>
        <p>This website helps tackle social challenges by making weather and climate data easy to access and understand for everyone. It shows historical trends and changes in weather that can help people like planners, farmers, or community groups—spot risks such as floods, heatwaves, or droughts. The simple design, filters, and clear language make it easier for users with different backgrounds to use. By supporting fair access to information, the site helps communities prepare for and respond to climate-related problems more equally.</p>
    </div>

    
        <div class="top-box">
        <h2>Usability:</h2>
        <p>This website can be used to explore and analyze climate and weather data across different regions and time periods in Australia. Users can filter the data by state, time range, climate variables (like rainfall or temperature). For example, an environmental scientist can view trends over the past decade, or a student can explore raw data for a school project. The site also provides background information, user personas, and team details, helping users understand its purpose and context. Overall, it supports informed decision-making in areas like planning, research, and sustainability.</p>
    </div>

    """
    # PERSONAS
    try:
        print("Fetching personas...")
        persona_query = "SELECT name,background,needs_goals,skills_experience,painpoints FROM persona;"
        persona_results = pyhtml.get_results_from_query("database/climate.db", persona_query)

        page_html += """
        <div class="box">
            <h2>Target Personas</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Background</th>
                        <th>Needs and Goals</th>
                        <th>Skills and Experience</th>
                        <th>Painpoints</th>
                    </tr>
                </thead>
                <tbody>
        """
        if persona_results:
            for name, background,needs_goals,skills_experience,painpoints in persona_results:
                page_html += f"""
                <tr>
                    <td>{name}</td>
                    <td>{background}</td>
                    <td>{needs_goals}</td>
                    <td>{skills_experience}</td>
                    <td>{painpoints}</td>
                </tr>
                """
        else:
            page_html += "<tr><td colspan='4'>No personas found.</td></tr>"
        page_html += "</tbody></table></div>"
    except Exception as e:
        print(f"Error fetching personas: {e}")
        page_html += f"<p style='color:red;'>Error loading personas: {e}</p>"

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


    # Close divs and return full page
    page_html += "</div></div></body></html>"
    return page_html