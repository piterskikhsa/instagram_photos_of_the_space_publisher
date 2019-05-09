from helpers import download_image, get_output_folder, get_json_from_url


def get_image_ids_from_collection(url):
    images_data = get_json_from_url(url)
    image_ids = (image.get('id') for image in images_data)
    return image_ids


def get_image_url(image_id, url):
    url = f'{url}/{image_id}'
    launch = get_json_from_url(url)
    image_files = launch['image_files']
    return image_files[-1]['file_url']


def fetch_hubble_images(collection, output_folder):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection)
    base_image_url = 'http://hubblesite.org/api/v3/image'
    image_ids = get_image_ids_from_collection(url)
    if not image_ids:
        return None
    for image_id in image_ids:
        image_url = get_image_url(image_id, base_image_url)
        download_image(image_url, f'{output_folder}/{image_id}')


def main():
    collection = 'spacecraft'
    output_folder = get_output_folder('images')
    fetch_hubble_images(collection, output_folder)


if __name__ == '__main__':
    main()
