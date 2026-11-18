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
import psycopg2
conn = psycopg2.connect(
        database="Assginment5Database",
        user="postgres",
        password="1234abcd",
        host="localhost",
        port="5432")
cur = conn.cursor()
cur.execute("SELECT day_of_week, AVG(temperature_value) AS average_temp FROM assignment5table WHERE day_of_week IN ('Thursday', 'Sunday')GROUP BY day_of_week;")
sqlcode = cur.fetchall()
for column in sqlcode:
    print(column)
    cur.close()


