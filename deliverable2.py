import os
import csv

csv_file = 'meets/Bret_Clements_Bath_Invitational_Mens_5000_Meters_J.V._24.csv'

with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

            #General Meet information
            meet_name = data[0][0]
            meet_date = data[1][0]
            team_results_link = data[2][0]
            race_comments = ' '.join(data[3])
            
            # Eshuan Kuan info
            Eshuan_info = data[26]
        
            athlete_placement1 = Eshuan_info[0]
            athlete_grade1 = Eshuan_info[1]
            athlete_name1 = Eshuan_info[2]
            athlete_pic1 = Eshuan_info[7]

            # Dylan Hanley
            Dylan_info = data[30]
        
            athlete_placement2 = Dylan_info[0]
            athlete_grade2 = Dylan_info[1]
            athlete_name2 = Dylan_info[2]
            athlete_pic2 = Dylan_info[7]

            # Raphael Hanley
            Raphael_info = data[34]
        
            athlete_placement3 = Raphael_info[0]
            athlete_grade3 = Raphael_info[1]
            athlete_name3 = Raphael_info[2]
            athlete_pic3 = Raphael_info[7]





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
   <div>
   <h2>Meet Results</h2>
   <p><a href="{team_results_link}">Results Available Here</a></p>

   <h2>Star Runners</h2>
        <!-- Eshuan's Information -->
  
   <div>{athlete_name1}, Grade: {athlete_grade1}</div>
   <div>
    <img src="{athlete_pic1}" alt="{athlete_name1} Photo"> </div>

        <!-- Dylan's information -->
    <div>{athlete_name2}, Grade: {athlete_grade2}</div>
   <div>
    <img src="{athlete_pic2}" alt="{athlete_name2} Photo"> </div>

         <!-- Raphael's information -->
    <div>{athlete_name3}, Grade: {athlete_grade3}</div>
   <div>
    <img src="{athlete_pic3}" alt="{athlete_name3} Photo"> </div>

   
   <h2>Overall Race Comments</div>
   <div>{race_comments}</div>

   <h2>Photo Gallery</h2>

</body>
</html>
'''

# Write to an HTML file
with open('cpd2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file generated: cpd2.html")
