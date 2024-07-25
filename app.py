from flask import Flask, render_template, url_for
from python.produtos import listaPizzas, listaMiniPizza, listaBebidas

app = Flask(__name__)

@app.route('/')
def home():
    " página principal "
    pizzas = listaPizzas()
    return render_template('index.html', pizzas=pizzas)

@app.route('/carrinho')
def carrinho():
    " mostra o carrinho "
    return render_template('carrinho.html')

@app.route('/pizzas')
def pizzas():
    " página das mini pizzas "
    pizzas = listaPizzas()
    return render_template('pizzas.html', pizzas=pizzas)

@app.route('/miniPizzas')
def miniPizzas():
    " página das mini pizzas "
    minipizza = listaMiniPizza()
    return render_template('miniPizzas.html', minipizza=minipizza)


@app.route('/brotinho')
def brotinho():
    " página das mini pizzas "
    return render_template('brotinho.html')


@app.route('/bebidas')
def bebidas():
    " página das mini pizzas "
    bebidas = listaBebidas()
    return render_template('bebidas.html', bebidas=bebidas)

if __name__ == '__main__':
    app.run(debug=True)