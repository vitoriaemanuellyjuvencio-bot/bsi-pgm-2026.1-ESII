import os
import sys

# 1. Configura os caminhos PRIMEIRO (Antes de qualquer import do seu projeto)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_interface_interna = os.path.join(diretorio_atual, 'interface', 'interface')
sys.path.append(pasta_interface_interna)

# 2. Agora que o Python sabe onde procurar, fazemos o import
from services.servico_emprestimo import ServicoEmprestimo


def main():
    repositorio = Repositorio()
    notificador = Notificador()
    
    servico = ServicoEmprestimo(repositorio, notificador)
    
    while True:
        print("\n--- MENU ---")
        print("1 - Registrar")
        print("2 - Listar")
        print("0 - Sair")
        
        op = input("Escolha: ")
        
        if op == "1":
            u = input("Usuário: ")
            eq = input("Equipamento: ")
            servico.registrar(u, eq)
            
        elif op == "2":
            servico.listar()
            
        elif op == "0":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()