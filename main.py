from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from flask import g


app = Flask(__name__)


# расположение файла БД SQLite 3
DATABASE = '/Users/802004/src/myproject/myproject.db'


def get_db():
    """ Возвращает объект соединения с БД"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Закрывает соединение с с БД"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    """
    функция для запроса к БД
    """
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def main_page():
    main_page = 'My vocabulary'
    return render_template('main_page.html', main_page=main_page)


@app.route("/word_list/")
def word_list():
    word_1 = 'to mash'
    description_1 = 'to go somewhere very fast, being in a hurry'
    translation_1 = 'врываться'
    word_2 = 'to dash'
    description_2 = 'to go somewhere very fast, being in a hurry'
    translation_2 = 'врываться'
    word_list = [
        [word_1, description_1, translation_1],
        [word_2, description_2, translation_2],
        [word_2, description_2, translation_2],
        [word_2, description_2, translation_2]
    ]
    search = request.args.get('search')

    if search:
        list_req = []
        for i in word_list:
            if search in i[0]:
                list_req.append(i)
        return render_template('word_list.html', word_list=list_req, count=len(list_req), search=search)
    return render_template('word_list.html', word_list=word_list)


@app.route("/add/")
def add():
    return 'Здесь будет форма добавления слов'


@app.route('/db/')
def index():
    cur = get_db().cursor()
    return 'соединение с базой. Тест'
