from dataclasses import dataclass
from datetime import date

@dataclass
class Emprestimo:
    id: int
    equip_id: int
    nome: str
    email: str
    data_emprestimo: date
    data_devolucao: date
    devolvido: bool