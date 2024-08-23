import cv2
from pytesseract import pytesseract

# Definir o caminho para o executável do Tesseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Altere o caminho conforme necessário

# Carregar a imagem
image = cv2.imread('Image20240823144259.jpg')

# Ler o texto na imagem
text = pytesseract.image_to_string(image)

# Printar o texto
print(text)
