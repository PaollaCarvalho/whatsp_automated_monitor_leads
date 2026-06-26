from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


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

    def obter_naolidas(self):
        """Retorna apenas conversas com mensagens não lidas."""

        chats = self.obter_chats()
        unread = []

        for chat in chats:

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
    
    def ac_abrir_chat_infos(self, chat):
        if chat.find_elements(
                By.CSS_SELECTOR,"span[data-testid='conversation-info-header-chat-title']"):

            self.wait.until(EC.visibility_of(chat))

            ActionChains(self.driver)\
                .move_to_element(chat)\
                .pause(0.3)\
                .click()\
                .perform()
            
            return True