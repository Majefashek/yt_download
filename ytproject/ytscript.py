import requests
from pytube import YouTube

def download_video(youtube_url, save_path="video.mp4"):
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        video_response = requests.get(stream.url, stream=True)
        
        # Ensure the request was successful
        video_response.raise_for_status()
        
        # Save the binary content of the response to a file
        with open(save_path, 'wb') as video_file:
            for chunk in video_response.iter_content(chunk_size=8192):
                video_file.write(chunk)
        
        print(f"Video downloaded successfully as {save_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    download_video(youtube_url, save_path="downloaded_video.mp4")
