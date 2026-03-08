"""
Exercício 5 — Funções + Dicionários + Arquivos
Agora vamos um nível acima. Vamos salvar os cadastros em um arquivo .txt:

Modifique o exercicio4.py ou crie exercicio5.py:

Tudo que já tinha no exercício 4
Adicione uma função salvar_cadastros(cadastros) que salva os dados em um arquivo cadastros.txt
Cada pessoa em uma linha no formato: Nome: X | Idade: X | Cidade: X
No final do programa, chame essa função para salvar os cadastros no arquivo
Dica: use a função open() para criar e escrever no arquivo, e o método write() para adicionar conteúdo. Lembre-se de fechar o arquivo após escrever.

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

def salvar_cadastros(cadastros):
    with open("cadastros.txt", "w") as arquivo:
        for pessoa in cadastros:
            linha = f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Cidade: {pessoa['cidade']}\n"
            arquivo.write(linha)

salvar_cadastros(cadastros)
print("\nCadastros realizados:")
for cadastro in cadastros:
    print(f"Nome: {cadastro['nome']}, Idade: {cadastro['idade']}, Cidade: {cadastro['cidade']}")
print(f"\nTotal de pessoas cadastradas: {len(cadastros)}")
