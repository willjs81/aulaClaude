"""
Crie um arquivo exercicio3.py com:

Uma função pedir_nome() que retorna o nome digitado
Uma função pedir_idade() que retorna a idade válida — se inválida, pede novamente em loop até o usuário digitar certo
Uma função exibir_resultado(nome, idade) que imprime a mensagem formatada
Um bloco principal que chama as três funções em sequência


Dica: funções são definidas com def nome_da_funcao(): e retornam valores com return
"""
def pedir_nome():
    nome = input("Digite seu nome: ")
    return nome

def pedir_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            return idade
        except ValueError:
            print("Por favor, digite um número válido para a idade.")

def exibir_resultado(nome, idade):
    print(f"Olá, {nome}! Você tem {idade} anos.")

if __name__ == "__main__":
    nome = pedir_nome()
    idade = pedir_idade()
    exibir_resultado(nome, idade)
    