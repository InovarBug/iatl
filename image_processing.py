
import cv2
import numpy as np

def convert_to_grayscale(image):
    '''
    Converte a imagem para escala de cinza.
    :param image: Imagem no formato numpy array (BGR)
    :return: Imagem em escala de cinza
    '''
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image(image, scale_percent):
    '''
    Redimensiona a imagem.
    :param image: Imagem no formato numpy array
    :param scale_percent: Porcentagem de escala (ex: 50 para metade do tamanho)
    :return: Imagem redimensionada
    '''
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

def apply_threshold(image, threshold_value):
    '''
    Aplica limiarização na imagem.
    :param image: Imagem em escala de cinza
    :param threshold_value: Valor de limiar (0-255)
    :return: Imagem binarizada
    '''
    _, binary = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary

if __name__ == "__main__":
    # Teste das funções
    import pyautogui
    
    # Captura a tela
    screenshot = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Processa a imagem
    gray = convert_to_grayscale(image)
    resized = resize_image(gray, 50)
    binary = apply_threshold(resized, 128)
    
    # Salva os resultados
    cv2.imwrite("gray.png", gray)
    cv2.imwrite("resized.png", resized)
    cv2.imwrite("binary.png", binary)
    
    print("Imagens processadas e salvas.")

