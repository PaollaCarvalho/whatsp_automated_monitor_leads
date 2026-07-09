from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from src.whatsapp_navegacao import WhatsAppNavigator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

navigator = WhatsAppNavigator(driver)

navigator.espera_zap_carregar()

while True:
    unread = navigator.obter_naolidas()    
    chat = unread[0]
    wait = WebDriverWait(driver, 10)

    spans = chat.find_elements(
    By.CSS_SELECTOR,
    "[data-testid='cell-frame-title'] span"
)

    for span in spans:
        texto = span.text.strip()

        if texto and "mensagem não lida" not in texto.lower():
            print(texto)
            break