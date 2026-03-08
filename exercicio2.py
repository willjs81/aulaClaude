"""
Peça ao usuário para digitar números repetidamente até ele digitar "sair"
Vá somando os números digitados
No final, exiba a soma total e a quantidade de números digitados
Se digitar algo que não seja número nem "sair", exiba "Valor inválido, tente novamente" e continue o loop


Dica: você vai precisar de while, break e continue

Exibir a média dos números digitados
Tratar o caso onde contador == 0 para evitar divisão por zero — nesse caso exiba "Nenhum número foi digitado."
"""
soma = 0
contador = 0
while True:
    entrada = input("Digite um número ou 'sair' para finalizar: ")
    if entrada.lower() == "sair":
        break
    try:
        numero = float(entrada)
        soma += numero
        contador += 1
    except ValueError:
        print("Valor inválido, tente novamente.")
        continue

print(f"Soma total: {soma}")
print(f"Quantidade de números digitados: {contador}")

if contador > 0:
    media = soma / contador
    print(f"Média dos números digitados: {media}")
else:
    print("Nenhum número foi digitado.")

