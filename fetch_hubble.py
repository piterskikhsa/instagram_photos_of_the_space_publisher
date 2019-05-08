import requests

from helpers import download_image, get_output_folder


def get_image_ids_from_collection(url):
    response = requests.get(url)
    response.raise_for_status()
    images_data = response.json()
    image_ids = (image.get('id') for image in images_data)
    return image_ids


def get_image_url(image_id, url):
    url = f'{url}/{image_id}'
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()
    return launch['image_files'][-1]['file_url']


def fetch_hubble_images(collection, output_folder):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection)
    image_url = 'http://hubblesite.org/api/v3/image'
    image_ids = get_image_ids_from_collection(url)
    if not image_ids:
        return None
    for image_id in image_ids:
        image = get_image_url(image_id, image_url)
        download_image(image, f'{output_folder}/{image_id}')


def main():
    collection = 'spacecraft'
    output_folder = get_output_folder('images')
    fetch_hubble_images(collection, output_folder)


if __name__ == '__main__':
    main()
