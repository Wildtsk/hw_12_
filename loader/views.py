from flask import Blueprint, render_template, request

from hw_12_.functions import add_post
from hw_12_.loader.utils import save_picture

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')


@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture') #None не пишем - по дефолту он.
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или текста'

    picture_path: str = '/' + save_picture(picture)
    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
