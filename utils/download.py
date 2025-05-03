import requests
from PIL import Image
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content)).convert("RGB")
        
    return img