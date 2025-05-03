import os
import requests
from io import BytesIO
from PIL import Image

def show_image_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    image.save("temp_image.png")
    os.system("chafa temp_image.png")