import cv2 as cv

def dodgeV2(image, mask):
    """
    We blend the gray scale image  
    """
    return cv.divide(image, 255-mask, scale=256)

def burnV2(image, mask):
    return 255 - cv.divide(255-image, 255 - mask, scale=256)

def render(image_rgb):
    # Convert to grayscale to convert to 2 dimensions
    image_gray = cv.cvtColor(image_rgb, cv.COLOR_BGR2GRAY)

    # Blurring the image to remove the extra noise
    image_blur = cv.GaussianBlur(image_gray, (21,21),0,0)

    # Blending the image
    image_blend = cv.divide(image_gray, image_blur, scale=256)
    return cv.cvtColor(image_blend, cv.COLOR_GRAY2BGR)