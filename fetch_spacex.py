import requests

from helpers import download_image, get_output_folder


def get_last_launch_images(url: str):
    response = requests.get(url)
    if response.ok:
        launch_json = response.json()
        return launch_json['links']['flickr_images']
    else:
        response.raise_for_status()


def fetch_spacex_last_launch(output_folder: str):
    last_launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    last_images = get_last_launch_images(last_launch_url)
    for image_number, image_url in enumerate(last_images, 1):
        download_image(image_url, f'{output_folder}/spacex{image_number}')


def main():
    folder = get_output_folder('images')
    fetch_spacex_last_launch(folder)


if __name__ == '__main__':
    main()
