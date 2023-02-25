import mysql
import mysql.connector
import pandas as pd
from datetime import datetime

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="akash_sql",
	database="sports"
	)

mycursor = db.cursor()

#mycursor.execute("SELECT * FROM athlete_events limit 20")

"""1) The data of Olympics that had been organized from which year to which year ?"""
#mycursor.execute("SELECT @min_val:=MIN(Year), @max_val:=MAX(year) FROM athlete_events")

"""2) What is the age of the oldest participant in Olympics till now"""
#mycursor.execute("SELECT MAX(Age) from athlete_events")
#mycursor.execute("SELECT * FROM athlete_events WHERE Age = (SELECT MAX(Age) FROM athlete_events)")

"""3) The total number of participants with the age group of 20 to 24"""
#mycursor.execute("SELECT Count(*) FROM athlete_events WHERE Age <= 26 AND Age >= 18")
#mycursor.execute("SELECT Count(*) FROM athlete_events WHERE Year <= 2016 AND Year >= 1995")

"""4) Total number of Gold Medal won by any particular country"""
#mycursor.execute("SELECT Count(Medal) FROM athlete_events where Team = 'United States' and Medal = 'Gold'")

"""5) Top 10 Countries who won the highest number of medals"""
#mycursor.execute("SELECT count(*), Team FROM athlete_events where medal <> '0' AND medal = 'Silver' group by Team order by count(*) desc limit 10")


"""6) Total number of participants from all countries"""
#mycursor.execute("SELECT count(*), Team FROM athlete_events group by Team order by count(*) desc limit 10")

"""Hypothesis 2"""

#mycursor.execute("SELECT team, (CAST(number_gold AS float(4))/CAST(number_players AS float(4)))*100 AS percent_gold, (CAST(number_silver AS float(4))/CAST(number_players AS float(4)))*100 AS percent_silver, (CAST(number_bronze AS float(4))/CAST(number_players AS float(4)))*100 AS percent_bronze, (CAST((number_gold+number_silver+number_bronze) AS float(4))/CAST(number_players AS float(4)))*100 AS percent_win FROM (SELECT team, COUNT(*) AS number_players, SUM(CASE WHEN medal='Gold' THEN 1 ELSE 0 END) AS number_gold, SUM(CASE WHEN medal='Silver' THEN 1 ELSE 0 END) AS number_silver, SUM(CASE WHEN medal='Bronze' THEN 1 ELSE 0 END) AS number_bronze FROM athlete_events LEFT JOIN noc_regions ON athlete_events.noc=noc_regions.noc GROUP BY team ORDER BY number_players DESC) AS number_medals_table LIMIT 20")

"""Hypothesis 1"""

#mycursor.execute("SELECT sport_win_percent, sport, (SUM(sport_win_percent) OVER (ORDER BY sport_win_percent DESC)) AS cumulative_percentage FROM (SELECT sport, (CAST(team_medal.sport_medal AS float(3))/CAST(3858 AS float(3)))*100 AS sport_win_percent FROM (SELECT sport, COUNT(*) AS sport_medal FROM athlete_events where team = 'United States' AND medal <> '0' group by sport order by sport_medal DESC) AS team_medal) AS final_table group by sport, sport_win_percent order by sport_win_percent DESC LIMIT 10")

"""Hypothesis 3"""

#mycursor.execute("SELECT name,sport,event FROM athlete_events where (team = 'United States' OR team='France' OR team = 'Germany') AND sport = 'Athletics' AND year = '2004' AND medal <> '0' order by name limit 20")

for x in mycursor:
	print(x)