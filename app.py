from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.whatsapp_navegacao import WhatsAppNavigator
from src.lead_detector import LeadDetector


#Você abre o Chrome uma única vez assim:
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
#http://127.0.0.1:9222/json - se abrir json com configs ta ok

options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

navigator = WhatsAppNavigator(driver)

navigator.espera_zap_carregar()

while True:
    unread = navigator.obter_naolidas()

    print(f"{len(unread)} conversas não lidas encontradas.")

    if unread:

        navigator.ac_abrir_chat(unread[0])

        if navigator.verf_chat_aberto():

            if LeadDetector.is_ctwa(driver):

                print(">>> LEAD VINDO DE ANÚNCIO <<<")

            else:

                print("Conversa comum.")

            break
        
    break

