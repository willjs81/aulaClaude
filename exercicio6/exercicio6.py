"""

exercicio6.py — importa as funções do utils.py e executa o programa

"""
from utils import salvar_cadastros, cadastrar_pessoas
if __name__ == "__main__":
    pessoas = cadastrar_pessoas()
    salvar_cadastros(pessoas)
    print(f"\n{len(pessoas)} pessoa(s) cadastrada(s) com sucesso!")
