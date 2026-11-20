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


<img width="1920" height="1080" alt="PycharmAssignment5OutputScreenshot(3)" src="https://github.com/user-attachments/assets/0c34bc43-e5be-4beb-92c9-75d5855f0773" />
