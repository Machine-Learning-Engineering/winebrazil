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
``
