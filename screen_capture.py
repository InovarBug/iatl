import pyautogui

def capture_screen(region=None):
    return pyautogui.screenshot(region=region)
