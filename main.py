# Responsabilidade: interface com usuário

from services.servico_emprestimo import ServicoEmprestimo

def main():
    servico = ServicoEmprestimo()

    while True:
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
            break

main()