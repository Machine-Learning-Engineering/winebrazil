import pandas as pd

def consultar_producao(ano=None, produto=None, caminho_arquivo='database/producao.csv'):
    try:
        df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')
    except FileNotFoundError:
        return {"erro": "Arquivo de produção não encontrado."}, 404
    except Exception as e:
        return {"erro": f"Erro ao ler o arquivo: {e}"}, 500

    # Filtra pelo produto, se informado (ignorando maiúsculo/minúsculo)
    if produto:
        df = df[df['produto'].str.contains(produto, case=False, na=False)]

    # Remove a coluna 'id' se existir
    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    # Filtra pelo ano, se informado
    if ano:
        ano = str(ano)
        if ano not in df.columns:
            return {"erro": f"Ano {ano} não encontrado no arquivo."}, 404
        colunas = ['produto', ano]
        df = df[colunas]

        # Formata o valor do ano e adiciona o label quantidade(L)
        def formatar_quantidade(valor):
            try:
                return {"quantidade(L)": f"{int(valor):,}".replace(",", ".")}
            except Exception:
                return {"quantidade(L)": str(valor)}

        df["quantidade(L)"] = df[ano].apply(formatar_quantidade).apply(lambda x: x["quantidade(L)"])
        df = df.drop(columns=[ano])

    # Ordena pelo tipo de produto
    df = df.sort_values(by='produto')

    resultado = df.to_dict(orient='records')
    return {"dados": resultado}, 200