import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    person_id = int(input("Enter a person's ID (or -1 to exit): ")
    if person_id == -1:
        break

    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person_data = cursor.fetchone()

    if person_data:
        print(f"{person_data[0]} {person_data[1]}, {person_data[2]} years old")

        cursor.execute("SELECT name, breed, age FROM pet WHERE id IN (SELECT pet_id FROM person_pet WHERE person_id = ?)", (person_id,))
        pets_data = cursor.fetchall()

        if pets_data:
            for pet in pets_data:
                print(f"Owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
        else:
            print("This person has no pets.")
    else:
        print("Person not found.")

conn.close()