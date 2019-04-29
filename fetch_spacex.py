import requests

from helpers import download_image


def fetch_spacex_last_launch():
    last_launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(last_launch_url)
    # TODO errors 404 or 403 response.ok
    launch_json = response.json()
    return launch_json['links']['flickr_images']


def main():
    last_images = fetch_spacex_last_launch()
    for image_number, image_url in enumerate(last_images, 1):
        download_image(image_url, f'images/spacex{image_number}')


if __name__ == '__main__':
    main()
