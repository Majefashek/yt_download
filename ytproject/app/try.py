# views.py
from pytube import YouTube


def download_video(youtube_url, output_path='./'):
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        print("Video downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

video_url = "https://youtu.be/3QCioZm58Gs?si=NPGNrwT_Kauw27p0"
download_video(video_url)
