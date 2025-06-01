from flask import Flask, request, render_template, jsonify
from flasgger import Swagger, swag_from

# Importando os serviços necessários
from service.download import atualizar_dados
from service.producao import consultar_producao
from service.processamento import consultar_processamento
from service.importacao import consultar_importacao
from service.exportacao import consultar_exportacao
from service.comercializacao import consultar_comercializacao

app = Flask(__name__)

#########################swagger
template = {
	"swagger": "2.0",
	"info": {
	"title": "Wine Brazil API",
	"description": "API para classificar dados de viticultura e enologia no Brasil",
	"version": "1.0"
	}
}

swagger = Swagger(app, template=template)

@app.route('/comercializacao', methods=['GET'])
@swag_from('yml/comercializacao.yml')
def comercializacao():
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    resultado, status = consultar_comercializacao(ano=ano, produto=produto)
    return jsonify(resultado), status

@app.route('/exportacao', methods=['GET'])
@swag_from('yml/exportacao.yml')
def exportacao():
    ano = request.args.get('ano')
    pais = request.args.get('pais')
    resultado, status = consultar_exportacao(ano=ano, pais=pais)
    return jsonify(resultado), status

@app.route('/importacao', methods=['GET'])
@swag_from('yml/importacao.yml')
def importacao():
    ano = request.args.get('ano')
    pais = request.args.get('pais')
    resultado, status = consultar_importacao(ano=ano, pais=pais)
    return jsonify(resultado), status

@app.route('/processamento', methods=['GET'])
@swag_from('yml/processamento.yml')
def processamento():
    ano = request.args.get('ano')
    cultivar = request.args.get('cultivar')
    resultado, status = consultar_processamento(ano=ano, cultivar=cultivar)
    return jsonify(resultado), status

@app.route('/producao', methods=['GET'])
@swag_from('yml/producao.yml')
def producao():
    ano = request.args.get('ano')
    produto = request.args.get('produto')
    resultado, status = consultar_producao(ano=ano, produto=produto)
    return jsonify(resultado), status


@app.route('/atualiza_base', methods=['GET'])
@swag_from('yml/atualiza_base.yml')
def atualiza_base():
    sucesso = atualizar_dados()
    if sucesso:
        return jsonify({"message": "Base de dados atualizada com sucesso."})
    else:
        return jsonify({"message": "Erro ao atualizar a base de dados."}), 500


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')