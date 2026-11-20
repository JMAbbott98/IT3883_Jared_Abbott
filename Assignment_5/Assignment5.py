	# Program Name: Assignment5.py (use the name the program is saved as)
	# Course: IT3883/Section W01
	# Student Name: Jared Abbott
	# Assignment Number: Lab 5
	# Due Date: 11/20/ 2026
	# Purpose: The purpose of this program is get SQL and Python to speak to each other
	# List https://www.youtube.com/watch?v=u62SBWmThV8
    # https://www.w3schools.com/sql/sql_in.asp
    # https://www.w3schools.com/sql/sql_where.asp
    # https://www.youtube.com/watch?v=LJC8277LONg
    # https://www.youtube.com/watch?v=M2NzvnfS-hI&t=1202s
    # https://www.youtube.com/watch?v=pd-0G0MigUA
    # https://keycombiner.com/collections/notepad/

import sqlite3
conn = sqlite3.connect('assignment5.db')
z = conn.cursor()
#z.execute('''CREATE TABLE assignment5table (
 #ID INTEGER PRIMARY KEY AUTOINCREMENT,
 #Day_of_Week TEXT,
 #Temperature_Value float) ''')
#z.execute("INSERT INTO assignment5table VALUES (NULL, 'Friday', 83.4)")
rows = z.fetchall()
for row in rows:
    z.execute("INSERT INTO assignment5table VALUES (?, ?, ?)", row)
z.execute("SELECT day_of_week, AVG(temperature_value) AS average_temp FROM assignment5table WHERE day_of_week IN ('Thursday', 'Sunday') GROUP BY day_of_week;")

print(z.fetchall())
conn.commit()
conn.close()

