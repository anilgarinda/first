import streamlit as st
from pytube import YouTube


def download_video(video_url):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video_path = video.download()
        message = f"Video downloaded successfully! Saved at: {video_path}"
    except Exception as e:
        message = f"Error occurred: {str(e)}"

    return message


def main():
    st.title("YouTube Video Downloader")

    # Input field
    video_url = st.text_input("Enter the YouTube video URL:")

    # Download button
    if st.button("Download"):
        if video_url:
            message = download_video(video_url)
            st.success(message)
        else:
            st.error("Please provide the video URL.")


if __name__ == "__main__":
    main()
