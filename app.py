from flask import Flask, render_template, request, redirect
import os

class Moveis:
    def __init__(self, nome, categoria, imagem):
        self.nome = nome
        self.categaria = categoria
        self.imagem = imagem
    

movel = Moveis("Mesa de jantar", "Mesas", "/static/img/mesa-lua.png")
movel2 = Moveis("Poltrona Balanço", "Acentos", "/static/img/poltrona-balanço.png")
movel3 = Moveis("Sofá Aqua", "Sofás", "/static/img/sofa-aqua.png")
lista = [movel, movel2, movel3]

app = Flask(__name__)

PASTA_UPLOAD = "static/img"
app.config[PASTA_UPLOAD] = PASTA_UPLOAD

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
    imagem = request.files.get('imagem')

    if imagem and imagem.filename != '':
        filename = os.path.join(app.config[PASTA_UPLOAD], imagem.filename)
        imagem.save(filename)
        imagem_url = f"/static/img/{imagem.filename}"

    else:
        imagem_url = "/static/img/default-image.png"

    moveis = Moveis(nome, categoria, imagem_url)
    lista.append(moveis)
    return redirect('/')

app.run(debug=True)