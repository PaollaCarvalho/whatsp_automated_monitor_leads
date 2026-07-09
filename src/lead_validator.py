from datetime import datetime, timedelta
from src.models.lead import Lead


class LeadValidator:

    DIAS_VALIDADE = 7

    def __init__(self):
        self.cache = {}

    def carregar_leads_processador(self, leads: list[Lead]):
        'carrega em cache a partir do sheetsservice os leads carregados nos ultimos 7 dias '

        self.cache.clear()

        for lead in leads:

            if lead.telefone:
                self.cache[self._normalizar(lead.telefone)] = lead.data

            if lead.nome:
                self.cache[self._normalizar(lead.nome)] = lead.data

        print(f"{len(self.cache)} identificadores carregados.")

    def new_lead(self, identificador: str) -> bool:
        'é um novo lead? ou está em cache?'

        identificador = self._normalizar(identificador)

        if identificador not in self.cache:
            return True

        ultima_data = self.cache[identificador]

        return datetime.now() - ultima_data >= timedelta(days=self.DIAS_VALIDADE)

    def lead_registrar(self, lead: Lead):
        'registra no cache'

        if lead.telefone:
            self.cache[self._normalizar(lead.telefone)] = lead.data

        if lead.nome:
            self.cache[self._normalizar(lead.nome)] = lead.data

    def _normalizar(self, texto: str) -> str:
        return texto.strip().lower()