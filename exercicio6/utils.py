"""
Crie dois arquivos:

utils.py — com as funções: pedir_nome(), pedir_idade(), pedir_cidade() cadastrar_pessoa() e salvar_cadastros()
cadastrar_pessoa() faz o loop e retorna a lista.

Adicione uma função salvar_cadastros(cadastros) que salva os dados em um arquivo cadastros.txt
Cada pessoa em uma linha no formato: Nome: X | Idade: X | Cidade: X
No final do programa, chame essa função para salvar os cadastros no arquivo
Dica: use a função open() para criar e escrever no arquivo, e o método write() para adicionar conteúdo. Lembre-se de fechar o arquivo após escrever.
Funções sao declaradas antes de loops e blocos principais, e podem ser chamadas em qualquer parte do código depois de sua definição.

"""
def pedir_nome():
    return input("Digite o nome (ou 'sair' para encerrar): ")
def pedir_idade():
    while True:
        try:
            return int(input("Digite a idade: "))
        except ValueError:
            print("Idade inválida. Por favor, digite um número inteiro.")
def pedir_cidade():
    return input("Digite a cidade: ")
def cadastrar_pessoas():
    pessoas = []
    while True:
        nome = pedir_nome()
        if nome.lower() == "sair":
            break
        idade = pedir_idade()
        cidade = pedir_cidade()
        pessoas.append((nome, idade, cidade))
    return pessoas
def salvar_cadastros(cadastros):
    with open("cadastros.txt", "w") as arquivo:
        for cadastro in cadastros:
            arquivo.write(f"Nome: {cadastro[0]} | Idade: {cadastro[1]} | Cidade: {cadastro[2]}\n")
            
