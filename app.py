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
        video.download(output_path=output_path)
        return True, f"Video downloaded successfully! Saved at: {output_path}"
    except Exception as e:
        return False, f"Error occurred: {str(e)}"

def main():
    st.title("YouTube Video Downloader")
    video_url = st.text_input("Enter the YouTube video URL:")
    output_path = None

    if st.button("Download Video"):
        if video_url:
            if platform.system() == "Android":
                output_path = str(Path.home() / "Pictures")
            else:
                output_path = get_default_output_path()

            success, message = download_video(video_url, output_path)
            st.write(message)
        else:
            st.write("Please enter the YouTube video URL.")

if __name__ == "__main__":
    main()
