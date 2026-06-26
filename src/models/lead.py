from dataclasses import dataclass

@dataclass
class Lead:
    nome: str = ""
    telefone: str = ""
    anuncio: str = ""
    data: str = ""