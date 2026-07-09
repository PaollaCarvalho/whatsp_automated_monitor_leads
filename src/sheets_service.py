from datetime import datetime, timedelta
from src.models.lead import Lead
import locale

import gspread
from google.oauth2.service_account import Credentials


class SheetsService:

    def __init__(self):

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_file(
            "credentials.json",
            scopes=scopes
        )

        client = gspread.authorize(creds)

        self.planilha = client.open_by_key("1scEHZQn9GVEHQV6HjXc61Vo01yNaKohEUdguMF5cM74")

        self.aba = self.planilha.worksheet("MES 06/2026")

    def buscar_leads_ultima_semana(self) -> list[Lead]:

        linhas = self.aba.get_all_values()

        leads = []

        limite = (datetime.now() - timedelta(days=7))

        # ignoramdo cabeçalho
        for linha in reversed(linhas[3:]):

            data_str = linha[0].strip()

            if not data_str:
                continue

            nome = linha[2]
            telefone = linha[3]

            try:
                data = datetime.strptime(data_str, "%d/%m/%Y")
            except ValueError:
                print(f"Data inválida: {data_str}")
                continue

            if data < limite:
                break

            leads.append(
                Lead(
                    nome=nome,
                    telefone=telefone,
                    data=data
                )
            )

        return leads

    def salvar(self, lead):
        'salva/insere lead na planilha'
        try:
            locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
        except:
            try:
                locale.setlocale(locale.LC_TIME, "Portuguese_Brazil")
            except:
                pass

        agora = datetime.now()

        data = agora.strftime("%d/%m/%Y")
        dia_semana = agora.strftime("%A").lower()

        self.aba.append_row([
            data,
            dia_semana,
            lead.nome,
            lead.telefone
        ])

        print("Lead salvo no Google Sheets!")