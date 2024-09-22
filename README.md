# Tennis-serve-speed-detection

git clone https://github.com/ultralytics/yolov5
cd yolov5
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Install PyTorch: If you haven't already installed PyTorch, you can do so by selecting the correct version from here based on your system and CUDA support.

2. Download YouTube Video
Since YOLOv5 doesn't directly support processing YouTube videos, you'll first need to download the video locally using pytube or youtube-dl.

Install pytube:
bash
Copy code
pip install pytube
Download the YouTube video:
Here’s an example of how to download a YouTube video using pytube:

from pytube import YouTube

# Specify the YouTube video URL
url = "https://www.youtube.com/watch?v=your_video_url"

# Download the video
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(filename='video.mp4')
Alternatively, you can use youtube-dl:

pip install youtube-dl
Download the video:


youtube-dl -o video.mp4 "https://www.youtube.com/watch?v=your_video_url"
This will download the YouTube video locally and save it as video.mp4.

3. Run YOLOv5 on the Downloaded Video
Once you've downloaded the video, you can run YOLOv5 on it. Here’s how:

Command to run YOLOv5:
bash
Copy code
python detect.py --weights yolov5s.pt --source video.mp4 --conf 0.5 --view-img
--weights yolov5s.pt: Specifies the pre-trained model weights (YOLOv5 small version).
--source video.mp4: The path to the downloaded YouTube video file.
--conf 0.5: Confidence threshold (can adjust based on performance).
--view-img: Display the output video with detection.
This will process the video, detect objects (such as tennis balls, since they're categorized as "sports balls" in the COCO dataset), and display the results in real-time.

Use ffmpeg -i video.mp4.webm video.mp4 (to convert the video from webm into mp4).


4. Save the Output
If you want to save the detection output to a new video file, you can add the --save-txt and --save-conf options to save the detection labels and confidence values.

python detect.py --weights yolov5s.pt --source video.mp4 --conf 0.5 --save-txt --save-conf --save-img
