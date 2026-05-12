class RepositorioEmprestimo:

    def buscar_equipamento(self, equip_id):
        ...

    def salvar_emprestimo(self, emprestimo):
        ...

    def marcar_indisponivel(self, equip_id):
        ...

    def buscar_emprestimo(self, emprestimo_id):
        ...

    def marcar_disponivel(self, equip_id):
        ...

    def finalizar_emprestimo(self, emprestimo_id):
        ...

    def buscar_emprestimos(self):
        ...

    # Responsabilidade: armazenar dados de empréstimos

class RepositorioEmprestimo:
    def __init__(self):
        self.emprestimos = []
        self.equipamentos = {
            "notebook": True,
            "projetor": True
        }

    def salvar_emprestimo(self, e):
        self.emprestimos.append(e)

    def listar_emprestimos(self):
        return self.emprestimos