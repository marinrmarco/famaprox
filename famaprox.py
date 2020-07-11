from flask import Flask, render_template, request
from random import random, randint
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    #Definir número aleatorio de 4 cifras, que no comience con 0 y no repita cifras
    numero = []
    for i in range(4):
        #si i = 0 seleccionar un número entre 1 y 9
        if i == 0:
            num = randint(1,9)
        else:
            # num no debe existir en la lista
            while num in numero:
                num = randint(0,9)
        numero.append(num)
    print(numero)
    return render_template("index.html")