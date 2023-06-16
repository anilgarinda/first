import os
import platform
import streamlit as st
from pytube import YouTube
from pathlib import Path

def get_default_output_path():
    if platform.system() == "Windows":
        return str(Path.home() / "Downloads")
    elif platform.system() == "Darwin":  # macOS
        return str(Path.home() / "Downloads")
    elif platform.system() == "Linux":
        return str(Path.home() / "Downloads")
    else:
        return None

def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video_file = video.download(output_path=output_path)
        return True, video_file
    except Exception as e:
        return False, str(e)

def main():
    st.title("YouTube Video Downloader")
    video_url = st.text_input("Enter the YouTube video URL:")
    output_path = None

    if st.button("Download Video"):
        if video_url:
            if platform.system() == "Android":
                output_path = str(Path.home() / "Downloads")
            else:
                output_path = get_default_output_path()

            success, video_file = download_video(video_url, output_path)
            if success:
                st.success("Video downloaded successfully!")
                st.markdown(f"Download Link: [Download Video]({video_file})")
            else:
                st.error("Error occurred during download.")
                st.error(video_file)
        else:
            st.warning("Please enter the YouTube video URL.")

if __name__ == "__main__":
    main()
