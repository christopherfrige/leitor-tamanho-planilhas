import pandas as pd
import os
import time
# Ignora aviso do pandas no terminal (deixar resposta mais limpa)
import warnings
warnings.simplefilter("ignore")

# Diretório da pasta dos arquivos a serem lidos
path = os.getcwd() + "/spreadsheets/"
os.chdir(path)
# Lê o arquivo e retorna qtd de linhas e colunas numa tupla
def ler_planilha(arquivo):
    arquivo_df = pd.read_excel(arquivo)
    return len(arquivo_df.index), len(arquivo_df.columns)

# Inicialização de variáveis de contagem
linhas = 0
colunas = 0
qtdArquivos = 0

# Tempo de início do processamento
timeStart = time.time()

for file in os.listdir():
    dados = ler_planilha(file)

    # É somado +1 devido a primeira linha nao ser contada (reservado para titulo da coluna)
    linhas = linhas + dados[0] + 1

    colunas = colunas + dados[1]

    qtdArquivos += 1

totalTime = time.time()

print("-"*60)
print(f"Foram lidos {qtdArquivos} arquivos, num tempo de processamento de {totalTime - timeStart:.2f}s")
print(f"O total de linhas desses arquivos é {linhas}.")
print(f"O total de colunas desses arquivos é {colunas}.")
print("-"*60)
