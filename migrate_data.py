import mysql.connector

# -------------------------
# Local XAMPP Database
# -------------------------
local_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",          # Change this if your XAMPP MySQL has a password
    database="sentiment_db"
)

local_cursor = local_db.cursor()
local_cursor.execute("SELECT comment, sentiment FROM feedback")
rows = local_cursor.fetchall()

print(f"Found {len(rows)} records in local database.")

# -------------------------
# Railway Database
# -------------------------
railway_db = mysql.connector.connect(
    host=input("Railway Host: "),
    user=input("Railway User: "),
    password=input("Railway Password: "),
    database=input("Railway Database: "),
    port=int(input("Railway Port: "))
)

railway_cursor = railway_db.cursor()

count = 0

for row in rows:
    railway_cursor.execute(
        "INSERT INTO feedback (comment, sentiment) VALUES (%s, %s)",
        row
    )
    count += 1

railway_db.commit()

print(f"Successfully copied {count} records!")

local_db.close()
railway_db.close()