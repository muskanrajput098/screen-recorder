import streamlit as st 
import pyautogui
import cv2
import os 
import numpy as np 
import time

st.title("Screen Recorder with OpenCV")

file_name = st.text_input("Enter the file name to save the video (e.g., output.mp4)")
duration = st.slider("Select the duration of the video in seconds", 1, 60, 10)
fps = st.slider("Select the frame rate", 1, 60, 30)

if st.button("Start Recording"):
    st.success("Recording started...")
    
    screen_size = pyautogui.size() 
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    final = cv2.VideoWriter(file_name, codec, fps, screen_size)
    
    start_time = time.time()
    
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        final.write(frame)
        
        if time.time() - start_time > duration:
            break
    
    final.release()
    st.success("Recording stopped!")

    # Display download button
    with open(file_name, "rb") as video_file:
        st.download_button(
            label="Download Video",
            data=video_file,
            file_name=file_name,
            mime="video/mp4"
        )

    # Optionally delete the file after download (not until after user downloads it)
    # os.remove(file_name)

                






        



