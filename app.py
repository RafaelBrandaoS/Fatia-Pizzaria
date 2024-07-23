from flask import Flask, render_template, url_for
from python.produtos import listaPizzas

app = Flask(__name__)

@app.route('/')
def home():
    " página principal "
    pizzas = listaPizzas()
    return render_template('index.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)