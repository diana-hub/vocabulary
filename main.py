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
    word_list = query_db('select * from vocabulary;')

    search = request.args.get('search')

    if search:
        # TODO: поиск увести в базу
        list_req = []
        for i in word_list:
            if search in i[1]:
                list_req.append(i)
        return render_template('word_list.html', word_list=list_req, count=len(list_req), search=search)
    return render_template('word_list.html', word_list=word_list)


@app.route("/add_words/")
def add_words():
    add_words = "Filling form"
    return render_template('add_words.html', add_words=add_words)


@app.route('/db/')
def index():
    data = query_db('select * from vocabulary;')
    print(data)
    return 'соединение с базой. Тест'
