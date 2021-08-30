import pandas as pd
import os
import time
# Ignora aviso do pandas no terminal (deixar resposta mais limpa)
import warnings
warnings.simplefilter("ignore")

# Diretório da pasta dos arquivos a serem lidos
path = "C:\Programacao\TrackCash\Contagem-Linhas-ML\Reportes"
os.chdir(path)

# Lê o arquivo e retorna qtd de linhas e colunas numa tupla
def ler_planilha(arquivo):
    arquivo_df = pd.read_excel(arquivo)
    return len(arquivo_df.index), len(arquivo_df.columns)

# Inicialização de variáveis de contagem
linhas = 0
qtdArquivos = 0
colunasMenorArquivo = 0
menorArquivo = 0
colunasMedioArquivo = 0
medioArquivo = 0
colunasMaiorArquivo = 0
maiorArquivo = 0

# Tempo de início do processamento
timeStart = time.time()

for file in os.listdir():
    dados = ler_planilha(file)

    linhas = linhas + dados[0]

    if dados[1] == 15:
        colunasMenorArquivo += dados[1]
        menorArquivo += 1
    elif dados[1] == 16:
        colunasMedioArquivo += dados[1]
        medioArquivo += 1
    elif dados[1] == 24:
        colunasMaiorArquivo += dados[1]
        maiorArquivo += 1
    # Caso algum arquivo com número diferente de colunas seja lido
    else:
        print(f"Tamanho novo: {dados[1]}")

    qtdArquivos += 1

totalTime = time.time()

print("-"*60)
print(f"Foram lidos {qtdArquivos} arquivos, num tempo de processamento de {totalTime - timeStart:.2f}s")
print(f"O total de linhas desses arquivos é {linhas}.")
print(f"Há {menorArquivo} arquivos de 15 colunas, havendo {colunasMenorArquivo} colunas!")
print(f"Há {medioArquivo} arquivos de 16 colunas, havendo {colunasMedioArquivo} colunas!")
print(f"Há {maiorArquivo} arquivos de 24 colunas, havendo {colunasMaiorArquivo} colunas!")
print("-"*60)
