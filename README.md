# Accident Detection System - README

## Overview

This project demonstrates an Accident Detection System using a pre-trained machine learning model that analyzes traffic CCTV video footage. The system detects accidents from the video frames and sends alerts to a central unit when an accident is detected. This system is designed to aid in traffic management and provide real-time notifications to nearby authorities.

### Technologies Used:
- **Django**: A high-level Python web framework for rapid development.
- **TensorFlow**: A popular machine learning library to load the pre-trained accident detection model.
- **OpenCV**: A computer vision library to process the video frames.
- **HTML/CSS**: For creating the front-end of the application.

## Features:
- **Video Upload**: Allows users to upload traffic surveillance videos.
- **Accident Detection**: Uses a deep learning model to process video frames and detect accidents.
- **Feedback**: Provides immediate feedback to users regarding the result of the video analysis (Accident detected or No accident).
- **Real-Time Notifications**: Once an accident is detected, the system can trigger a notification to a central unit, which could be extended for further integration.

---

## Project Structure

### Backend (Django)

- **views.py**: Handles the backend logic for video uploading and accident detection. 
    - The **home()** view renders the home page, where users can upload videos.
    - The **process_video()** view handles the POST request when a user uploads a video, processes the video, and returns a JSON response indicating whether an accident was detected.
    - The **process_video_file()** function processes the video frames, resizes them, normalizes them, and uses the pre-trained model to predict if an accident has occurred.

### Frontend (HTML/CSS)

- **home.html**: The frontend page where users can upload videos for processing.
    - The page features a form for uploading video files.
    - A video player displays the uploaded video for preview.
    - The result of the processing is displayed once the video is analyzed, indicating whether an accident was detected or not.

---

## How It Works

1. **Upload Video**: Users upload a video of traffic CCTV footage via the web interface.
2. **Process Video**: The video is processed frame-by-frame. Each frame is resized and normalized before being passed to the trained machine learning model.
3. **Accident Detection**: The model predicts whether there is an accident in the frame. If an accident is detected (with a confidence threshold > 0.9), a notification can be triggered.
4. **Feedback to User**: After processing, a message is displayed to the user indicating whether an accident was detected in the video.
5. **Deletion of Video**: After processing, the uploaded video is removed from the server.

---

## Setup Instructions

1. **Install Dependencies**:
   - Install the required Python packages via pip:
     ```bash
     pip install django tensorflow opencv-python
     ```

2. **Set Up Django**:
   - Run the Django development server:
     ```bash
     python manage.py runserver
     ```

3. **Pre-trained Model**:
   - Ensure that the pre-trained accident detection model (`Accident_Detection_Model.h5`) is stored at the specified location: `'Accident_Detection_Model.h5'`. Update the path if necessary.

4. **Start the Application**:
   - Open your browser and navigate to `http://localhost:8000/`.
   - Upload a traffic CCTV video file and the system will analyze the footage.

---

## Demo

This project is a **demo** to showcase how accident detection works in real-time using traffic CCTV footage. The system processes videos uploaded by the user, and in a production environment, this system can be connected to live CCTV feeds from traffic cameras.

In a real-world scenario, the system would take video input directly from traffic CCTV cameras, analyze each frame, detect accidents, and send alerts to nearby central units or traffic authorities for swift action.

---

## Notes
- **Video Processing**: The current implementation processes videos that are uploaded by users. For production, you would need to replace the video upload feature with real-time video feed integration (e.g., connecting to live CCTV cameras).
- **Model Performance**: The accident detection model is based on deep learning and provides predictions for accident detection with a confidence score. This can be fine-tuned and optimized for better accuracy.
- **Threshold**: The accident detection threshold is set to 0.9 for high confidence. This value can be adjusted based on specific requirements.

---

## Future Enhancements
- **Real-Time Video Feed Integration**: Replace the video upload feature with live video stream processing from traffic cameras.
- **Centralized Alert System**: Integrate with a centralized dashboard for monitoring multiple cameras and displaying real-time alerts.
- **Multi-Language Support**: Add support for multiple languages on the frontend for broader accessibility.

---

## License

This project is open-source and available under the MIT License.

