from pytube import YouTube

# Function to download audio from YouTube
def download_audio(url, output_path):
    try:
        # Creating a YouTube object
        yt = YouTube(url)

        # Getting the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Downloading the audio
        audio_stream.download(output_path)

        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

# Example usage:
if __name__ == "__main__":
    video_url = "https://youtu.be/nwFBxMqm1X4?si=8MOD23dNHzEbnrlm"  # Replace VIDEO_ID with the actual video ID
    output_path = "D:\project__python\savedaudio"  # Replace with the path where you want to save the audio
    download_audio(video_url, output_path)
