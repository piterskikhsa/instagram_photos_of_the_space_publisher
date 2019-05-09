import os
import requests
import glob


def download_image(image_link, image_name):
    response = requests.get(image_link)
    image_name = f'{image_name}{os.path.splitext(image_link)[-1]}'
    response.raise_for_status()
    with open(image_name, 'wb') as out_file:
        out_file.write(response.content)


def get_output_folder(output_folder_path):
    os.makedirs(output_folder_path, exist_ok=True)
    return output_folder_path


def get_sorted_pictures(folder_path, exts=('jpg', 'tif')):
    pics = []
    folder_path = folder_path.strip('/')
    for ext in exts:
        pics.extend(glob.glob('{}/*.{}'.format(folder_path, ext)))
    return sorted(pics)


def get_json_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def can_remove_file(file_name):
    file_name = file_name.split('.')
    return file_name[-1] == 'REMOVE_ME' or file_name[-2] == 'CONVERTED'


def clear_converted_image(dir_path):
    files = glob.glob('{}/*'.format(dir_path))
    for file in files:
        if can_remove_file(file):
            os.remove(file)
