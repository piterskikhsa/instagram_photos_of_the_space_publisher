import os
import requests


def download_image(image_link, image_name):
    response = requests.get(image_link)
    image_name = f'{image_name}{os.path.splitext(image_link)[-1]}'
    response.raise_for_status()
    with open(image_name, 'wb') as out_file:
        out_file.write(response.content)


def get_output_folder(output_folder_path):
    os.makedirs(output_folder_path)
    return output_folder_path


def get_sorted_pictures(folder_path, exts=('jpg', 'tif')):
    pics = []
    folder_path = folder_path.strip('/')
    for ext in exts:
        pics.extend(glob.glob('{}/*.{}'.format(folder_path, ext)))
    return sorted(pics)