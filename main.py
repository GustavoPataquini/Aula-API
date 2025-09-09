from flask import Flask, request, make_response, jsonify
from bd import Carros 

app = Flask('Carros')

#metodo 1- visualizacao de dados (GET)
@app.route('/carrinho',methods=['GET'])
def get_carros():
    return Carros



# metodo 1 part 2- GET

@app.route('/carrinhos/<int:id>', methods= ['GET'])
def get_carros_id(id_pam):
    for car in Carros:
        if car.get('id') == id_pam:
            return jsonify(car)
        
        @app.route('/carrinho',methods=['POST'])
        def criar_carro():
            car = request.json
            Carros.append(car)
        return make_response(
              jsonify(
                  mensagem= 'carro cadastrado com sucesso!!', car = car
              )


    )        

@app.route('/carrinho/<int:id>',methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id')==id:
            del Carros[indice]
            return jsonify(
                {'mensagem': "carro excluido"}
            )

@app.route('/carrinho/<int:id>',methods=['PUT'])
def editar_carro(id):
    carro_alterado= request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id')==id:
            Carros [indice].update(carro_alterado)
            return jsonify(
                Carros[indice]
            )


app.run(port=5000, host= 'localhost',debug=True)


        







