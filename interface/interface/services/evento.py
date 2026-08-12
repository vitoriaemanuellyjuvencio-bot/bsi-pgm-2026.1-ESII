from dataclasses import dataclass
from datetime import date


@dataclass
class Evento:
    tipo: str
    email: str
    data: date | None = None   # Usado no empréstimo
    multa: float | None = None # Usado na devolução