import sqlite3

def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_into_info(name, group, direction):
    try:
        sqlite_connection = sqlite3.connect('lab_rats.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("""INSERT INTO lab_rats(name, group, direction) VALUES(?, ?, ?, ?);""", (name, group, direction))
        sqlite_connection.commit()
        print("Данные успешно вставлены в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def create(g):
    try:
        sqlite_connection = sqlite3.connect('lab_rats.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("""CREATE TABLE IF NOT EXISTS lab_rats(id INTEGER PRIMARY KEY, name STRING NOT NULL, group STRING NOT NULL, direction STRING NOT NULL);""")
        print(g)
        sqlite_connection.commit()
        print("Данные успешно вставлены в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def insert_photo(photo, rat_id):
    try:
        sqlite_connection = sqlite3.connect('lab_rats.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        create_rats_photos_table = """INSERT INTO lab_rats_photos (photo, rat_id) VALUES (?, ?);"""
        rat_photo = convert_to_binary_data(photo)
        # Преобразование данных в формат кортежа
        data_tuple = (rat_photo, rat_id)
        cursor.execute(create_rats_photos_table, data_tuple)
        sqlite_connection.commit()
        print("Изображение успешно вставлено как BLOB в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

a = insert_photo("/Users/linaquinzel/Dev/rats_detector/faces_base/19.jpg", 19)






