from flask import Flask,render_template,jsonify
from modelo import *

app = Flask(__name__)

from views import *



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

