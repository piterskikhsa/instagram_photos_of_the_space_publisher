# Скрипт для публикации фотографий космоса в инстаграм
Скрипт автоматизирует сбор фотографий космоса (spacex, hubble) и публикацию в инстаграме.

### Как установить
Для использования скрипта необходимо:
1. необходим аккаунт в инстаграм
2. создать файл '.env' и записать там ваши данные:
```
LOGIN_INST=ваш логин
PASSWORD_INST=ваш пароль
```

Python3 должен быть уже установлен. 
Затем используйте pipenv или pip для установки зависимостей:

```
pipenv install
```

Рекомендуется использовать virtualenv для изоляции проекта.

### Цель проекта
#### fetch_spacex
Скачиваем все фотографии с последнего запуска SpaceX и сохраняем в папку.

#### fetch_hubble
Скачиваем фотографий из коллекций Hubble и сохраняем в папку.

#### publish_instagram
Публикует фотографии.

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).