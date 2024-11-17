
import pyautogui
import time

def press_key(key):
    '''
    Pressiona uma tecla.
    :param key: Tecla a ser pressionada (string)
    '''
    pyautogui.press(key)

def hold_key(key, duration):
    '''
    Mantém uma tecla pressionada por um determinado tempo.
    :param key: Tecla a ser pressionada (string)
    :param duration: Duração em segundos
    '''
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def activate_skill(skill_key):
    '''
    Ativa uma habilidade pressionando a tecla correspondente.
    :param skill_key: Tecla da habilidade (string)
    '''
    press_key(skill_key)
    print(f"Habilidade '{skill_key}' ativada")

if __name__ == "__main__":
    # Teste das funções
    print("Testando automação de teclas...")
    print("Pressionando a tecla 'a'")
    press_key('a')
    time.sleep(1)
    
    print("Mantendo a tecla 'w' pressionada por 2 segundos")
    hold_key('w', 2)
    time.sleep(1)
    
    print("Ativando habilidade '1'")
    activate_skill('1')

