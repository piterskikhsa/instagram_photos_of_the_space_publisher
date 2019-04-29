import os
import requests


def download_image(image_link: str, image_name: str):
    response = requests.get(image_link)
    image_name = f'{image_name}{os.path.splitext(image_link)}'
    if response.ok:
        with open(image_name, 'wb') as out_file:
            out_file.write(response.content)
