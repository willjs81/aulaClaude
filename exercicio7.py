"""
Exercício 7 — Leitura de arquivos

Crie um arquivo exercicio7.py que:

Leia o arquivo cadastros.txt gerado pelo exercício 6
Exiba cada linha formatada no terminal
Conte quantas pessoas estão cadastradas
Se o arquivo não existir, exiba uma mensagem amigável em vez de quebrar o programa


Dicas:

Para ler arquivo use open("cadastros.txt", "r")
Para tratar arquivo inexistente use try/except FileNotFoundError

"""
try:
    with open("cadastros.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())
        print(f"\nTotal de pessoas cadastradas: {len(linhas)}")
except FileNotFoundError:
    print("O arquivo 'cadastros.txt' não foi encontrado.")
    