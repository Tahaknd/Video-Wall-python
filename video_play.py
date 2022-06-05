import os
import cv2
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD')
)
cursor = conn.cursor()

cursor.execute("SELECT video_path FROM videos WHERE user_id = " + os.getenv('USER_ID'))
records = cursor.fetchall()

while True:
    for record in records:
        print(record[0])

        title = record[0]
        video = cv2.VideoCapture(os.getenv('VIDEOS_PATH') + record[0])

        while video.isOpened():
            ret, frame = video.read()
            if ret is False:
                break

            frame = cv2.resize(frame, dsize=(1920, 1080), fx=2, fy=2)
            cv2.imshow(title, frame)

            if cv2.waitKey(15) == ord("q"):
                break
            elif cv2.waitKey(15) == ord("f"):
                quit()

        video.release()
