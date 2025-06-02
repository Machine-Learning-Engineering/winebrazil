# winebrazil
API para consulta de no banco de dados de viticultura brasileira.

## Sumary
- [Requisitos](#requisitos)
- [Sumary](#sumary)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Executando localmente](#executando-localmente)
  - [Configurando ambiente virtual](#configurando-ambiente-virtual)
  - [Ativando ambiente virtual](#ativando-ambiente-virtual)
  - [Atualizando pip](#atualizando-pip)
  - [Instalando dependências](#instalando-dependências)
  - [Executando aplicação](#executando-aplicação)
  - [Acessando a aplicação](#acessando-a-aplicação)
  - [Acessando swagger](#acessando-swagger)
- [Gerando container image](#gerando-container-image)
- [Baixando imagem de repositório (quay.io)](#baixando-imagem-de-repositório-quayio)
- [Executando container image](#executando-container-image)
- [Executando na cloud](#executando-na-cloud)
- [Realizando testes nas APIs](#realizando-testes-nas-apis)
  - [Definindo variavel de ambiente](#definindo-variavel-de-ambiente)
  - [Obtendo token JWT](#obtendo-token-jwt)
  - [Utualizando base de dados](#utualizando-base-de-dados)
  - [Consultando dados de comercialização](#consultando-dados-de-comercialização)
  - [Consultando dados de exportação](#consultando-dados-de-exportação)
  - [Consultando dados de importação](#consultando-dados-de-importação)
  - [Consultando dados de processamento](#consultando-dados-de-processamento)
  - [Consultando dados de produção](#consultando-dados-de-produção)
- [Referências](#referências)


## Arquitetura

A arquitetura da aplicação é baseada em Flask, uma microframework para Python, que permite a criação de APIs RESTful de forma rápida e fácil. A aplicação é dividida em camadas, onde cada camada tem uma responsabilidade específica. Abaixo a imagem representa a visão logica da arquitetura da aplicação:

<p align="center">
  <img src="https://github.com/Machine-Learning-Engineering/winebrazil/blob/main/docs/fig1.jpeg" alt="Arquitetura da aplicação - Visão Lógica">
</p>

Na figura abaixo, é apresentada a as APIs disponíveis na aplicação, que são responsáveis por fornecer os dados de comercialização, exportação, importação, processamento e produção de vinhos no Brasil. Para garantir a segurança das APIs, é utilizado o JWT (JSON Web Token) para autenticação e autorização dos usuários. Abaixo a imagem representa a visão logica das APIs disponíveis na aplicação:

<p align="center">
  <img src="https://github.com/Machine-Learning-Engineering/winebrazil/blob/main/docs/fig2.jpeg" alt="Arquitetura da aplicação - Visão APIs">
</p>



## Requisitos
* podman version 5.5.0
* Python-311
* Fedora release 41 (Forty One)

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
Para executar a aplicação a partir da cloud publica, abra o navegador e acesse o seguinte endereço:
```
http://ec2-54-234-51-169.compute-1.amazonaws.com/
```

## Realizando testes nas APIs

A seguir estão os passos para realizar testes nas APIs utilizando o curl.

### Definindo variavel de ambiente

Caso esteja realizando os testes na cloud, é necessário definir a variável de ambiente `API_URL` com o endereço da API.

* Localmente:
```bash
$ export API_URL=http://127.0.0.1:5000
```

* Na cloud:
```bash
$ export API_URL=http://ec2-54-234-51-169.compute-1.amazonaws.com:5000
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
{
  "dados": [
    {
      "Produto": "  Agrin (fermentado, acetico misto)",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Aguardente de vinho 50°gl",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Alcool vinico",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Bagaceira (graspa)",
      "quantidade(L)": "8.213"
    },
    {
      "Produto": "  Base champenoise champanha",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Base charmat champanha",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Base espumante moscatel",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Bebida de uva",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Borra líquida",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Borra seca",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Branco",
      "quantidade(L)": "18.055.443"
    },
    {
      "Produto": "  Branco",
      "quantidade(L)": "71.473"
    },
    {
      "Produto": "  Branco",
      "quantidade(L)": "39.688.884"
    },
    {
      "Produto": "  Brandy (conhaque)",
      "quantidade(L)": "2.035.067"
    },
    {
      "Produto": "  Cooler",
      "quantidade(L)": "10.847.415"
    },
    {
      "Produto": "  Coquetel com vinho",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Destilado de vinho",
      "quantidade(L)": "400.579"
    },
    {
      "Produto": "  Espumante",
      "quantidade(L)": "4.136.072"
    },
    {
      "Produto": "  Espumante  Moscatel",
      "quantidade(L)": "194.723"
    },
    {
      "Produto": "  Espumante Orgânico",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Filtrado doce",
      "quantidade(L)": "11.065.803"
    },
    {
      "Produto": "  Jeropiga",
      "quantidade(L)": "66.197"
    },
    {
      "Produto": "  Mistelas",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Mosto concentrado",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Mosto de uva",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Mosto sulfitado",
      "quantidade(L)": "180.900"
    },
    {
      "Produto": "  Nectar de uva",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Outros produtos",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Outros sucos de uvas",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Outros vinhos (sem informação detalhada)",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Polpa de uva",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Preparado líquido para refresco",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Refrigerante +50% suco",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Rosado",
      "quantidade(L)": "9.150.927"
    },
    {
      "Produto": "  Rosado",
      "quantidade(L)": "1.021.310"
    },
    {
      "Produto": "  Rosado",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Sangria",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Suco Adoçado",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Suco Natural Integral",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Suco Orgânico",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Suco Reprocessado/reconstituido",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Tinto",
      "quantidade(L)": "177.872"
    },
    {
      "Produto": "  Tinto",
      "quantidade(L)": "15.119.076"
    },
    {
      "Produto": "  Tinto",
      "quantidade(L)": "172.183.792"
    },
    {
      "Produto": "  Vinagre balsamico",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Vinagre duplo",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Vinagre simples",
      "quantidade(L)": "6.654.097"
    },
    {
      "Produto": "  Vinho acetificado",
      "quantidade(L)": "3.715.390"
    },
    {
      "Produto": "  Vinho base para espumantes",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Vinho composto",
      "quantidade(L)": "1.084.344"
    },
    {
      "Produto": "  Vinho gaseificado",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Vinho leve",
      "quantidade(L)": "0"
    },
    {
      "Produto": "  Vinho licoroso",
      "quantidade(L)": "1.110.159"
    },
    {
      "Produto": "ESPUMANTES ",
      "quantidade(L)": "4.330.795"
    },
    {
      "Produto": "OUTROS PRODUTOS COMERCIALIZADOS",
      "quantidade(L)": "37.168.164"
    },
    {
      "Produto": "SUCO DE UVAS",
      "quantidade(L)": "6.847.466"
    },
    {
      "Produto": "SUCO DE UVAS CONCENTRADO",
      "quantidade(L)": "15.315.971"
    },
    {
      "Produto": "VINHO  FINO DE MESA",
      "quantidade(L)": "34.195.829"
    },
    {
      "Produto": "VINHO DE MESA",
      "quantidade(L)": "221.023.603"
    },
    {
      "Produto": "VINHO ESPECIAL",
      "quantidade(L)": "249.345"
    },
    {
      "Produto": "VINHO FRIZANTE",
      "quantidade(L)": "2.583"
    },
    {
      "Produto": "VINHO ORGÂNICO",
      "quantidade(L)": "0"
    }
  ]
}
```

### Consultando dados de exportação
Para consultar os dados de exportação, execute o seguinte comando no terminal:
```bash
curl -X GET "http://127.0.0.1:5000/exportacao?ano=2000" -H "accept: application/json" -H "Authorization: $TOKEN"
```
Output:
```json
{
  "dados": [
    {
      "País": "Afeganistão",
      "quantidade(L)": "0"
    },
    {
      "País": "Alemanha, República Democrática",
      "quantidade(L)": "9.900"
    },
    {
      "País": "Angola",
      "quantidade(L)": "249.717"
    },
    {
      "País": "Anguilla",
      "quantidade(L)": "0"
    },
    {
      "País": "Antilhas Holandesas",
      "quantidade(L)": "0"
    },
    {
      "País": "Antígua e Barbuda",
      "quantidade(L)": "0"
    },
    {
      "País": "Argentina",
      "quantidade(L)": "0"
    },
    {
      "País": "Argélia",
      "quantidade(L)": "0"
    },
    {
      "País": "Aruba",
      "quantidade(L)": "0"
    },
    {
      "País": "Arábia Saudita",
      "quantidade(L)": "0"
    },
    {
      "País": "Austrália",
      "quantidade(L)": "0"
    },
    {
      "País": "Bahamas",
      "quantidade(L)": "0"
    },
    {
      "País": "Bangladesh",
      "quantidade(L)": "0"
    },
    {
      "País": "Barbados",
      "quantidade(L)": "0"
    },
    {
      "País": "Barein",
      "quantidade(L)": "0"
    },
    {
      "País": "Belice",
      "quantidade(L)": "0"
    },
    {
      "País": "Benin",
      "quantidade(L)": "0"
    },
    {
      "País": "Bermudas",
      "quantidade(L)": "0"
    },
    {
      "País": "Bolívia",
      "quantidade(L)": "265.988"
    },
    {
      "País": "Brasil",
      "quantidade(L)": "0"
    },
    {
      "País": "Bulgária",
      "quantidade(L)": "0"
    },
    {
      "País": "Bélgica",
      "quantidade(L)": "0"
    },
    {
      "País": "Bósnia-Herzegovina",
      "quantidade(L)": "0"
    },
    {
      "País": "Cabo Verde",
      "quantidade(L)": "0"
    },
    {
      "País": "Camarões",
      "quantidade(L)": "0"
    },
    {
      "País": "Canadá",
      "quantidade(L)": "4.480"
    },
    {
      "País": "Catar",
      "quantidade(L)": "0"
    },
    {
      "País": "Cayman, Ilhas",
      "quantidade(L)": "0"
    },
    {
      "País": "Chile",
      "quantidade(L)": "0"
    },
    {
      "País": "China",
      "quantidade(L)": "0"
    },
    {
      "País": "Chipre",
      "quantidade(L)": "0"
    },
    {
      "País": "Cingapura",
      "quantidade(L)": "0"
    },
    {
      "País": "Cocos (Keeling), Ilhas",
      "quantidade(L)": "0"
    },
    {
      "País": "Colômbia",
      "quantidade(L)": "0"
    },
    {
      "País": "Comores",
      "quantidade(L)": "0"
    },
    {
      "País": "Congo",
      "quantidade(L)": "0"
    },
    {
      "País": "Coreia, Republica Sul",
      "quantidade(L)": "0"
    },
    {
      "País": "Costa Rica",
      "quantidade(L)": "0"
    },
    {
      "País": "Costa do Marfim",
      "quantidade(L)": "0"
    },
    {
      "País": "Coveite (Kuweit)",
      "quantidade(L)": "0"
    },
    {
      "País": "Croácia",
      "quantidade(L)": "0"
    },
    {
      "País": "Cuba",
      "quantidade(L)": "0"
    },
    {
      "País": "Curaçao",
      "quantidade(L)": "0"
    },
    {
      "País": "Dinamarca",
      "quantidade(L)": "0"
    },
    {
      "País": "Dominica",
      "quantidade(L)": "0"
    },
    {
      "País": "El Salvador",
      "quantidade(L)": "0"
    },
    {
      "País": "Emirados Arabes Unidos",
      "quantidade(L)": "0"
    },
    {
      "País": "Equador",
      "quantidade(L)": "0"
    },
    {
      "País": "Eslovaca, Republica",
      "quantidade(L)": "0"
    },
    {
      "País": "Espanha",
      "quantidade(L)": "0"
    },
    {
      "País": "Estados Unidos",
      "quantidade(L)": "2.151"
    },
    {
      "País": "Estônia",
      "quantidade(L)": "0"
    },
    {
      "País": "Filipinas",
      "quantidade(L)": "0"
    },
    {
      "País": "Finlândia",
      "quantidade(L)": "40.824"
    },
    {
      "País": "França",
      "quantidade(L)": "600"
    },
    {
      "País": "Gabão",
      "quantidade(L)": "0"
    },
    {
      "País": "Gana",
      "quantidade(L)": "0"
    },
    {
      "País": "Gibraltar",
      "quantidade(L)": "0"
    },
    {
      "País": "Granada",
      "quantidade(L)": "0"
    },
    {
      "País": "Grécia",
      "quantidade(L)": "0"
    },
    {
      "País": "Guatemala",
      "quantidade(L)": "0"
    },
    {
      "País": "Guiana",
      "quantidade(L)": "0"
    },
    {
      "País": "Guiana Francesa",
      "quantidade(L)": "0"
    },
    {
      "País": "Guine Bissau",
      "quantidade(L)": "0"
    },
    {
      "País": "Guine Equatorial",
      "quantidade(L)": "0"
    },
    {
      "País": "Haiti",
      "quantidade(L)": "0"
    },
    {
      "País": "Honduras",
      "quantidade(L)": "0"
    },
    {
      "País": "Hong Kong",
      "quantidade(L)": "0"
    },
    {
      "País": "Hungria",
      "quantidade(L)": "0"
    },
    {
      "País": "Ilha de Man",
      "quantidade(L)": "0"
    },
    {
      "País": "Ilhas Virgens",
      "quantidade(L)": "0"
    },
    {
      "País": "Indonésia",
      "quantidade(L)": "0"
    },
    {
      "País": "Iraque",
      "quantidade(L)": "0"
    },
    {
      "País": "Irlanda",
      "quantidade(L)": "0"
    },
    {
      "País": "Irã",
      "quantidade(L)": "0"
    },
    {
      "País": "Itália",
      "quantidade(L)": "0"
    },
    {
      "País": "Jamaica",
      "quantidade(L)": "0"
    },
    {
      "País": "Japão",
      "quantidade(L)": "672.280"
    },
    {
      "País": "Jordânia",
      "quantidade(L)": "0"
    },
    {
      "País": "Letônia",
      "quantidade(L)": "0"
    },
    {
      "País": "Libéria",
      "quantidade(L)": "0"
    },
    {
      "País": "Luxemburgo",
      "quantidade(L)": "0"
    },
    {
      "País": "Líbano",
      "quantidade(L)": "0"
    },
    {
      "País": "Macau",
      "quantidade(L)": "0"
    },
    {
      "País": "Malavi",
      "quantidade(L)": "0"
    },
    {
      "País": "Malta",
      "quantidade(L)": "0"
    },
    {
      "País": "Malásia",
      "quantidade(L)": "0"
    },
    {
      "País": "Marshall, Ilhas",
      "quantidade(L)": "0"
    },
    {
      "País": "Martinica",
      "quantidade(L)": "0"
    },
    {
      "País": "Mauritânia",
      "quantidade(L)": "0"
    },
    {
      "País": "Montenegro",
      "quantidade(L)": "0"
    },
    {
      "País": "Moçambique",
      "quantidade(L)": "0"
    },
    {
      "País": "México",
      "quantidade(L)": "0"
    },
    {
      "País": "Namíbia",
      "quantidade(L)": "0"
    },
    {
      "País": "Nicarágua",
      "quantidade(L)": "0"
    },
    {
      "País": "Nigéria",
      "quantidade(L)": "396"
    },
    {
      "País": "Noruega",
      "quantidade(L)": "0"
    },
    {
      "País": "Nova Caledônia",
      "quantidade(L)": "0"
    },
    {
      "País": "Nova Zelândia",
      "quantidade(L)": "0"
    },
    {
      "País": "Omã",
      "quantidade(L)": "0"
    },
    {
      "País": "Palau",
      "quantidade(L)": "0"
    },
    {
      "País": "Panamá",
      "quantidade(L)": "0"
    },
    {
      "País": "Paraguai",
      "quantidade(L)": "4.997.801"
    },
    {
      "País": "Países Baixos",
      "quantidade(L)": "0"
    },
    {
      "País": "Peru",
      "quantidade(L)": "0"
    },
    {
      "País": "Pitcairn",
      "quantidade(L)": "0"
    },
    {
      "País": "Polônia",
      "quantidade(L)": "0"
    },
    {
      "País": "Porto Rico",
      "quantidade(L)": "0"
    },
    {
      "País": "Portugal",
      "quantidade(L)": "0"
    },
    {
      "País": "Quênia",
      "quantidade(L)": "0"
    },
    {
      "País": "Reino Unido",
      "quantidade(L)": "0"
    },
    {
      "País": "República Dominicana",
      "quantidade(L)": "0"
    },
    {
      "País": "Rússia",
      "quantidade(L)": "0"
    },
    {
      "País": "Senegal",
      "quantidade(L)": "0"
    },
    {
      "País": "Serra Leoa",
      "quantidade(L)": "0"
    },
    {
      "País": "Singapura",
      "quantidade(L)": "0"
    },
    {
      "País": "Suazilândia",
      "quantidade(L)": "0"
    },
    {
      "País": "Suriname",
      "quantidade(L)": "0"
    },
    {
      "País": "Suécia",
      "quantidade(L)": "0"
    },
    {
      "País": "Suíça",
      "quantidade(L)": "0"
    },
    {
      "País": "São Cristóvão e Névis",
      "quantidade(L)": "0"
    },
    {
      "País": "São Tomé e Príncipe",
      "quantidade(L)": "0"
    },
    {
      "País": "São Vicente e Granadinas",
      "quantidade(L)": "0"
    },
    {
      "País": "Sérvia",
      "quantidade(L)": "0"
    },
    {
      "País": "Tailândia",
      "quantidade(L)": "0"
    },
    {
      "País": "Taiwan (Formosa)",
      "quantidade(L)": "0"
    },
    {
      "País": "Tanzânia",
      "quantidade(L)": "0"
    },
    {
      "País": "Tcheca, República",
      "quantidade(L)": "0"
    },
    {
      "País": "Togo",
      "quantidade(L)": "0"
    },
    {
      "País": "Toquelau",
      "quantidade(L)": "0"
    },
    {
      "País": "Trinidade Tobago",
      "quantidade(L)": "0"
    },
    {
      "País": "Tunísia",
      "quantidade(L)": "0"
    },
    {
      "País": "Turquia",
      "quantidade(L)": "0"
    },
    {
      "País": "Tuvalu",
      "quantidade(L)": "0"
    },
    {
      "País": "Uruguai",
      "quantidade(L)": "44.476"
    },
    {
      "País": "Vanuatu",
      "quantidade(L)": "0"
    },
    {
      "País": "Venezuela",
      "quantidade(L)": "0"
    },
    {
      "País": "Vietnã",
      "quantidade(L)": "0"
    },
    {
      "País": "África do Sul",
      "quantidade(L)": "0"
    },
    {
      "País": "Áustria",
      "quantidade(L)": "0"
    },
    {
      "País": "Índia",
      "quantidade(L)": "0"
    }
  ]
}
```

### Consultando dados de importação
Para consultar os dados de importação, execute o seguinte comando no terminal:
```bash
curl -X GET "http://127.0.0.1:5000/importacao?ano=2000" -H "accept: application/json" -H "Authorization: $TOKEN"
```
Output:
```json 
{
  "dados": [
    {
      "País": "Africa do Sul",
      "quantidade(L)": "0"
    },
    {
      "País": "Alemanha",
      "quantidade(L)": "1.164.724"
    },
    {
      "País": "Argentina",
      "quantidade(L)": "2.724.941"
    },
    {
      "País": "Argélia",
      "quantidade(L)": "0"
    },
    {
      "País": "Armênia",
      "quantidade(L)": "0"
    },
    {
      "País": "Arábia Saudita",
      "quantidade(L)": "0"
    },
    {
      "País": "Austrália",
      "quantidade(L)": "130.097"
    },
    {
      "País": "Bermudas",
      "quantidade(L)": "0"
    },
    {
      "País": "Bolívia",
      "quantidade(L)": "0"
    },
    {
      "País": "Brasil",
      "quantidade(L)": "0"
    },
    {
      "País": "Bulgária",
      "quantidade(L)": "0"
    },
    {
      "País": "Bélgica",
      "quantidade(L)": "0"
    },
    {
      "País": "Bósnia-Herzegovina",
      "quantidade(L)": "0"
    },
    {
      "País": "Canada",
      "quantidade(L)": "0"
    },
    {
      "País": "Chile",
      "quantidade(L)": "5.559.322"
    },
    {
      "País": "China",
      "quantidade(L)": "0"
    },
    {
      "País": "Coreia do Sul, República",
      "quantidade(L)": "0"
    },
    {
      "País": "Croácia",
      "quantidade(L)": "0"
    },
    {
      "País": "Cuba",
      "quantidade(L)": "0"
    },
    {
      "País": "Emirados Árabes Unidos",
      "quantidade(L)": "0"
    },
    {
      "País": "Eslováquia",
      "quantidade(L)": "0"
    },
    {
      "País": "Eslovênia",
      "quantidade(L)": "0"
    },
    {
      "País": "Espanha",
      "quantidade(L)": "531.425"
    },
    {
      "País": "Estados Unidos",
      "quantidade(L)": "426.442"
    },
    {
      "País": "França",
      "quantidade(L)": "3.431.635"
    },
    {
      "País": "Geórgia",
      "quantidade(L)": "0"
    },
    {
      "País": "Geórgia do Sul e Sandwich do Sul, Ilhas",
      "quantidade(L)": "0"
    },
    {
      "País": "Grécia",
      "quantidade(L)": "0"
    },
    {
      "País": "Hong Kong",
      "quantidade(L)": "0"
    },
    {
      "País": "Hungria",
      "quantidade(L)": "0"
    },
    {
      "País": "Indonésia",
      "quantidade(L)": "0"
    },
    {
      "País": "Irlanda",
      "quantidade(L)": "0"
    },
    {
      "País": "Israel",
      "quantidade(L)": "0"
    },
    {
      "País": "Itália",
      "quantidade(L)": "8.261.193"
    },
    {
      "País": "Iugoslávia",
      "quantidade(L)": "0"
    },
    {
      "País": "Japão",
      "quantidade(L)": "0"
    },
    {
      "País": "Luxemburgo",
      "quantidade(L)": "0"
    },
    {
      "País": "Líbano",
      "quantidade(L)": "0"
    },
    {
      "País": "Macedônia",
      "quantidade(L)": "0"
    },
    {
      "País": "Marrocos",
      "quantidade(L)": "0"
    },
    {
      "País": "Moldávia",
      "quantidade(L)": "0"
    },
    {
      "País": "Montenegro",
      "quantidade(L)": "0"
    },
    {
      "País": "México",
      "quantidade(L)": "0"
    },
    {
      "País": "Noruega",
      "quantidade(L)": "0"
    },
    {
      "País": "Nova Zelândia",
      "quantidade(L)": "0"
    },
    {
      "País": "Não consta na tabela",
      "quantidade(L)": "0"
    },
    {
      "País": "Não declarados",
      "quantidade(L)": "0"
    },
    {
      "País": "Outros",
      "quantidade(L)": "73.451"
    },
    {
      "País": "Panamá",
      "quantidade(L)": "0"
    },
    {
      "País": "Paraguai",
      "quantidade(L)": "0"
    },
    {
      "País": "Países Baixos (Holanda)",
      "quantidade(L)": "0"
    },
    {
      "País": "Peru",
      "quantidade(L)": "0"
    },
    {
      "País": "Porto Rico",
      "quantidade(L)": "0"
    },
    {
      "País": "Portugal",
      "quantidade(L)": "5.011.051"
    },
    {
      "País": "Reino Unido",
      "quantidade(L)": "0"
    },
    {
      "País": "Republica Dominicana",
      "quantidade(L)": "0"
    },
    {
      "País": "Romênia",
      "quantidade(L)": "0"
    },
    {
      "País": "Rússia",
      "quantidade(L)": "0"
    },
    {
      "País": "San Marino",
      "quantidade(L)": "0"
    },
    {
      "País": "Suazilândia",
      "quantidade(L)": "0"
    },
    {
      "País": "Suíça",
      "quantidade(L)": "0"
    },
    {
      "País": "Sérvia",
      "quantidade(L)": "0"
    },
    {
      "País": "Síria",
      "quantidade(L)": "0"
    },
    {
      "País": "Tcheca, República",
      "quantidade(L)": "0"
    },
    {
      "País": "Tunísia",
      "quantidade(L)": "0"
    },
    {
      "País": "Turquia",
      "quantidade(L)": "0"
    },
    {
      "País": "Ucrânia",
      "quantidade(L)": "0"
    },
    {
      "País": "Uruguai",
      "quantidade(L)": "1.961.733"
    },
    {
      "País": "Áustria",
      "quantidade(L)": "0"
    }
  ]
}
```

### Consultando dados de processamento
Para consultar os dados de processamento, execute o seguinte comando no terminal:
```bash
curl -X GET "http://127.0.0.1:5000/processamento?ano=2000" -H "accept: application/json" -H "Authorization: $TOKEN"
```
Output:
```json
{
  "dados": [
    {
      "cultivar": "Alfrocheiro",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Aliatico",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Alicante Bouschet",
      "quantidade(L)": "160.318"
    },
    {
      "cultivar": "Aligote",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Altesse",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Alvarinho",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Ancelota",
      "quantidade(L)": "26.088"
    },
    {
      "cultivar": "Aramon",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Arinarnoa",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Arriloba",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Aspirant Bouschet",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Auxerrois",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "BRANCAS E ROSADAS",
      "quantidade(L)": "49.613.743"
    },
    {
      "cultivar": "Barbera",
      "quantidade(L)": "397.479"
    },
    {
      "cultivar": "Bonarda",
      "quantidade(L)": "67.152"
    },
    {
      "cultivar": "Burger",
      "quantidade(L)": "13.028"
    },
    {
      "cultivar": "Cabernet Franc",
      "quantidade(L)": "4.419.829"
    },
    {
      "cultivar": "Cabernet Sauvignon",
      "quantidade(L)": "4.591.561"
    },
    {
      "cultivar": "Caladoc",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Campanario",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Canaiolo",
      "quantidade(L)": "4.927"
    },
    {
      "cultivar": "Carignan",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Carmenere",
      "quantidade(L)": "26.460"
    },
    {
      "cultivar": "Castelão",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Chardonnay",
      "quantidade(L)": "2.873.611"
    },
    {
      "cultivar": "Chasselas",
      "quantidade(L)": "179.914"
    },
    {
      "cultivar": "Chenin Blanc",
      "quantidade(L)": "496.981"
    },
    {
      "cultivar": "Cinsaut",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Clairette(1)",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Colombard",
      "quantidade(L)": "343.181"
    },
    {
      "cultivar": "Corvina",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Croatina",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Dolcetto",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Dom Felder",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Durif",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Egiodola",
      "quantidade(L)": "325.911"
    },
    {
      "cultivar": "Ekigaina",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Festival (Sugraone)",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Flora",
      "quantidade(L)": "581.824"
    },
    {
      "cultivar": "Franconia",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Freisa",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Gamay Beaujolais",
      "quantidade(L)": "557.368"
    },
    {
      "cultivar": "Gamay St Romain",
      "quantidade(L)": "86.966"
    },
    {
      "cultivar": "Garganega",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Gewurztraminer",
      "quantidade(L)": "474.897"
    },
    {
      "cultivar": "Gouveio",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Grand Noir",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Grenache",
      "quantidade(L)": "298"
    },
    {
      "cultivar": "Gros Manseng",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Italia (Pirovano 65) (PE)",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Jaen",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Lagrein",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Lambrusco",
      "quantidade(L)": "45.815"
    },
    {
      "cultivar": "Maccabeo",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Malbec",
      "quantidade(L)": "105.730"
    },
    {
      "cultivar": "Malvasia",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Malvasia Amarela",
      "quantidade(L)": "400.884"
    },
    {
      "cultivar": "Malvasia Bianca",
      "quantidade(L)": "1.792.354"
    },
    {
      "cultivar": "Malvasia Chianti",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Malvasia Istriana",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Malvasia Verde",
      "quantidade(L)": "60.915"
    },
    {
      "cultivar": "Malvasia di Candia",
      "quantidade(L)": "403.192"
    },
    {
      "cultivar": "Marselan",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Marzemina",
      "quantidade(L)": "7.765"
    },
    {
      "cultivar": "Merlot",
      "quantidade(L)": "6.223.276"
    },
    {
      "cultivar": "Mistura de uvas viníferas branco",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Mistura de uvas viníferas rosado",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Mistura de uvas viníferas tinto ",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Molinera",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Montepulciano",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Moscato Bailey",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Moscato Bianco R2",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Moscato Branco",
      "quantidade(L)": "19.535.723"
    },
    {
      "cultivar": "Moscato Canelli",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Moscato Giallo",
      "quantidade(L)": "17.700"
    },
    {
      "cultivar": "Moscato Nazareno",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Moscato Rosado",
      "quantidade(L)": "31.105"
    },
    {
      "cultivar": "Moscato de Alexandria",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Muller Thurgau",
      "quantidade(L)": "22.207"
    },
    {
      "cultivar": "Muscadelle",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Muscat à Petits Grains",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Napa Gamay",
      "quantidade(L)": "290.790"
    },
    {
      "cultivar": "Nebbiolo",
      "quantidade(L)": "80"
    },
    {
      "cultivar": "Ora",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Outras(3)",
      "quantidade(L)": "73.487"
    },
    {
      "cultivar": "Outras1",
      "quantidade(L)": "10.833"
    },
    {
      "cultivar": "Palomino",
      "quantidade(L)": "28.451"
    },
    {
      "cultivar": "Petit Manseng",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Petit Verdot",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Petite Sirah",
      "quantidade(L)": "177.654"
    },
    {
      "cultivar": "Peverella",
      "quantidade(L)": "556.215"
    },
    {
      "cultivar": "Pinot Blanc",
      "quantidade(L)": "486.786"
    },
    {
      "cultivar": "Pinot Gris",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Pinot Noir",
      "quantidade(L)": "621.890"
    },
    {
      "cultivar": "Pinot Saint George",
      "quantidade(L)": "255.810"
    },
    {
      "cultivar": "Pinotage",
      "quantidade(L)": "1.851.305"
    },
    {
      "cultivar": "Piriquita",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Primitivo",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Prosecco",
      "quantidade(L)": "455.579"
    },
    {
      "cultivar": "Rebo",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Red Veltliner",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Refosco",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Riesling Italico",
      "quantidade(L)": "8.855.066"
    },
    {
      "cultivar": "Riesling Renano",
      "quantidade(L)": "380.135"
    },
    {
      "cultivar": "Rondinella",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Ruby Cabernet",
      "quantidade(L)": "42.699"
    },
    {
      "cultivar": "Sangiovese",
      "quantidade(L)": "684"
    },
    {
      "cultivar": "Saperavi ",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Sauvignon Blanc(2)",
      "quantidade(L)": "1.156.987"
    },
    {
      "cultivar": "Sauvignon Gris",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Schonburger",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Seara Nova",
      "quantidade(L)": "18.890"
    },
    {
      "cultivar": "Semillon",
      "quantidade(L)": "4.310.660"
    },
    {
      "cultivar": "Sira (falsa)",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Sylvaner",
      "quantidade(L)": "129.489"
    },
    {
      "cultivar": "TINTAS",
      "quantidade(L)": "23.975.805"
    },
    {
      "cultivar": "Tannat",
      "quantidade(L)": "3.487.128"
    },
    {
      "cultivar": "Tempranillo",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Teroldego",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Tinta Barroca",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Tinta Madeira",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Tinta Roriz ",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Tintoria",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Tocai Friulano",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Torrontes",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Touriga Francesa",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Touriga Nacional",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Trebbiano",
      "quantidade(L)": "5.413.475"
    },
    {
      "cultivar": "Trebbiano Toscano",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Trincdeira",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Trousseau",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Verdea",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Verdelho",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Verdiso",
      "quantidade(L)": "1.435"
    },
    {
      "cultivar": "Vermentino",
      "quantidade(L)": "17.835"
    },
    {
      "cultivar": "Vernaccia",
      "quantidade(L)": "501.737"
    },
    {
      "cultivar": "Viogner ",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Viognier",
      "quantidade(L)": "0"
    },
    {
      "cultivar": "Zinfandel",
      "quantidade(L)": "189.989"
    }
  ]
}
```
### Consultando dados de produção
Para consultar os dados de produção, execute o seguinte comando no terminal:
```bash
$ curl -X GET "http://127.0.0.1:5000/producao?ano=2000" -H "accept: application/json" -H "Authorization: $TOKEN"   
```
Output:
```json
{
  "dados": [
    {
      "produto": "Bagaceira",
      "quantidade(L)": "12.700"
    },
    {
      "produto": "Base Champenoise champanha",
      "quantidade(L)": "0"
    },
    {
      "produto": "Base Charmat champanha",
      "quantidade(L)": "0"
    },
    {
      "produto": "Base espumante",
      "quantidade(L)": "0"
    },
    {
      "produto": "Base espumante moscatel",
      "quantidade(L)": "0"
    },
    {
      "produto": "Bebida de uva",
      "quantidade(L)": "0"
    },
    {
      "produto": "Borra líquida",
      "quantidade(L)": "9.626.928"
    },
    {
      "produto": "Borra seca",
      "quantidade(L)": "0"
    },
    {
      "produto": "Branco",
      "quantidade(L)": "44.902.276"
    },
    {
      "produto": "Branco",
      "quantidade(L)": "36.955.126"
    },
    {
      "produto": "Brandy",
      "quantidade(L)": "0"
    },
    {
      "produto": "Compostos",
      "quantidade(L)": "0"
    },
    {
      "produto": "DERIVADOS",
      "quantidade(L)": "25.959.016"
    },
    {
      "produto": "Destilado",
      "quantidade(L)": "1.960"
    },
    {
      "produto": "Destilado alcoólico simples de bagaceira ",
      "quantidade(L)": "0"
    },
    {
      "produto": "Espumante",
      "quantidade(L)": "71.410"
    },
    {
      "produto": "Espumante moscatel",
      "quantidade(L)": "0"
    },
    {
      "produto": "Espumante orgânico",
      "quantidade(L)": "0"
    },
    {
      "produto": "Filtrado",
      "quantidade(L)": "0"
    },
    {
      "produto": "Frisante",
      "quantidade(L)": "0"
    },
    {
      "produto": "Jeropiga",
      "quantidade(L)": "0"
    },
    {
      "produto": "Licor de bagaceira",
      "quantidade(L)": "0"
    },
    {
      "produto": "Licorosos",
      "quantidade(L)": "21.000"
    },
    {
      "produto": "Mistelas",
      "quantidade(L)": "33.000"
    },
    {
      "produto": "Mosto concentrado",
      "quantidade(L)": "0"
    },
    {
      "produto": "Mosto de uva com bagaço",
      "quantidade(L)": "0"
    },
    {
      "produto": "Mosto dessulfitado",
      "quantidade(L)": "0"
    },
    {
      "produto": "Mosto parcialmente fermentado ",
      "quantidade(L)": "0"
    },
    {
      "produto": "Mosto simples",
      "quantidade(L)": "16.192.018"
    },
    {
      "produto": "Néctar de uva",
      "quantidade(L)": "0"
    },
    {
      "produto": "Outros derivados",
      "quantidade(L)": "0"
    },
    {
      "produto": "Pisco",
      "quantidade(L)": "0"
    },
    {
      "produto": "Polpa de uva",
      "quantidade(L)": "0"
    },
    {
      "produto": "Rosado",
      "quantidade(L)": "19.880.630"
    },
    {
      "produto": "Rosado",
      "quantidade(L)": "709.000"
    },
    {
      "produto": "SUCO",
      "quantidade(L)": "17.722.779"
    },
    {
      "produto": "Suco de uva adoçado",
      "quantidade(L)": "0"
    },
    {
      "produto": "Suco de uva concentrado",
      "quantidade(L)": "14.176.000"
    },
    {
      "produto": "Suco de uva integral",
      "quantidade(L)": "3.546.779"
    },
    {
      "produto": "Suco de uva orgânico",
      "quantidade(L)": "0"
    },
    {
      "produto": "Suco de uva reconstituído",
      "quantidade(L)": "0"
    },
    {
      "produto": "Tinto",
      "quantidade(L)": "208.242.670"
    },
    {
      "produto": "Tinto",
      "quantidade(L)": "18.545.613"
    },
    {
      "produto": "VINHO DE MESA",
      "quantidade(L)": "273.025.576"
    },
    {
      "produto": "VINHO FINO DE MESA (VINIFERA)",
      "quantidade(L)": "56.209.739"
    },
    {
      "produto": "Vinagre",
      "quantidade(L)": "0"
    },
    {
      "produto": "Vinho Composto",
      "quantidade(L)": "0"
    },
    {
      "produto": "Vinho acidificado ",
      "quantidade(L)": "0"
    },
    {
      "produto": "Vinho leve",
      "quantidade(L)": "0"
    },
    {
      "produto": "Vinho licoroso",
      "quantidade(L)": "0"
    },
    {
      "produto": "Vinho orgânico",
      "quantidade(L)": "0"
    }
  ]
}
```

## Referências
