"""
Brandon Dunbar
Compare two images
Source:
https://rosettacode.org/wiki/Percentage_difference_between_images#Python
"""

from PIL import Image


def compare(image1, image2):
    """
    Determines percent difference between two images.
    
    Input:
	image1, image2 - First and second images to compare

    Output:
	percent - Percent difference between the two
    """

    imageObj1 = Image.open(image1)
    imageObj2 = Image.open(image2)

    pairs = zip(imageObj1.getdata(), imageObj2.getdata())
    if len(imageObj1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = imageObj1.size[0] * imageObj2.size[1] * 3
    difference =  (dif / 255.0 * 100) / ncomponents
    return difference

