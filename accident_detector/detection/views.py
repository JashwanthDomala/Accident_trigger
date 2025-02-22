# detection/views.py
from django.shortcuts import render
from django.http import JsonResponse
import tensorflow as tf
import cv2
import numpy as np
import os
from django.core.files.storage import FileSystemStorage

# Load the pre-trained model (update with the correct path)
model = tf.keras.models.load_model('C:/Users/Student/Downloads/Accident_Detection_Model.h5')

# Home page view (allowing user to upload video)
def home(request):
    return render(request, 'home.html')

# Video processing view
def process_video(request):
    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        fs = FileSystemStorage()
        video_path = fs.save(video_file.name, video_file)
        video_url = fs.url(video_path)  # Get the URL of the uploaded video
        
        # Process the uploaded video
        result = process_video_file(video_path)
        
        # Provide feedback to the user
        if result:
            return JsonResponse({'message': 'Accident detected! Video processed successfully.', 'video_url': video_url})
        else:
            return JsonResponse({'message': 'No accident detected in the video.', 'video_url': video_url})
    return JsonResponse({'message': 'Failed to upload the video.'})

# Function to process the uploaded video
def process_video_file(video_path):
    cap = cv2.VideoCapture(video_path)  # Open the uploaded video
    accident_detected = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Preprocess the frame before passing it to the model
        frame_resized = cv2.resize(frame, (256, 256))  # Resize to 256x256 to match model input
        frame_normalized = frame_resized / 255.0  # Normalize pixel values to [0, 1]
        frame_input = np.expand_dims(frame_normalized, axis=0)  # Add batch dimension (1, 256, 256, 3)
        
        # Predict accident (1) or no accident (0)
        prediction = model.predict(frame_input)
        
        # If accident is detected (threshold of 0.9)
        if prediction > 0.9:
            accident_detected = True
            break  # Stop processing as accident is detected
    
    cap.release()
    
    # Delete the uploaded video file after processing
    os.remove(video_path)
    
    return accident_detected
