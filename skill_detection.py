
import cv2
import numpy as np

def detect_skill_active(image, skill_region, active_color, threshold=0.8):
    '''
    Detecta se uma habilidade está ativa com base na cor.
    :param image: Imagem completa da tela
    :param skill_region: Tupla (x, y, width, height) da região da habilidade
    :param active_color: Tupla (B, G, R) da cor quando a habilidade está ativa
    :param threshold: Limiar de similaridade (0-1)
    :return: Boolean indicando se a habilidade está ativa
    '''
    x, y, w, h = skill_region
    skill_image = image[y:y+h, x:x+w]
    
    # Cria uma máscara da cor ativa
    lower = np.array([max(0, c-20) for c in active_color])
    upper = np.array([min(255, c+20) for c in active_color])
    mask = cv2.inRange(skill_image, lower, upper)
    
    # Calcula a porcentagem de pixels ativos
    active_pixels = np.sum(mask == 255)
    total_pixels = mask.size
    active_ratio = active_pixels / total_pixels
    
    return active_ratio > threshold

if __name__ == "__main__":
    # Teste da função
    import pyautogui
    
    # Captura a tela
    screenshot = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Define uma região de teste e uma cor ativa
    test_region = (100, 100, 50, 50)  # Exemplo: x=100, y=100, width=50, height=50
    active_color = (0, 255, 0)  # Verde brilhante
    
    # Testa a detecção
    is_active = detect_skill_active(image, test_region, active_color)
    print(f"Habilidade ativa: {is_active}")

