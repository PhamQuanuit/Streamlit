
import cv2
import streamlit as st
import detect
import numpy as np

def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_title="Phạm Minh Quân_19522084")

FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture()

def main(img):
    # img = np.array(img)
    # showimg(img)
    img = detect.detect(img)
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return frame

if __name__ == '__main__':

    st.title("Webcam Live Feed")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        _, frame = camera.read()
        frame = np.array(frame)
        #print(type(frame))
        frame = main(frame)
        FRAME_WINDOW.image(frame)
        
    else:
        st.write('Stopped')
        cam.release()

        st.stop()