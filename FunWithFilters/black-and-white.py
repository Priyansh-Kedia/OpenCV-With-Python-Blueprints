"""
Two techniques used to achieve this are dodging and burning. Dodging lightens an image whereas burning darkens it.
Areas not supposed to undergo change are protected with a mask
Common procedure to achieve pencil sketch is:
1) Convert the image to grayscale
2) Invert the grayscale image to the negative
3) Apply Gaussian blur to the negative
4) Blend the images from step 1 and 3 to get the final image
"""
import cv2 as cv
import numpy as np
from conversion_fns import *


image = cv.imread('download.jpeg')

# Convert to grayscale to convert to 2 dimensions
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("original",image)


img_blend = render(image)
cv.imshow("render blend", img_blend)
cv.waitKey(0)
cv.destroyAllWindows()