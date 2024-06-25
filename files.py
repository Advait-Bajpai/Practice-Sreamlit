import pandas as pd
import streamlit as st
st.subheader('Loading the CSV file')
df = st.file_uploader("Upload the CSV file : ", type = ['csv', 'xlsx'])
df = pd.read_csv('iris.csv')
if df is not None:
    st.table(df.head())
st.subheader('Dealing with images directly')
st.image('image.jpg')
st.subheader('Dealing with images while uploading')
img_file = st.file_uploader("Upload the Image file : ", type = ['png', 'jpg'])
if img_file is not None:
    st.image(img_file)
st.subheader('Working with Videos')
vid_file = st.file_uploader("Upload the Video file : ", type = ['mp4', 'mkv'])
if vid_file is not None:
    st.video(vid_file, start_time = 0)
st.subheader('Working with Audio')
aud_file = st.file_uploader("Upload the Video file : ", type = ['mp3', 'wav'])
if aud_file is not None:
    st.audio(aud_file, start_time = 0)
