import pandas as pd

def consultar_importacao(ano=None, pais=None, caminho_arquivo='database/importacao.csv'):
    try:
        df = pd.read_csv(caminho_arquivo, sep='\t', encoding='utf-8')
    except FileNotFoundError:
        return {"erro": "Arquivo de importação não encontrado."}, 404
    except Exception as e:
        return {"erro": f"Erro ao ler o arquivo: {e}"}, 500

    # Remove a coluna 'id' se existir
    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    coluna_pais = 'País'  
    
    # Filtra pelo país, se informado (ignorando maiúsculo/minúsculo)
    if pais:
        df = df[df[coluna_pais].str.contains(pais, case=False, na=False)]

    # Filtra pelo ano, se informado
    if ano:
        ano = str(ano)
        if ano not in df.columns:
            return {"erro": f"Ano {ano} não encontrado no arquivo."}, 404
        colunas = [coluna_pais, ano]
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

    # Ordena pelo país
    if coluna_pais in df.columns:
        df = df.sort_values(by=coluna_pais)

    # Retorna todos os dados se nenhum filtro for informado
    resultado = df.to_dict(orient='records')
    return {"dados": resultado}, 200