import glob
import os
import time
from io import open

from instabot import Bot
from dotenv import load_dotenv

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
    folder_path = folder_path[:-1] if folder_path[-1] == '/' else folder_path
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


def main():
    # TODO должен быть алгоритм без лишних подробностей
    # Создать дир
    # Скачать картинки
    # Выложить изображения в Инст

    posted_pic_file = 'posted_pics.txt'
    image_dir_path = './images'
    timeout = 10

    if not os.path.exists(image_dir_path):
        os.makedirs(image_dir_path)

    posted_pic_list = get_posted_pic(posted_pic_file)
    bot = create_bot(os.getenv('LOGIN_INST'), os.getenv('PASSWORD_INST'), os.getenv('PROXY_INST'))
    pictures = get_sorted_pictures(image_dir_path)

    for pic in pictures:
        if pic in posted_pic_list:
            continue
        print('upload: ', pic)
        bot.upload_photo(pic, caption='Космос: {}'.format(pic.split('.')[0]))
        if bot.api.last_response.status_code != 200:
            print(bot.api.last_response)
        if pic not in posted_pic_list:
            posted_pic_list.append(pic)
            write_posted_pic_in_file(pic, posted_pic_file)

        time.sleep(timeout)

    del_converted_image(image_dir_path)


if __name__ == '__main__':
    main()

