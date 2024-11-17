import pyautogui

def press_key(key):
    pyautogui.press(key)

def activate_skill(skill_key):
    press_key(skill_key)
    print(f"Habilidade '{skill_key}' ativada")
