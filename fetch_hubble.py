import requests

from helpers import download_image


def get_image_ids_from_collection(collection_name: str):
    payload = {'page': 'all', 'collection_name': collection_name}
    url = 'http://hubblesite.org/api/v3/images'
    response = requests.get(url, params=payload)
    if response.ok:
        images_data = response.json()
        image_ids = (image.get('id') for image in images_data)
        return image_ids
    else:
        # TODO raise error
        print('error')


def fetch_habr_images(image_id: int):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    # TODO errors 404 or 403 response.ok
    response = requests.get(url)
    launch = response.json()
    return launch['image_files'][-1]['file_url']


def main():
    collection = 'spacecraft'
    image_ids = get_image_ids_from_collection(collection)
    if not image_ids:
        return None
    for image_id in image_ids:
        image = fetch_habr_images(image_id)
        download_image(image, f'images/{image_id}')


if __name__ == '__main__':
    main()
