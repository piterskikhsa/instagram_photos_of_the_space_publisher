import os
import requests


if not os.path.exists('images'):
    os.makedirs('images')


def download_image(image_link: str, image_name: str):
    response = requests.get(image_link)
    image_name = f'{image_name}.{get_expansion_from_url(image_link)}'
    if response.ok:
        with open(image_name, 'wb') as out_file:
            out_file.write(response.content)


def get_expansion_from_url(image_url: str):
    return image_url.split('.')[-1]
