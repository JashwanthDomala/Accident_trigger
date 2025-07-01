<h1 align="center">🚨 Accident Detection System</h1>
<p align="center">
  <strong>Real-time accident detection and reporting platform using Computer Vision and Deep Learning</strong><br>
  <em>Built with Django, TensorFlow, and OpenCV | Supports traffic monitoring via webcam or video feed</em>
</p>

---

![Screenshot](assets/screenshot.png)

---

## 📌 Overview

The **Accident Detection System** is a machine learning-powered web application that uses video input from surveillance cameras or uploaded footage to detect potential road accidents. It processes the video using a trained deep learning model and provides immediate alerts, which can assist **traffic police**, **emergency responders**, or **smart city systems** in real-time.

---

## 🚀 Features

- 📹 Upload or stream video via webcam
- 🧠 Deep learning-based accident recognition (TensorFlow)
- 🔍 Frame-by-frame video analysis
- 📤 Real-time alerts for traffic authorities
- 📊 Future-ready for integration with smart city platforms

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=fff" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</p>

---

## 📸 Screenshot

![Accident Detection Screenshot](assets/screenshot.png)

> Screenshot shows the system in action: video uploaded, displayed, and processed in real-time.

---

## 🧑‍💻 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/accident-detection.git
cd accident-detection

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
