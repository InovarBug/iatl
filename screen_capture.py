
import pyautogui

def capture_screen(region=None):
    '''
    Captura a tela ou uma região específica.
    :param region: Tupla (left, top, width, height) para capturar uma região específica.
    :return: Objeto de imagem PIL
    '''
    if region:
        return pyautogui.screenshot(region=region)
    else:
        return pyautogui.screenshot()

def save_screenshot(image, filename):
    '''
    Salva a captura de tela em um arquivo.
    :param image: Objeto de imagem PIL
    :param filename: Nome do arquivo para salvar a imagem
    '''
    image.save(filename)

if __name__ == "__main__":
    # Teste da função
    img = capture_screen()
    save_screenshot(img, "test_screenshot.png")
    print("Captura de tela salva como test_screenshot.png")

