nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
try:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
except ValueError:
    print("Por favor, digite um número válido para a idade.")
