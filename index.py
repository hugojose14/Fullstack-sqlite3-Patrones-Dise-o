from flask import Flask,render_template,jsonify
import sqlite3
from flask import g 
app = Flask(__name__)

DATABASE = '/database/users.db'

def get_db():
    db = getattr(g, '_users', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_users', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users/list')
def get_users():
   con = sqlite3.connect('./database/users.db')
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   rows = cur.fetchall()
   return render_template("users.html",rows = rows)

@app.route('/api/v1/users')
def lista2():

    con = sqlite3.connect('./database/users.db')
    cur = con.cursor()
    cur.execute("select * from users")
    valores = cur.fetchall()
    return jsonify(valores)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

