from fastapi import HTTPException
from pytube import YouTube

url = "https://www.youtube.com/watch?v=ZkYOvViSx3E"
try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        # Download the video to the current working directory
        stream.download()

        print("message", "Video downloaded successfully!")
except KeyError:
    raise HTTPException(status_code=400, detail="Error: Video is not available or cannot be downloaded")
except ValueError:
    raise HTTPException(status_code=400, detail="Error: Invalid URL")
except Exception as e:
    raise HTTPException(status_code=400, detail="Error downloading video: " + str(e))