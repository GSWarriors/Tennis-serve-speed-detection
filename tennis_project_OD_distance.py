from pytube import YouTube
import cv2
import os
from inference_sdk import InferenceHTTPClient




def main():

    #get video of tennis play
    """url = "https://www.youtube.com/watch?v=s3o3fL_59Gk&ab_channel=CourtsideTennisHighlights"

    #download video
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(filename='video.mp4')"""

    video_path = 'compressed_video.mp4'

    #directory where the frames
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="fxpfPbxMltx9lhX4HSBM"
    )

    cap = cv2.VideoCapture(video_path)
    #add a check to make sure the video is opened correctly
    if not cap.isOpened():
        print("error: could not open video")
        return


    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        #save frame every nth frame (e.g., every 30 frames)
        if frame_count % 30 == 0:
            frame_path = f'frame_{frame_count}.jpg'
            cv2.imwrite(frame_path, frame)

            #send each frame to model, and run model inference on frame
            result = CLIENT.infer(frame_path, model_id="tennis-vhrs9/9")
            print(f"Result for frame {frame_count}: {result}")

            #parse results i have for bounding box information
            if result and "predictions" in result:
                for prediction in result["predictions"]:

                    print("our prediction: " + str(prediction))
                    print()
                    if prediction["class"] == 'net' and prediction["confidence"] >= 0.5:

                    #assume we have format 'x', 'y', 'width', 'height' for bounding box
                        x = int(prediction["x"] - prediction["width"] / 2)
                        y = int(prediction["y"] - prediction["height"] / 2)
                        width = int(prediction["width"])
                        height = int(prediction["height"])

                        #draw bounding box on the frame
                        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
                        cv2.putText(frame, "Tennis Net", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


            cv2.imshow('Tennis Detection', frame)

        #wait briefly for q key press in order to exit loop,
        #since that will close whatever display we have
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

#now just calculate euclidean distance between player and net


main()
