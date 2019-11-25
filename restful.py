# coding=utf-8
from bottle import run, get, get_books, create_bd, database_get_all

emojies = [{'emoji': 'var1'}, {'like': 'var2'}]


@get('/emoji/<emoji>')
def get_all(emoji):
    return {get_books(emoji, create_bd())}


@get('/like/<like>/<id>')
def get_all(like, id):
    return {like, id}


run(reloader=True, debug=True)
