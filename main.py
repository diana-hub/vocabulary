from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def main_page():
    main_page = 'My vocabulary'
    return render_template('main_page.html', main_page=main_page)


@app.route("/word_list/")
def word_list():
    word_1 = 'to dash'
    description_1 = 'to go somewhere very fast, being in a hurry'
    translation_1 = 'врываться'
    word_2 = 'to dash'
    description_2 = 'to go somewhere very fast, being in a hurry'
    translation_2 = 'врываться'
    word_list = [[word_1, description_1, translation_1], [word_2, description_2, translation_2], [word_2, description_2, translation_2],[word_2, description_2, translation_2]]
    return render_template('word_list.html', word_list=word_list)


@app.route("/add/")
def add():
    return 'Здесь будет форма добавления слов'



