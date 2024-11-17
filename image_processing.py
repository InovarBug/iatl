import cv2
import numpy as np

def convert_to_grayscale(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
