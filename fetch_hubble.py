import json
import requests

from helpers import download_image


def get_image_ids_from_collection(collection_name: str):
    payload = {'page': 'all', 'collection_name': collection_name}
    url = 'http://hubblesite.org/api/v3/images'
    response = requests.get(url, params=payload)
    if response.ok:
        images_data = json.loads(response.content)
        image_ids = (image.get('id') for image in images_data)
        return image_ids
    else:
        print('error')


def fetch_habr_images(image_id: int):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    launch = json.loads(requests.get(url).content)
    return launch['image_files'][-1]['file_url']


def main():
    collection = 'spacecraft'
    image_ids = get_image_ids_from_collection(collection)
    if not image_ids:
        print('none ids')
        return None
    for image_id in image_ids:
        image = fetch_habr_images(image_id)
        download_image(image, f'images/{image_id}')


if __name__ == '__main__':
    main()
