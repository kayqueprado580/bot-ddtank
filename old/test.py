import pyautogui
import numpy as np
from PIL import Image, ImageDraw
import pytesseract
import time
import cv2
import logging
import re


# Configurando o caminho para o executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

logging.basicConfig(filename="log/error_log.txt", level=logging.ERROR)

ANGLES_IMAGES_PATH = [
    {"key": "-5", "path": "img/ant/ang/ang_-5.png"},
    {"key": "6", "path": "img/ant/ang/ang_6.png"},
    {"key": "10", "path": "img/ant/ang/ang_10.png"},
    {"key": "11", "path": "img/ant/ang/ang_11.png"},
    {"key": "12", "path": "img/ant/ang/ang_12.png"},
    {"key": "13", "path": "img/ant/ang/ang_13.png"},
    {"key": "14", "path": "img/ant/ang/ang_14.png"},
    {"key": "15", "path": "img/ant/ang/ang_15.png"},
    {"key": "16", "path": "img/ant/ang/ang_16.png"},
    {"key": "17", "path": "img/ant/ang/ang_17.png"},
    {"key": "19", "path": "img/ant/ang/ang_19.png"},
    {"key": "30", "path": "img/ant/ang/ang_30.png"},
    {"key": "41", "path": "img/ant/ang/ang_41.png"},
    {"key": "46", "path": "img/ant/ang/ang_46.png"},
    {"key": "51", "path": "img/ant/ang/ang_51.png"},
    {"key": "-5", "path": "img/ant/ang/-5.png"},
    {"key": "6", "path": "img/ant/ang/6.png"},
    {"key": "10", "path": "img/ant/ang/10.png"},
    {"key": "10", "path": "img/ant/ang/10_1.png"},
    {"key": "17", "path": "img/ant/ang/17.png"},
    {"key": "41", "path": "img/ant/ang/41.png"},
    {"key": "46", "path": "img/ant/ang/46.png"},
    {"key": "10", "path": "img/ant/ang/ang_10_1.png"},
]


def find_image(image_path, confidence=0.9):
    result = {"found": False, "position_x": 0, "position_y": 0}
    try:
        template = cv2.imread(image_path)
        position = pyautogui.locateOnScreen(template, confidence=confidence)

        if position is not None:
            x, y, width, height = position
            result["found"] = True
            result["x"] = x
            result["y"] = y
            result["width"] = width
            result["height"] = height

    except Exception as e:
        error_message = f"An error occurred: {e}"
        logging.error(error_message)
        with open("log/log.txt", "a") as log_file:
            log_file.write(error_message + "\n")

    return result

def extrair_texto_imagem(caminho_imagem, salvar_imagem=True):
    imagem = cv2.imread(caminho_imagem)
    # Converta para escala de cinza
    screenshot_gray = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2GRAY)

    # Aplique binarização
    _, screenshot_binary = cv2.threshold(screenshot_gray, 128, 255, cv2.THRESH_BINARY)

    # Salvar a imagem temporária
    if salvar_imagem:
        imagem_com_retangulo = Image.fromarray(screenshot_binary)
        imagem_com_retangulo.save("temp_screenshot.png")

    # Configuração personalizada do Tesseract OCR
    custom_config = r"--oem 3 --psm 6 outputbase"

    # Usar o Tesseract OCR para extrair o texto com configuração personalizada
    texto_extraido = pytesseract.image_to_string(
        Image.fromarray(screenshot_binary), lang="por", config=custom_config
    )

    return texto_extraido
  
def extrair_texto_regiao(regiao):
    salvar_imagem = True

    x, y, largura, altura = map(int, regiao)

    # Tirar um screenshot da região especificada
    screenshot = pyautogui.screenshot(region=(x, y, largura, altura))

    # Converta para escala de cinza
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Aplique um filtro ou limiarização adaptativa, se necessário
    # screenshot_gray = cv2.adaptiveThreshold(screenshot_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Aplique binarização
    _, screenshot_binary = cv2.threshold(screenshot_gray, 128, 255, cv2.THRESH_BINARY)

    # Salvar a imagem temporária
    temp_path = "temp_screenshot.png"
    cv2.imwrite(temp_path, screenshot_binary)

    # Salvar a imagem com o retângulo
    if salvar_imagem:
        imagem_com_retangulo = Image.fromarray(screenshot_binary)
        imagem_com_retangulo.save(f"print/teste_{regiao}.png")
        # imagem_com_retangulo.save("teste.png")

    # Configuração personalizada do Tesseract OCR
    custom_config = r"--oem 3 --psm 6 outputbase"

    # Usar o Tesseract OCR para extrair o texto com configuração personalizada
    texto_extraido = pytesseract.image_to_string(
        Image.open(temp_path), lang="por", config=custom_config
    )

    # Excluir a imagem temporária
    screenshot.close()

    return texto_extraido


def filtrar_numeros(texto):
    # Usa regex para encontrar todos os números na string
    # numeros = re.findall(r'\d+', texto)
    
    numeros = re.sub(r'[^0-9]', '', texto)

    # Junta os números encontrados em uma string
    numeros_str = ''.join(numeros)

    return numeros_str


# regioes = [
#     (420, 610, 210, 220),
#     (920, 575, 100, 90),
#     (0, 950, 105, 95),
#     (930, 600, 80, 60),
#     (935, 600, 60, 45),
# ]

# for regiao in regioes:
#     if regiao is None:
#         break
#     texto_encontrado = extrair_texto(regiao)
#     print(f"região: {regiao} - texto: {texto_encontrado}")

# print("==================================================================================")
# print("==================================================================================")
# print("==================================================================================")
# print("")
# print("")
while True:
    for angle in ANGLES_IMAGES_PATH:
        key = angle["key"]
        result = find_image(angle["path"])

        if result["found"]:
            x = result["x"] - 1
            y = result["y"] - 1
            width = result["width"] + 1
            height = result["height"] + 1
            print(f"angle: '{key}' x: {x} y: {y} width: {width} height: {height}")
            regiao = (x, y, width, height)
            texto_encontrado = extrair_texto_regiao(regiao)
            print(f"região: {regiao} - texto: {texto_encontrado}")
            
            texto_encontrado_imagem = extrair_texto_imagem(angle["path"])
            print(f"texto_imagem: {texto_encontrado_imagem}")
            
            numeros_imagem = filtrar_numeros(texto_encontrado_imagem)
            print("Números filtrados IMAGEM:", numeros_imagem)
            
            numeros = filtrar_numeros(texto_encontrado)
            print("Números filtrados:", numeros)

# check = find_image("../img/ant/ants_check.png")
# if check["found"]:
#     ENABLE_START = True


# def capturar_regiao():
#     print("Passe o mouse sobre o canto superior esquerdo da região e aguarde 5 segundos.")
#     time.sleep(5)
#     x1, y1 = pyautogui.position()
#     print(f"Coordenadas do canto superior esquerdo: ({x1}, {y1})")

#     print("Agora, passe o mouse sobre o canto inferior direito da região e aguarde 5 segundos.")
#     time.sleep(5)
#     x2, y2 = pyautogui.position()
#     print(f"Coordenadas do canto inferior direito: ({x2}, {y2})")

#     return (x1, y1, x2 - x1, y2 - y1)

# # Exemplo de uso
# regiao = capturar_regiao()
# print("Coordenadas da região:", regiao)
