import pandas as pd

def consultar_processamento(ano=None, cultivar=None, caminho_arquivo='database/processamento.csv'):
    try:
        df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')
    except FileNotFoundError:
        return {"erro": "Arquivo de processamento não encontrado."}, 404
    except Exception as e:
        return {"erro": f"Erro ao ler o arquivo: {e}"}, 500

    # Remove a coluna 'id' se existir
    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    # Filtra pela cultivar, se informado (ignorando maiúsculo/minúsculo)
    if cultivar:
        df = df[df['cultivar'].str.contains(cultivar, case=False, na=False)]

    # Filtra pelo ano, se informado
    if ano:
        ano = str(ano)
        if ano not in df.columns:
            return {"erro": f"Ano {ano} não encontrado no arquivo."}, 404
        colunas = ['cultivar', ano]
        df = df[colunas]

        # Formata o valor do ano no padrão 999.999.999 e adiciona o label quantidade(L)
        def formatar_quantidade(valor):
            try:
                if pd.isna(valor) or str(valor).strip() == '' or str(valor) == '-':
                    return '-'
                return f"{int(valor):,}".replace(",", ".")
            except Exception:
                return str(valor)

        df["quantidade(L)"] = df[ano].apply(formatar_quantidade)
        df = df.drop(columns=[ano])

    # Ordena pelo tipo de cultivar
    df = df.sort_values(by='cultivar')

    resultado = df.to_dict(orient='records')
    return {"dados": resultado}, 200