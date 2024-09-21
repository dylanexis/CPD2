import os
import csv

def extract_athlete_data(csv_file, row_index):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

        # General meet information
        meet_name = data[0][0]
        meet_date = data[1][0]
        team_results_link = data[2][0]
        race_comments = ' '.join(data[3])

        # Extract a single athlete's info based on the provided row index
        athlete_info = data[row_index]
        athlete = {
            'placement': athlete_info[0],
            'grade': athlete_info[1],
            'name': athlete_info[2],
            'time': athlete_info[4],
            'place': athlete_info[0]
        }

    return meet_name, meet_date, team_results_link, race_comments, athlete

# Men's CSV file details
mens_file = 'meets/Bret_Clements_Bath_Invitational_Mens_5000_Meters_Class_1_24.csv'
mens_row_index1 = 43  # Index for the chosen athlete
mens_row_index2 = 46

# Women's CSV file details
womens_file = 'meets/Bret_Clements_Bath_Invitational_Womens_5000_Meters_Class_1_24.csv'
womens_row_index1 = 31  # Index for the chosen athlete
womens_row_index2 = 42


# Extract data
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete1 = extract_athlete_data(mens_file, mens_row_index1)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete2 = extract_athlete_data(mens_file, mens_row_index2)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete1 = extract_athlete_data(womens_file, womens_row_index1)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete2 = extract_athlete_data(womens_file, womens_row_index2)
# Template for the HTML file
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Skyline Cross Country</title>
    <style>
        table {{
            border: 4px solid lightblue;
            margin: auto;
            width: 75%;
        }}

        div {{
            margin: 20px;
        }}

        td{{
            text-align: center;
        }}

        h3 {{
            text-align:center;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Bret Clements Bath Invitational</h1>
        <nav>
            <ul>
                <li><a href="cpd2.html">Home</a></li>
                <li><a href="cpd2.html#meets">Meets</a></li>
                <li><a href="#photo-gallery">Photo Gallery</a></li>
            </ul>
        </nav>
    </header>
    <section id='meet1'>
        <h2>Men's 5000 Meters Class 1</h2>
        <div>{team1_comments}</div>
        <h3>Skyline Runners</h3>
        <table>
            <tr>
                <th>Name</th> 
                <th>Grade</th>
                <th>Time</th> 
                <th>Place</th>
            </tr>
            <tr>
                <td>{athlete1_name}</td> 
                <td>{athlete1_grade}</td> 
                <td>{athlete1_time}</td>
                <td>{athlete1_place}</td>
            </tr>
            <tr>
                <td>{athlete2_name}</td> 
                <td>{athlete2_grade}</td>
                <td>{athlete2_time}</td> 
                <td>{athlete2_place}</td>
            </tr>
        </table>

        <h2>Women's 5000 Meters Class 1</h2>
        <div>{team2_comments}</div>
        <h3>Skyline Runners</h3>
        <table>
            <tr>
                <th>Name</th>
                <th>Grade</th>
                <th>Time</th> 
                <th>Place</th>
            </tr>
            <tr>
                <td>{athlete3_name}</td> 
                <td>{athlete3_grade}</td>
                <td>{athlete3_time}</td> 
                <td>{athlete3_place}</td>
            </tr>
            <tr>
                <td>{athlete4_name}</td> 
                <td>{athlete4_grade}</td>
                <td>{athlete4_time}</td> 
                <td>{athlete4_place}</td>
            </tr>
        </table>
    </section>
    <footer></footer>
</body>
</html>
"""

# Create the HTML content by formatting the template with the extracted data
html_content = html_template.format(
    athlete1_name=mens_athlete1['name'],
    athlete1_grade=mens_athlete1['grade'],
    athlete1_time=mens_athlete1['time'],
    athlete1_place=mens_athlete1['place'],
    athlete2_name=mens_athlete2['name'],
    athlete2_grade=mens_athlete2['grade'],
    athlete2_time=mens_athlete2['time'],
    athlete2_place=mens_athlete2['place'],
    team1_comments=mens_race_comments,
    athlete3_name=womens_athlete1['name'],
    athlete3_grade=womens_athlete1['grade'],
    athlete3_time=womens_athlete1['time'],
    athlete3_place=womens_athlete1['place'],
    athlete4_name=womens_athlete2['name'],
    athlete4_grade=womens_athlete2['grade'],
    athlete4_time=womens_athlete2['time'],
    athlete4_place=womens_athlete2['place'],
    team2_comments=womens_race_comments
)

# Save the HTML content to a file
with open('meet1_final.html', 'w') as file:
    file.write(html_content)

print("HTML file generated successfully!")