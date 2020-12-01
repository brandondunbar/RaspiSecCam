"""
Brandon Dunbar
Takes picture or video with python3-picamera
"""

import picamera
from time import sleep
from subprocess import call


def capPicture(imageName="default"):
    """
    Captures a picture.

    Input:
         imageName - The image's file name.

    Output:
	bool - Successful execution
    """

    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(f"{imageName}.jpg")

    return True


def capVideo(vidName="default", time=5, mp4=False):
    """
    Captures a video.
    * Uses sleep function. Would like to fix this. *

    Input:
        vidName - The video's file name.
        time - 5000
        mp4 - Convert to mp4 or leave as h264

    Output:
        bool - Successful execution
    """

    fileName = f"{vidName}.h264"

    with picamera.PiCamera() as camera:
        camera.start_recording(fileName)
        sleep(time)
        camera.stop_recording()

    if mp4:
        convertH264toMp4(fileName)


def convertH264toMp4(fileName, keepOldFile=False):
    """
    Uses ffmpeg to convert file from .h264 to mp4
    
    Input:
         fileName - The name of the file

    Output:
         bool - Successful execution
    """

    command = f"ffmpeg -framerate 24 -i {fileName} -c copy {fileName[:-5]}.mp4"
    call([command], shell=True)

    return True


if __name__ == "__main__":
    capVideo()
