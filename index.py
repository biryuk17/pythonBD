import sqlite3
conn = sqlite3.connect('BD.sqlite')

cursor = conn.cursor()

cursor.execute("SELECT * from employees")

results = cursor.fetchall()
sum = 0
for element in results:
    sum = sum + element[5]
sum = round(sum / len(results))
print(sum)
conn.commit()