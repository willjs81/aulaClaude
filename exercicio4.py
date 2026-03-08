"""
Crie exercicio4.py com um sistema de cadastro:

Lista vazia cadastros
Em loop pergunte: nome, idade e cidade
vslidar idade para ser um número inteiro, se inválida, peça novamente
Cada pessoa como um dicionário dentro da lista
Encerra quando digitar "sair" no nome
Exibe todos os cadastros formatados no final
Exibe quantas pessoas foram cadastradas
Dica: use um dicionário para cada pessoa e uma lista para armazenar os cadastros
"""
cadastros = []
while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    while True:
        try:
            idade = int(input("Digite a idade: "))
            break
        except ValueError:
            print("Idade inválida. Por favor, digite um número inteiro.")
    cidade = input("Digite a cidade: ")
    
    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }
    cadastros.append(pessoa)
print("\nCadastros realizados:")
for cadastro in cadastros:
    print(f"Nome: {cadastro['nome']}, Idade: {cadastro['idade']}, Cidade: {cadastro['cidade']}")
print(f"\nTotal de pessoas cadastradas: {len(cadastros)}")
