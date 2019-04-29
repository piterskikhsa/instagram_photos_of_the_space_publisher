import os
import requests


def download_image(image_link: str, image_name: str):
    response = requests.get(image_link)
    image_name = f'{image_name}{os.path.splitext(image_link)[-1]}'
    if response.ok:
        with open(image_name, 'wb') as out_file:
            out_file.write(response.content)
    else:
        response.raise_for_status()


def get_output_folder(output_folder_path: str):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    return output_folder_path
