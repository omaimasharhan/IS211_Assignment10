import sqlite3 as lite

con = lite.connect('pets.db')

with con:
    cur = con.cursor()

    while True:
        id_num = input("Enter ID NUMBER of pet owner, or enter -1 to exit: ")

        if id_num == '-1':
            print('Exiting Database Query.')
            raise SystemExit

        cur.execute("SELECT first_name, last_name, person.age, name, breed, pet.age, dead "
                    "FROM person, pet, person_pet "
                    "WHERE person.id = person_pet.person_id AND "
                    "pet.id = person_pet.pet_id AND person.id = ?", (id_num,))

        person = cur.fetchall()

.        if len(person) == 0:
            print('Invalid ID number entered.')
            continue

        for row in person:
            first_name, last_name, age, pet_name, pet_type, pet_age, living = row
            if living == 1:
                print('{} {}, age {}, owned a {} named {}, '
                      'who was {} years old.'.format(first_name, last_name,
                                                      age, pet_type,
                                                      pet_name, pet_age))
            else:
                print('{} {}, age {}, owns a {} named {}, '
                      'who is {} years old.'.format(first_name, last_name,
                                                     age, pet_type,
                                                     pet_name, pet_age))
