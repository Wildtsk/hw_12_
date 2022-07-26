import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from hw_12_.functions import add_post
from hw_12_.loader.utils import save_picture

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')


@loader_blueprint.route('/post')
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture') #None не пишем - по дефолту он.
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или текста'

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Загруженный файл не является картинкой')
        return 'Не тот формат файла, нужен jpeg или png'
    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error('файл не найден')
        return 'Возможно здесь ошибка, файл не найден'
    except JSONDecodeError:
        return 'Что то с файлом не так'
    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
