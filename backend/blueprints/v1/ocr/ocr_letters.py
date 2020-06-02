import pytesseract
from PIL import Image

from common.utils import chrs


def img_ocr(img):
    text = pytesseract.image_to_string(Image.open(img), lang='chi_sim')
    text = text.translate(chrs)
    text.replace(" ", "")
    text = text.split()
    return text
