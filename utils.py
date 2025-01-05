import os
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def write_text_to_file(file_path, text):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def get_receipts(folder_path):
    images = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path)]
    return images


def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(image_path)
    return text

def extract_all_receipts(folder_path="./data/receipts", output_folder="./data/texts"):
    images = get_receipts(folder_path)
    for image_path in images:
        # img = Image.open(image_path)
        # plt.imshow(img)
        # plt.axis('off')
        # plt.show()
        text = extract_text_from_image(image_path)
        image_file_name_with_extension = os.path.basename(image_path)
        text_file_name = os.path.splitext(image_file_name_with_extension)[0] + ".txt"
        text_path = os.path.join(output_folder, text_file_name)
        write_text_to_file(text_path, text)


#extract_all_receipts("./data/receipts/restaurants", "./data/texts/restaurants")
