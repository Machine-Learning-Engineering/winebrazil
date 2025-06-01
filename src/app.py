from flask import Flask, request, render_template, jsonify
from flasgger import Swagger, swag_from
from download import atualizar_dados
from producao import consultar_producao
from processamento import consultar_processamento

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

@app.route('/comercializacao', methods=['POST'])
@swag_from('yml/comercializacao.yml')
def comercializacao():
    return jsonify({"message": "Comercialização endpoint is not implemented yet."})

@app.route('/exportacao', methods=['POST'])
@swag_from('yml/exportacao.yml')
def exportacao():
    return jsonify({"message": "Exportação endpoint is not implemented yet."})

@app.route('/importacao', methods=['POST'])
@swag_from('yml/importacao.yml')
def importacao():
    return jsonify({"message": "Importação endpoint is not implemented yet."})

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