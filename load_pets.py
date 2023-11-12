import sqlite3
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

data = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23),
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

for item in data:
    cursor.execute("INSERT INTO person VALUES (?, ?, ?, ?)", item[:4])
    cursor.execute("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", item[4:])
    if len(item) == 6:
        cursor.execute("INSERT INTO person_pet VALUES (?, ?)", (item[0], item[4]))


conn.commit()
conn.close()