from flask import Flask

from numeros import decimal_a_binario

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/numeros")
def decimal_to_binario():
    print(decimal_a_binario(4))
    return f'<p>{decimal_a_binario(10)}<p>'