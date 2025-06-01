import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

def download(url, local_filename):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Lança exceção para códigos de erro HTTP
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        return True, f"Arquivo salvo em {local_filename}"
    except requests.exceptions.RequestException as e:
        return False, f"Erro ao baixar o arquivo: {e}"
    except Exception as e:
        return False, f"Erro inesperado: {e}"
    
def atualizar_dados():
    urls = {
        "comercializacao": os.getenv("COMERCIALIZACAO_URL"),
        "exportacao": os.getenv("EXPORTACAO_URL"),
        "importacao": os.getenv("IMPORTACAO_URL"),
        "processamento": os.getenv("PROCESSAMENTO_URL"),
        "producao": os.getenv("PRODUCAO_URL")
    }

    for key, url in urls.items():
        local_filename = f"database/{key}.csv"
        success, message = download(url, local_filename)
        print(f"{key}: {message}")
    
    return True
