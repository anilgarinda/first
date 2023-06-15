import streamlit as st
st.title('My Web App')
st.header('Header')
st.subheader('Subheader')
st.write('Hello, World!')
if st.button('Click me'):
    st.write('Button clicked!')
if st.checkbox('Checkbox'):
    st.write('Checkbox checked!')
option = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])
st.write('You selected:', option)
value = st.slider('Slide me', 0, 10)
st.write('You selected:', value)
file = st.file_uploader('Upload file', type=['csv', 'txt'])
if file:
    st.write(file.read())
import streamlit as st
from pytube import YouTube


# Set page title
st.title("YouTube Video Downloader")

# Get YouTube video URL from user input
video_url = st.text_input("Enter YouTube Video URL")

if st.button("Download"):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution video
        video = yt.streams.get_highest_resolution()

        # Set the output path for the downloaded video
        output_path = "./video.mp4"  # You can change the output path here

        # Download the video
        video.download(output_path)

        st.success("Video downloaded successfully!")
        st.markdown(f"Downloaded video: [video.mp4](./video.mp4)")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


