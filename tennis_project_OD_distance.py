from pytube import YouTube

def main():

    #get video of tennis play
    url = "https://www.youtube.com/watch?v=s3o3fL_59Gk&ab_channel=CourtsideTennisHighlights"

    #download video
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(filename='video.mp4')

        


main()
