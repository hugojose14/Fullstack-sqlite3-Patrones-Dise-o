from flask import Flask,render_template,jsonify
import sqlite3
from index import app
from modelo import *


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users/list')
def get_users():
   db = singletonDB()
   with db.database as con:
     con.row_factory = sqlite3.Row     
     cur = con.cursor()
     cur.execute("select * from users")     
     rows = cur.fetchall()
     return render_template("users.html",rows = rows)

@app.route('/api/v1/users')
def lista2():
    db = sqlite3.connect('./database/users.db', check_same_thread=False)
    with db as con:
      cur = con.cursor()
      cur.execute("select * from users")
      valores = cur.fetchall()
      return jsonify(valores)


@app.errorhandler(404)
def page_not_found(error):
  return render_template("error.html",error="Página no encontrada..."), 404