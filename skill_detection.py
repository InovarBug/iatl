import cv2
import numpy as np

def detect_skill_active(image, skill_region, active_color, threshold=0.8):
    x, y, w, h = skill_region
    skill_image = image[y:y+h, x:x+w]
    
    lower = np.array([max(0, c-20) for c in active_color])
    upper = np.array([min(255, c+20) for c in active_color])
    mask = cv2.inRange(skill_image, lower, upper)
    
    active_pixels = np.sum(mask == 255)
    total_pixels = mask.size
    active_ratio = active_pixels / total_pixels
    
    return active_ratio > threshold
