import cv2
import face_recognition
import sqlite3
from io import BytesIO

def rats_detector():
    # Get a reference to webcam
    video_capture = cv2.VideoCapture(0)
    # Initialize variables
    face_locations = []
    face_encodings = []
    frame_number = 0
    known_faces = []
    database = []

    def take_photo_and_id(t):
        # получаем фото и айди из базы данных
        try:
            sqlite_connection = sqlite3.connect('lab_rats.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            take_rats_photos = """SELECT photo, rat_id FROM lab_rats_photos;"""
            cursor.execute(take_rats_photos)
            photos = cursor.fetchall()
            print("Изображения успешно получены")
            cursor.close()
            return(photos)

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")


    def take_id_and_name(t):
        # получаем айдишники, имена и направления из базы данных
        try:
            sqlite_connection = sqlite3.connect('lab_rats.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            take_rats = """SELECT id, name, direction FROM lab_rats;"""
            cursor.execute(take_rats)
            data = cursor.fetchall()
            print("Данные успешно получены")
            cursor.close()
            return(data)

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def counter(r: list, value) -> int:
        # счётчик для поиска номера нужного нам элемента в списке
        c = -1
        for i in r:
            if i == value:
                c += 1
                return(c)
            else:
                c += 1
        return(8888)

    ph = take_photo_and_id("f") # получаем айди и фото
    ids = take_id_and_name("f") # получаем остальную информацию
    rats_id_list = []
    for b in ids:
        rats_id_list.append(b[0])
    print(ids)
    for o in ph:
        fil = BytesIO(o[0])
        database.append(fil)
    # for n in ids:
    #     aidie = n[0]
    #     name = n[1]
    #     direction = n[2]

    for k in database:
        image = face_recognition.load_image_file(k)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)

    while True:
	
    # Grab a single frame of video
	
        ret, frame = video_capture.read()

        frame_number += 1

        if not ret:
    	
            break 
	
# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
	
        rgb_frame = frame[:, :, ::-1]
 
	
# Find all the faces in the current frame of video
	
        face_locations = face_recognition.face_locations(rgb_frame, model="cnn")

        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
    	
# See if the face is a match for the known face(s)
    	
            match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
        # получаем номер распознанной фотографии
            number = counter(match, True)
            if number != 8888:
            # получаем айди распознанного пользователя
                recognized_man: int = ph[number][1]
            # получаем номер кортежа с информацией о распознанном пользователе
                number_id = counter(rats_id_list, recognized_man)
                name_man = ids[number_id][1]
                print(name_man)
            else:
                print("I see no one")

 

# Display the results
	
        for top, right, bottom, left in face_locations:
    	
# Draw a box around the face
    	
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
 
	
# Display the resulting image
	
            cv2.imshow('Video', frame)
 
	
# Hit 'q' on the keyboard to quit!
	
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
rats_detector()
