from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Lead:
    nome: str

    telefone: str

    data: datetime

    campanha: str = ""

    anuncio: str = ""

    mensagem: str = ""