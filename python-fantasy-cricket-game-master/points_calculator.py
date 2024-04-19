import sqlite3

db = sqlite3.connect("fandatabase.db")
cursor = db.cursor()
cursor.execute("SELECT * FROM match")
row = cursor.fetchall()

def calculate_points(row):
    points = 0.0
    score = row[1]
    try:
        strike_rate = float(row[1]) / float(row[2]) 
    except:
        strike_rate = 0
    fours, sixes = float(row[3]), float(row[4])

    twos = int((score - 4 * fours - 6 * sixes) / 2)
    wickets = 10 * float(row[8])
    try:
        economy = float(row[7]) / (float(row[5]) / 6)
    except:
        economy = 0
    Fielding = float(row[9]) + float(row[10]) + float(row[11])

   
    points += (fours + 2 * sixes + 10 * Fielding + twos + wickets)
    if score > 100:
        points += 10  
    elif score >= 50:
        points += 5  
    if strike_rate > 1:  
        points += 4

    elif strike_rate >= 0.8:
        points += 2 
    if wickets >= 5:
        points += 10  
    elif wickets > 3:
        points += 5  
    if economy >= 3.5 and economy <= 4.5:
        points += 4  
    elif economy >= 2 and economy < 3.5:
        points += 7  
    elif economy < 2:
        points += 10 
    return points

player_points = {}
for i in row:
    player_points[i[0]] = calculate_points(i)

print(player_points)
