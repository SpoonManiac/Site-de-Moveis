from flask import Flask, render_template, request, redirect

class Moveis:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categaria = categoria

movel = Moveis("Mesa de jantar", "Mesas")
movel2 = Moveis("Poltrona Balanço", "Acentos")
movel3 = Moveis("Sofá Aqua", "Sofás")
lista = [movel, movel2, movel3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', nomeLoja='Stock Sir', cat=lista)


@app.route('/admin')
def adicionar():
    return render_template('adicionar.html', titulo='Admin Stock-Sir')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    moveis = Moveis(nome, categoria)
    lista.append(moveis)
    return redirect('/')

app.run(debug=True)