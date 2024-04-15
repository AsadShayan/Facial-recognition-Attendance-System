# FaceAttendance

![FaceAttendance Logo](https://yourlogourl.com)

---

## Overview

FaceAttendance is a Python project for automating attendance tracking using face recognition technology. This project utilizes the OpenCV and face_recognition libraries to detect faces in real-time video streams, compare them with known faces, and mark attendance accordingly. It's a convenient solution for classrooms, conferences, or any setting where traditional attendance tracking methods are cumbersome.

## Features

- **Real-time Face Detection**: Utilizes OpenCV to detect faces in live video streams.
- **Face Recognition**: Uses the face_recognition library to recognize known faces.
- **Automated Attendance**: Marks attendance automatically based on recognized faces.
- **CSV Logging**: Records attendance data in a CSV file for easy management and tracking.

## Usage

1. **Installation**:
   - Clone the repository: `git clone https://github.com/yourusername/FaceAttendance.git`
   - Install dependencies: `pip install -r requirements.txt`

2. **Prepare Known Faces**:
   - Add images of individuals whose attendance you want to track to the `photos` directory.
   - Ensure each image is named after the respective individual (e.g., `dar.jpeg`, `talal.jpeg`).

3. **Run the Script**:
   - Execute the `attendance.py` script: `python attendance.py`.
   - Ensure your webcam is connected and positioned correctly.

4. **View Attendance**:
   - Attendance data is logged in CSV files named by the current date (e.g., `15-04-24.csv`).
   - Open the CSV files using spreadsheet software to view and manage attendance records.

## Dependencies

- [`face_recognition`](https://github.com/ageitgey/face_recognition): A Python library for face recognition built on top of dlib.
- [`opencv-python`](https://github.com/opencv/opencv-python): OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.
- [`numpy`](https://github.com/numpy/numpy): Fundamental package for scientific computing with Python.

## Contribution

Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the need for a hassle-free attendance tracking solution.
- Special thanks to the creators and maintainers of the OpenCV and face_recognition libraries for their invaluable contributions to the field of computer vision.

## Authors

- [Your Name](https://github.com/yourusername) - Initial work

--- 

Feel free to customize the README with additional information or styling according to your preferences!
