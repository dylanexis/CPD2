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
mens_row_index3 = 48  # New athlete index
mens_row_index4 = 57  # New athlete index
mens_row_index5 = 66  # New athlete index
mens_row_index6 = 70  # New athlete index
mens_row_index7 = 73  # New athlete index
mens_row_index8 = 75  # New athlete index

# Women's CSV file details
womens_file = 'meets/Bret_Clements_Bath_Invitational_Womens_5000_Meters_Class_1_24.csv'
womens_row_index1 = 31  # Index for the chosen athlete
womens_row_index2 = 42
womens_row_index3 = 53  # New athlete index
womens_row_index4 = 63  # New athlete index
womens_row_index5 = 69  # New athlete index
womens_row_index6 = 72  # New athlete index
womens_row_index7 = 78  # New athlete index
womens_row_index8 = 82  # New athlete index

# Extract data for men's athletes
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete1 = extract_athlete_data(mens_file, mens_row_index1)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete2 = extract_athlete_data(mens_file, mens_row_index2)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete3 = extract_athlete_data(mens_file, mens_row_index3)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete4 = extract_athlete_data(mens_file, mens_row_index4)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete5 = extract_athlete_data(mens_file, mens_row_index5)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete6 = extract_athlete_data(mens_file, mens_row_index6)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete7 = extract_athlete_data(mens_file, mens_row_index7)
mens_meet_name, mens_meet_date, mens_team_results_link, mens_race_comments, mens_athlete8 = extract_athlete_data(mens_file, mens_row_index8)

# Extract data for women's athletes
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete1 = extract_athlete_data(womens_file, womens_row_index1)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete2 = extract_athlete_data(womens_file, womens_row_index2)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete3 = extract_athlete_data(womens_file, womens_row_index3)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete4 = extract_athlete_data(womens_file, womens_row_index4)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete5 = extract_athlete_data(womens_file, womens_row_index5)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete6 = extract_athlete_data(womens_file, womens_row_index6)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete7 = extract_athlete_data(womens_file, womens_row_index7)
womens_meet_name, womens_meet_date, womens_team_results_link, womens_race_comments, womens_athlete8 = extract_athlete_data(womens_file, womens_row_index8)

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
            <tr>
                <td>{athlete5_name}</td> 
                <td>{athlete5_grade}</td>
                <td>{athlete5_time}</td> 
                <td>{athlete5_place}</td>
            </tr>
            <tr>
                <td>{athlete6_name}</td> 
                <td>{athlete6_grade}</td>
                <td>{athlete6_time}</td> 
                <td>{athlete6_place}</td>
            </tr>
            <tr>
                <td>{athlete7_name}</td> 
                <td>{athlete7_grade}</td>
                <td>{athlete7_time}</td> 
                <td>{athlete7_place}</td>
            </tr>
            <tr>
                <td>{athlete8_name}</td> 
                <td>{athlete8_grade}</td>
                <td>{athlete8_time}</td> 
                <td>{athlete8_place}</td>
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
                <td>{athlete9_name}</td> 
                <td>{athlete9_grade}</td>
                <td>{athlete9_time}</td> 
                <td>{athlete9_place}</td>
            </tr>
            <tr>
                <td>{athlete10_name}</td> 
                <td>{athlete10_grade}</td>
                <td>{athlete10_time}</td> 
                <td>{athlete10_place}</td>
            </tr>
            <tr>
                <td>{athlete11_name}</td> 
                <td>{athlete11_grade}</td>
                <td>{athlete11_time}</td> 
                <td>{athlete11_place}</td>
            </tr>
            <tr>
                <td>{athlete12_name}</td> 
                <td>{athlete12_grade}</td>
                <td>{athlete12_time}</td> 
                <td>{athlete12_place}</td>
            </tr>
            <tr>
                <td>{athlete13_name}</td> 
                <td>{athlete13_grade}</td>
                <td>{athlete13_time}</td> 
                <td>{athlete13_place}</td>
            </tr>
            <tr>
                <td>{athlete14_name}</td> 
                <td>{athlete14_grade}</td>
                <td>{athlete14_time}</td> 
                <td>{athlete14_place}</td>
            </tr>
            <tr>
                <td>{athlete15_name}</td> 
                <td>{athlete15_grade}</td>
                <td>{athlete15_time}</td> 
                <td>{athlete15_place}</td>
            </tr>
            <tr>
                <td>{athlete16_name}</td> 
                <td>{athlete16_grade}</td>
                <td>{athlete16_time}</td> 
                <td>{athlete16_place}</td>
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
    #
    athlete2_name=mens_athlete2['name'],
    athlete2_grade=mens_athlete2['grade'],
    athlete2_time=mens_athlete2['time'],
    athlete2_place=mens_athlete2['place'],
    #
    athlete3_name=mens_athlete3['name'],
    athlete3_grade=mens_athlete3['grade'],
    athlete3_time=mens_athlete3['time'],
    athlete3_place=mens_athlete3['place'],
    #
    athlete4_name=mens_athlete4['name'],
    athlete4_grade=mens_athlete4['grade'],
    athlete4_time=mens_athlete4['time'],
    athlete4_place=mens_athlete4['place'],
    #
    athlete5_name=mens_athlete5['name'],
    athlete5_grade=mens_athlete5['grade'],
    athlete5_time=mens_athlete5['time'],
    athlete5_place=mens_athlete5['place'],
    #
    athlete6_name=mens_athlete6['name'],
    athlete6_grade=mens_athlete6['grade'],
    athlete6_time=mens_athlete6['time'],
    athlete6_place=mens_athlete6['place'],
    #
    athlete7_name=mens_athlete7['name'],
    athlete7_grade=mens_athlete7['grade'],
    athlete7_time=mens_athlete7['time'],
    athlete7_place=mens_athlete7['place'],
    #
    athlete8_name=mens_athlete8['name'],
    athlete8_grade=mens_athlete8['grade'],
    athlete8_time=mens_athlete8['time'],
    athlete8_place=mens_athlete8['place'],
    #
    team1_comments=mens_race_comments,
    team2_comments=womens_race_comments,
    #
    athlete9_name=womens_athlete1['name'],
    athlete9_grade=womens_athlete1['grade'],
    athlete9_time=womens_athlete1['time'],
    athlete9_place=womens_athlete1['place'],
    #
    athlete10_name=womens_athlete2['name'],
    athlete10_grade=womens_athlete2['grade'],
    athlete10_time=womens_athlete2['time'],
    athlete10_place=womens_athlete2['place'],
    #
    athlete11_name=womens_athlete3['name'],
    athlete11_grade=womens_athlete3['grade'],
    athlete11_time=womens_athlete3['time'],
    athlete11_place=womens_athlete3['place'],
    #
    athlete12_name=womens_athlete4['name'],
    athlete12_grade=womens_athlete4['grade'],
    athlete12_time=womens_athlete4['time'],
    athlete12_place=womens_athlete4['place'],
    #
    athlete13_name=womens_athlete5['name'],
    athlete13_grade=womens_athlete5['grade'],
    athlete13_time=womens_athlete5['time'],
    athlete13_place=womens_athlete5['place'],
    #
    athlete14_name=womens_athlete6['name'],
    athlete14_grade=womens_athlete6['grade'],
    athlete14_time=womens_athlete6['time'],
    athlete14_place=womens_athlete6['place'],
    #
    athlete15_name=womens_athlete7['name'],
    athlete15_grade=womens_athlete7['grade'],
    athlete15_time=womens_athlete7['time'],
    athlete15_place=womens_athlete7['place'],
    #
    athlete16_name=womens_athlete8['name'],
    athlete16_grade=womens_athlete8['grade'],
    athlete16_time=womens_athlete8['time'],
    athlete16_place=womens_athlete8['place']
)

# Save the HTML content to a file
with open('meet1_final.html', 'w') as file:
    file.write(html_content)

print("HTML file generated successfully!")
