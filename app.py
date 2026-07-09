from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.whatsapp_navegacao import WhatsAppNavigator
from src.lead_detector import LeadDetector
from src.sheets_service import SheetsService
from src.lead_extractor import ContactExtractor
from src.lead_validator import LeadValidator


#Você abre o Chrome uma única vez assim:
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
#http://127.0.0.1:9222/json - se abrir json com configs ta ok

options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

navigator = WhatsAppNavigator(driver)

navigator.espera_zap_carregar()

sheets = SheetsService()

leads = sheets.buscar_leads_ultima_semana()

validator = LeadValidator()
validator.carregar_leads_processador(leads)

while True:

    unread = navigator.obter_naolidas()

    if not unread:
        continue

    print(f"{len(unread)} conversas não lidas encontradas.")

    for chat in unread:

        identificador = navigator.obter_nome_chat(chat)

        print(f"Analisando: {identificador}")

        # 1 - Já foi processado?
        if not validator.new_lead(identificador):
            print("Lead já processado recentemente.")
            continue

        print("Novo lead.")

        # 2 - Abre a conversa
        navigator.ac_abrir_chat(chat)

        if not navigator.verf_chat_aberto():
            print("Não foi possível abrir a conversa.")
            continue

        # 3 - É realmente um clique em anúncio?
        if not LeadDetector.is_ctwa(driver):
            print("Conversa comum.")
            continue

        print(">>> LEAD VINDO DE ANÚNCIO <<<")

        # 4 - Extrai informações
        navigator.ac_abrir_info_contato()

        lead = ContactExtractor.extract(driver)

        print(lead)

        # 5 - Salva
        sheets.salvar(lead)

        # 6 - Atualiza cache
        validator.lead_registrar(lead)

        print("Lead processado com sucesso.")
        break