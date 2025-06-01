from flask import Flask, request, render_template, jsonify
from flasgger import Swagger, swag_from


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

@app.route('/processamento', methods=['POST'])
@swag_from('yml/processamento.yml')
def processamento():
    return jsonify({"message": "Processamento endpoint is not implemented yet."})

@app.route('/producao', methods=['POST'])
@swag_from('yml/producao.yml')
def producao():
    return jsonify({"message": "Produção endpoint is not implemented yet."})



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')