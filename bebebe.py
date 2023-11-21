import csv
import os
import sqlite3

# """
def save_user_data(user_id, name, surname):
    found = False

    if not os.path.exists("ud.csv"):
        file = open("ud.csv", "w")
        file.write("id,name,surname,age\n")
        file.close()

    file = open("ud.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        # print('Read', row)
        if row.__len__() > 0 and row[0] == user_id:
            found = True
            break
    file.close()
    print('user' + str(user_id) + ' found : ' + str(found))

    if not found:
        file = open("ud.csv", "a", newline="")
        writer = csv.writer(file)
        writer.writerow([user_id, name, surname])
        file.close()
        print('User' + str(user_id) + ' added')
    else:
        file = open("ud.csv", "r")
        reader = csv.reader(file)
        users = []
        for row in reader:
            if row[0] == user_id:
                if name != None and name != '':
                    row[1] = name
                if surname != None and surname != '':
                    row[2] = surname
                users.append(row)
            else:
                users.append(row)
        file.close()

        file = open("ud.csv", "w", newline="")
        writer = csv.writer(file)
        # writer.writerow(["id", "name", "surname"])
        for row in users:
            if row.__len__() < 1:
                continue
            writer.writerow(row)
        file.close()
# """



# def get_id():


# save_user_data('123', 'Buba', 'Kastorsky')
# save_user_data('222', 'Beba', 'bebebe')
# save_user_data('123', 'BUBA', 'Kastorsky')
# save_user_data('333', 'alice', 'pozniakovska')
# save_user_data('111', 'alice', '')
# save_user_data('111',    ''  , 'pozniakovska')
# save_user_data('111',    ''  , '')

'''
def save_user_data(user_id, name, surname):
    conn = sqlite3.connect("user_data.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT
        )""")

    cur.execute("INSERT INTO users (id, name, surname) VALUES (?, ?, ?)", (id, name, surname))
    conn.commit()
    conn.close()


save_user_data('123', 'Buba', 'Kastorsky')


'''
