# Responsabilidade: armazenar dados de empréstimos

class RepositorioEmprestimo:
    def __init__(self):
        self.emprestimos = []

    def salvar_emprestimo(self, e):
        self.emprestimos.append(e)

    def listar_emprestimos(self):
        return self.emprestimos