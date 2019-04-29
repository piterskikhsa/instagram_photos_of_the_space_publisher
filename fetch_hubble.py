import requests

from helpers import download_image


def get_image_ids_from_collection(collection_name: str, url: str):
    payload = {'page': 'all', 'collection_name': collection_name}
    response = requests.get(url, params=payload)
    if response.ok:
        images_data = response.json()
        image_ids = (image.get('id') for image in images_data)
        return image_ids
    else:
        response.raise_for_status()


def fetch_hubble_images(image_id: int, url: str):
    url = f'{url}/{image_id}'
    response = requests.get(url)
    if response.ok:
        launch = response.json()
        return launch['image_files'][-1]['file_url']
    else:
        response.raise_for_status()


def download_images_from_hubble_collection(collection: str, output_folder: str):
    url = 'http://hubblesite.org/api/v3/image'
    image_ids = get_image_ids_from_collection(collection, url)
    if not image_ids:
        return None
    for image_id in image_ids:
        image = fetch_hubble_images(image_id, url)
        download_image(image, f'{output_folder}/{image_id}')


def main():
    collection = 'spacecraft'
    output_folder = 'images'
    download_images_from_hubble_collection(collection, output_folder)


if __name__ == '__main__':
    main()
