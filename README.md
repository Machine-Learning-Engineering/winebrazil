# winebrazil
API para consulta de no banco de dados de viticultura brasileira.

## Requisitos
* podman version 5.5.0
* Python-311
* Fedora release 41 (Forty One)

## Sumary
* [Compile and Run](#compile-and-run)
    * [Compiling source code](#compiling-source-code)
    * [Build a container image](#build-a-container-image)
    * [Running the container](#running-the-container)
        * [Runnig the container using podman](#runnig-the-container-using-podman)
        * [Runnig the container using OpenShift](#runnig-the-container-using-openshift)
* [Using api to create users](#using-api-to-create-users)
* [Using api to drop users](#using-api-to-drop-users)

## Estrutura do projeto
Abaixo a estrura de pasta do projeto
```bash
.
├── app.py
├── Containerfile
├── database
│   ├── comercializacao.csv
│   ├── exportacao.csv
│   ├── importacao.csv
│   ├── processamento.csv
│   └── producao.csv
├── README.md
├── requirements.txt
├── security
│   └── valida_acesso.py
├── service
│   ├── comercializacao.py
│   ├── download.py
│   ├── exportacao.py
│   ├── importacao.py
│   ├── processamento.py
│   └── producao.py
├── swagger
│   ├── atualiza_base.yml
│   ├── comercializacao.yml
│   ├── exportacao.yml
│   ├── importacao.yml
│   ├── login.yml
│   ├── processamento.yml
│   └── producao.yml
└── templates
    └── index.html
```

* **app.py** - arquivo de inicialização
* **README.md** - arquivo de documentação do projeto
* **Containerfile** - arquivo de construção da imagem de container
* **database** - pasta contendo os arquivos de dados                
* **requirements.txt** - arquivo contendo as dependências do projeto
* **security** - pasta contendo os arquivos de segurança
* **service** - pasta contendo os arquivos de serviços
* **swagger** - pasta contendo os arquivos de documentação das APIs
* **templates** - pasta contendo os arquivos de templates

## Executando localmente

Para executar aplicação localmente é recomendando a validação dos requisitos listados acima, caso opte por não realizar este passo, é possível gerar a imagem de container, baixar diretamente do repositório remoto ou ainda executar diretamente da cloud.

### Configurando ambiente virtual

Para configurar o ambiente virtual, execute o seguinte comando no terminal:
```bash
$ python -m venv env
```

### Ativando ambiente virtual
Para ativar o ambiente virtual, execute o seguinte comando no terminal:
```bash
$ source env/bin/activate
```

### Atualizando pip
Para atualizar o pip, execute o seguinte comando no terminal:
```bash
$ pip install --upgrade pip
```

### Instalando dependências
Para instalar as dependências do projeto, execute o seguinte comando no terminal:
```bash
$ pip install -r requirements.txt
```
### Executando aplicação
Para executar a aplicação, execute o seguinte comando no terminal:
```bash
$ python app.py
```
### Acessando a aplicação
Abra o navegador e acesse o seguinte endereço:
```
http://127.0.0.1:5000
```

### Acessando swagger
Para acessar a documentação das APIs, abra o navegador e acesse o seguinte endereço:
```
http://127.0.0.1:5000/apidocs
```

## Gerando container image
Para gerar a imagem de container, execute o seguinte comando no terminal:
```bash
$ podman build . -t winebrazil:v1.0
```

## Baixando imagem de repositório (quay.io)
Para baixar a imagem de container do repositório quay.io, execute o seguinte comando no terminal:
```bash
$ podman pull quay.io/parraes/winebrazil:v1.0
```

## Executando container image
Para executar a imagem de container, execute o seguinte comando no terminal:
```bash
$ podman run -d -p 5000:5000 winebrazil:v1.0
```

## Executando na cloud

## Realizando testes nas APIs

A seguir estão os passos para realizar testes nas APIs utilizando o curl.

### Definindo variavel de ambiente

Caso esteja realizando os testes na cloud, é necessário definir a variável de ambiente `API_URL` com o endereço da API.

```bash
$ export API_URL=http://127.0.0.1:5000
```

### Obtendo token JWT
Para obter o token JWT, execute o seguinte comando no terminal:
```bash
$ export TOKEN=$(curl -X POST "$API_URL/login" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"password\": \"senha123\", \"username\": \"admin\"}" | grep token | cut -d '"' -f 4)

$ echo $TOKEN
```

### Utualizando base de dados
Para atualizar a base de dados, execute o seguinte comando no terminal:
```bash
$ curl -X GET "http://127.0.0.1:5000/atualiza_base" -H "accept: application/json" -H "Authorization: $TOKEN"
```

### Consultando dados de comercialização
Para consultar os dados de comercialização, execute o seguinte comando no terminal:
```bash
curl -X GET "http://127.0.0.1:5000/comercializacao?ano=2000" -H "accept: application/json" -H "Authorization: $TOKEN"
```
Output:
```json
{"dados":[{"Produto":"  Agrin (fermentado, acetico misto)","quantidade(L)":"0"},{"Produto":"  Aguardente de vinho 50\u00b0gl","quantidade(L)":"0"},{"Produto":"  Alcool vinico","quantidade(L)":"0"},{"Produto":"  Bagaceira (graspa)","quantidade(L)":"8.213"},{"Produto":"  Base champenoise champanha","quantidade(L)":"0"},{"Produto":"  Base charmat champanha","quantidade(L)":"0"},{"Produto":"  Base espumante moscatel","quantidade(L)":"0"},{"Produto":"  Bebida de uva","quantidade(L)":"0"},{"Produto":"  Borra l\u00edquida","quantidade(L)":"0"},{"Produto":"  Borra seca","quantidade(L)":"0"},{"Produto":"  Branco","quantidade(L)":"18.055.443"},{"Produto":"  Branco","quantidade(L)":"71.473"},{"Produto":"  Branco","quantidade(L)":"39.688.884"},{"Produto":"  Brandy (conhaque)","quantidade(L)":"2.035.067"},{"Produto":"  Cooler","quantidade(L)":"10.847.415"},{"Produto":"  Coquetel com vinho","quantidade(L)":"0"},{"Produto":"  Destilado de vinho","quantidade(L)":"400.579"},{"Produto":"  Espumante","quantidade(L)":"4.136.072"},{"Produto":"  Espumante  Moscatel","quantidade(L)":"194.723"},{"Produto":"  Espumante Org\u00e2nico","quantidade(L)":"0"},{"Produto":"  Filtrado doce","quantidade(L)":"11.065.803"},{"Produto":"  Jeropiga","quantidade(L)":"66.197"},{"Produto":"  Mistelas","quantidade(L)":"0"},{"Produto":"  Mosto concentrado","quantidade(L)":"0"},{"Produto":"  Mosto de uva","quantidade(L)":"0"},{"Produto":"  Mosto sulfitado","quantidade(L)":"180.900"},{"Produto":"  Nectar de uva","quantidade(L)":"0"},{"Produto":"  Outros produtos","quantidade(L)":"0"},{"Produto":"  Outros sucos de uvas","quantidade(L)":"0"},{"Produto":"  Outros vinhos (sem informa\u00e7\u00e3o detalhada)","quantidade(L)":"0"},{"Produto":"  Polpa de uva","quantidade(L)":"0"},{"Produto":"  Preparado l\u00edquido para refresco","quantidade(L)":"0"},{"Produto":"  Refrigerante +50% suco","quantidade(L)":"0"},{"Produto":"  Rosado","quantidade(L)":"9.150.927"},{"Produto":"  Rosado","quantidade(L)":"1.021.310"},{"Produto":"  Rosado","quantidade(L)":"0"},{"Produto":"  Sangria","quantidade(L)":"0"},{"Produto":"  Suco Ado\u00e7ado","quantidade(L)":"0"},{"Produto":"  Suco Natural Integral","quantidade(L)":"0"},{"Produto":"  Suco Org\u00e2nico","quantidade(L)":"0"},{"Produto":"  Suco Reprocessado/reconstituido","quantidade(L)":"0"},{"Produto":"  Tinto","quantidade(L)":"177.872"},{"Produto":"  Tinto","quantidade(L)":"15.119.076"},{"Produto":"  Tinto","quantidade(L)":"172.183.792"},{"Produto":"  Vinagre balsamico","quantidade(L)":"0"},{"Produto":"  Vinagre duplo","quantidade(L)":"0"},{"Produto":"  Vinagre simples","quantidade(L)":"6.654.097"},{"Produto":"  Vinho acetificado","quantidade(L)":"3.715.390"},{"Produto":"  Vinho base para espumantes","quantidade(L)":"0"},{"Produto":"  Vinho composto","quantidade(L)":"1.084.344"},{"Produto":"  Vinho gaseificado","quantidade(L)":"0"},{"Produto":"  Vinho leve","quantidade(L)":"0"},{"Produto":"  Vinho licoroso","quantidade(L)":"1.110.159"},{"Produto":"ESPUMANTES ","quantidade(L)":"4.330.795"},{"Produto":"OUTROS PRODUTOS COMERCIALIZADOS","quantidade(L)":"37.168.164"},{"Produto":"SUCO DE UVAS","quantidade(L)":"6.847.466"},{"Produto":"SUCO DE UVAS CONCENTRADO","quantidade(L)":"15.315.971"},{"Produto":"VINHO  FINO DE MESA","quantidade(L)":"34.195.829"},{"Produto":"VINHO DE MESA","quantidade(L)":"221.023.603"},{"Produto":"VINHO ESPECIAL","quantidade(L)":"249.345"},{"Produto":"VINHO FRIZANTE","quantidade(L)":"2.583"},{"Produto":"VINHO ORG\u00c2NICO","quantidade(L)":"0"}]}

  "ano": 2000,
  "dados": [
    {
      "id": 1,
      "uf": "SP",
      "valor": 1000000.0
    },
    {
      "id": 2,
      "uf": "RJ",
      "valor": 500000.0
    }
  ]
}

```

