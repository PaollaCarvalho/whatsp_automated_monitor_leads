from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time


class WhatsAppNavigator:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def espera_zap_carregar(self):
        """Espera o WhatsApp carregar completamente."""
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='cell-frame-container']")
            )
        )

    def obter_chats(self):
        """Retorna todas as conversas visíveis."""
        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[data-testid='cell-frame-container']"
        )
    
    def obter_nome_chat(self, chat):
        'captura apenas nome(ou numero) do lead dentro do conteiner do chat'

        spans = chat.find_elements(
            By.CSS_SELECTOR,
            "[data-testid='cell-frame-title'] span"
        )

        # Método principal
        if len(spans) >= 2:
            return spans[1].text.strip()
        
        # 2° metodo fallback
        for span in spans:

            texto = span.text.strip()

            if texto and "não lida" not in texto.lower():
                print("[Navigator] Fallback utilizado.")
                return texto

        print("[Navigator] Não foi possível identificar o chat.")
        return None

    def obter_naolidas(self):
        """Retorna apenas conversas com mensagens não lidas."""

        chats = self.obter_chats()
        unread = []

        for chat in chats:

            arquivada = bool(
                chat.find_elements(
                    By.CSS_SELECTOR,
                    "[data-testid='archive-refreshed']"
                )
            )

            #ignora arquivada
            if arquivada:
                print("Achei Arquivadas!")
                continue

            if chat.find_elements(
                By.CSS_SELECTOR,
                "span[data-testid='icon-unread-count']"
            ):
                unread.append(chat)

        return unread   
        
    def verf_chat_aberto(self):
        try:

            self.driver.find_element(
                By.TAG_NAME,
                "header"
            )

            return True

        except:

            return False

    def ac_abrir_chat(self, chat):

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            chat
        )

        self.wait.until(
            EC.visibility_of(chat)
        )

        ActionChains(self.driver)\
            .move_to_element(chat)\
            .pause(0.3)\
            .click()\
            .perform()

        print("[Navigator] Conversa aberta.")
        return True
    


    def ac_abrir_info_contato(self):

        header = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "[data-testid='conversation-info-header-chat-title']"
                )
            )
        )

        header.click()