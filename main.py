"""
Basic security functionality for raspi w camera.
Brandon Dunbar
"""

# import scripts
import rpi_camera, compare_two_images
from datetime import datetime

THRESHOLD = 5  # Percent of allowable difference between each image check


def main():

    picToOverwrite = "picA"

    # Take initial picture
    rpi_camera.capPicture(imageName=picToOverwrite)

    # Is picA the string to overwrite
    overwritePicA = False

    # Enter loop
    while True:

        # Alternate between image paths
        if overwritePicA:
            picToOverwrite = "picA"
        else:
            picToOverwrite = "picB"

    	# Take picture
        rpi_camera.capPicture(imageName=picToOverwrite)

        # Compare the two pictures
        difference = compare_two_images.compare("picA.jpg", "picB.jpg")

        # If difference above threshold
        if difference > THRESHOLD:
            # Timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

            # Record for x seconds
            rpi_camera.capVideo(vidName=timestamp)


if __name__ == "__main__":
    main()
