import glob
import os
import time
from io import open
from instabot import Bot
from dotenv import load_dotenv

from fetch_hubble import fetch_hubble_images
from fetch_spacex import fetch_spacex_last_launch
from helpers import get_output_folder


load_dotenv()


def create_bot(username, password, proxy):
    insta_bot = Bot()
    insta_bot.login(username=username, password=password, proxy=proxy)
    return insta_bot


def get_posted_pic(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file_output:
            posted_pic = file_output.read().splitlines()
    except Exception:
        posted_pic = []
    return posted_pic


def get_sorted_pictures(folder_path, exts=('jpg', 'tif')):
    pics = []
    folder_path = folder_path.strip('/')
    for ext in exts:
        pics.extend(glob.glob('{}/*.{}'.format(folder_path, ext)))
    return sorted(pics)


def write_posted_pic_in_file(posted_pic, file_name):
    with open(file_name, 'a') as file_out:
        file_out.write('{}\n'.format(posted_pic))


def del_converted_image(dir_path):
    files = glob.glob('{}/*'.format(dir_path))
    for file in files:
        file_status = file.split('.')
        if file_status[-1] == 'REMOVE_ME' or file_status[-2] == 'CONVERTED':
            os.remove(file)


def upload_images(inst_bot, pictures, posted_pictures):
    for pic in pictures:
        if pic in posted_pictures:
            continue
        inst_bot.upload_photo(pic, caption='Космос: {}'.format(pic.split('.')[0]))
        if inst_bot.api.last_response.status_code != 200:
            pass
        if pic not in posted_pictures:
            posted_pictures.append(pic)
            write_posted_pic_in_file(pic, posted_pictures)


def main():
    posted_pic_file = 'posted_pics.txt'
    image_dir_path = get_output_folder('images')

    fetch_spacex_last_launch(image_dir_path)
    fetch_hubble_images('news', image_dir_path)

    posted_pic_list = get_posted_pic(posted_pic_file)
    bot = create_bot(os.getenv('LOGIN_INST'), os.getenv('PASSWORD_INST'), os.getenv('PROXY_INST'))
    pictures = get_sorted_pictures(image_dir_path)

    upload_images(bot, pictures, posted_pic_list)

    del_converted_image(image_dir_path)


if __name__ == '__main__':
    main()

