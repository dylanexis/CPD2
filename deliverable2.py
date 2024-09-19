import os
import csv

folder_path = 'meets'

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        csv_file_path = os.path.join(folder_path, filename)


with open(csv_file_path, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)
    
    meet_name = data[0][0]
    meet_date = data[1][0]
    team_results_link = data[2][0]
    race_comments = data[3][0]




    html_content = f'''<!DOCTYPE html>
    <html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel = "stylesheet" href = "css/reset.css">
   <link rel = "stylesheet" href = "css/style.css">
   <title>{meet_name} Country Meet</title>
</head>
<body>


   <header>
       <h1>{meet_name}</h1>
       <h2>{meet_date}</h2>
   </header>
   <div>{team_results_link}</div>
   <div>{race_comments}</div>
</body>
</html>
'''

# Write to an HTML file
with open('cpd2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file generated: cpd2.html")
