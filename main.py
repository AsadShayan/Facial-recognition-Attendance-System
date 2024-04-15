import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

# Initialize the video capture object for the default camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Load known faces
dar_image = face_recognition.load_image_file("photos/dar.jpeg")
# then the face recog library encodes all the raw data of the image
dar_encoding = face_recognition.face_encodings(dar_image)[0]

# same goes for all the images
talal_image = face_recognition.load_image_file("photos/talal.jpeg")
talal_encoding = face_recognition.face_encodings(talal_image)[0]

makar_image = face_recognition.load_image_file("photos/makar.jpeg")
makar_encoding = face_recognition.face_encodings(makar_image)[0]

peer_image = face_recognition.load_image_file("photos/peer.jpeg")
peer_encoding = face_recognition.face_encodings(peer_image)[0]

shayan_image = face_recognition.load_image_file("photos/shayan.jpeg")
shayan_encoding = face_recognition.face_encodings(shayan_image)[0]

# Load the image
ryan_image = face_recognition.load_image_file("photos/ryan.jpeg")
# Get the face encodings (if any)
ryan_encoding = face_recognition.face_encodings(ryan_image)
# Check if any face encodings were found
if ryan_encoding:
    # If at least one face encoding is found, use the first one
    ryan_encoding = ryan_encodings[0]
else:
    # Handle the case where no face encodings are found
    print("No face found in the image 'ryan.jpeg'")
    # You might want to handle this case differently based on your requirements
known_faces_encoding = [
    dar_encoding,
    talal_encoding,
    peer_encoding,
    makar_encoding,
    shayan_encoding,
    ryan_encoding
]

# the list for all the known faces we have
known_faces_names = [
    "dar",
    "talal",
    "makar",
    "peer",
    "shayan",
    "ryan"
]

# Create a copy of the known face names for expected students
expected_students = known_faces_names.copy()

# Initialize variables for face locations and encodings
face_locations = []
face_encodings = []

# Get the current time
now = datetime.now()
current_date = now.strftime("%d-%m-%y")

# Open a CSV file for writing attendance
with open(f"{current_date}.csv", "w+", newline="") as f:
    writer = csv.writer(f)

    # Start the main video capture loop
    while True:
        _, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces in the frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                # Add text if the person is present
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottom_left_corner_of_text = (10, 100)
                font_scale = 1.5
                font_color = (255, 0, 0)
                thickness = 3
                line_type = 2
                cv2.putText(frame, f"{name} PRESENT", bottom_left_corner_of_text, 0, font_scale, font_color, thickness, line_type)

                if name in expected_students:
                    expected_students.remove(name)
                    current_time = now.strftime("%H-%M-%S")
                    writer.writerow([name, current_time])

        cv2.imshow("Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()