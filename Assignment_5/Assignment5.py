	# Program Name: Assignment5.py (use the name the program is saved as)
	# Course: IT3883/Section W01
	# Student Name: Jared Abbott
	# Assignment Number: Lab 5
	# Due Date: 11/20/ 2026
	# Purpose: What does the program do (in a few sentences)?
	# List Specific resources used to complete the assignment.
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


