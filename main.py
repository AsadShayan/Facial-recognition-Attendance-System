import tensorflow as tf
import cv2
import numpy as np
import os
from datetime import datetime
import csv

# Load the pre-trained face detection model from TensorFlow
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load known faces and their encodings
def load_known_faces_and_names(directory):
    known_faces = []
    known_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
            image = cv2.imread(os.path.join(directory, filename))
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            face_locations = face_detector.detectMultiScale(rgb_image, scaleFactor=1.1, minNeighbors=5)
            if len(face_locations) > 0:
                x, y, w, h = face_locations[0]
                face_image = rgb_image[y:y+h, x:x+w]
                face_encoding = tf.image.resize(face_image, (160, 160)).numpy().flatten()
                known_faces.append(face_encoding)
                known_names.append(os.path.splitext(filename)[0])
    return known_faces, known_names

known_faces, known_names = load_known_faces_and_names("photos")

# Initialize the video capture object for the default camera
cap = cv2.VideoCapture(0)

# Get the current time
now = datetime.now()
current_date = now.strftime("%d-%m-%y")

# Open a CSV file for writing attendance
with open(f"{current_date}.csv", "w+", newline="") as f:
    writer = csv.writer(f)

    # Start the main video capture loop
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        face_locations = face_detector.detectMultiScale(rgb_small_frame, scaleFactor=1.1, minNeighbors=5)
        face_encodings = []

        for (x, y, w, h) in face_locations:
            face_image = rgb_small_frame[y:y+h, x:x+w]
            face_encoding = tf.image.resize(face_image, (160, 160)).numpy().flatten()
            face_encodings.append(face_encoding)

        for face_encoding in face_encodings:
            distances = [np.linalg.norm(face_encoding - known_face) for known_face in known_faces]
            best_match_index = np.argmin(distances)
            if distances[best_match_index] < 0.6:
                name = known_names[best_match_index]

                # Add text if the person is present
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottom_left_corner_of_text = (10, 100)
                font_scale = 1.5
                font_color = (255, 0, 0)
                thickness = 3
                line_type = 2
                cv2.putText(frame, f"{name} PRESENT", bottom_left_corner_of_text, font, font_scale, font_color, thickness, line_type)

                if name in known_names:
                    known_names.remove(name)
                    current_time = now.strftime("%H-%M-%S")
                    writer.writerow([name, current_time])

        cv2.imshow("Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
