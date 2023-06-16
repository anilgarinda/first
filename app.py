import os
import streamlit as st
from pytube import YouTube
from pathlib import Path

def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=output_path)
        return True, f"Video downloaded successfully! Saved at: {output_path}"
    except Exception as e:
        return False, f"Error occurred: {str(e)}"

def main():
    st.title("YouTube Video Downloader")
    video_url = st.text_input("Enter the YouTube video URL:")
    output_path = None

    if st.button("Choose Output Path"):
        output_path = st.file_uploader("Select output path", type="directory", key="output_path")

    download_button = st.button("Download Video")

    if download_button:
        if video_url and output_path:
            output_path = Path(output_path.name).resolve()
            success, message = download_video(video_url, str(output_path))
            st.write(message)
        else:
            st.write("Please provide both the video URL and select the output path.")

if __name__ == "__main__":
    main()
