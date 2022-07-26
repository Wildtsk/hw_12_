import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from hw_12_.functions import get_posts_by_word

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

@main_blueprint.route("/")
def mane_page():
    return render_template("index.html")


@main_blueprint.route("/search/")
def search_page():
    search_query = request.args.get("s", "")
    logging.info('Поиск выполняется')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error('файл не найден')
        return 'Что то пошло не так.. Возможно файла не существует?'
    except JSONDecodeError:
        return 'Что то с файлом не так'
    return render_template("post_list.html", query=search_query, posts=posts)