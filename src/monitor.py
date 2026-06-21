import time
from selenium.webdriver.common.by import By

class WhatsAppMonitor:

    def __init__(self, driver):
        self.driver = driver

    def obter_conversas(self):

        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[data-testid='cell-frame-container']"
        )    

    def buscar_nao_lidas(self):
        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "span[data-testid='icon-unread-count']"
        )    

    def monitorar(self):

        print("Monitor iniciado...")

        while True:

            conversas = self.obter_conversas()
            print(f"Foram encontradas {len(conversas)} conversas.")
            time.sleep(5)

            for conversa in conversas:

                nao_lida = conversa.find_elements(
                    By.CSS_SELECTOR,
                    "span[data-testid='icon-unread-count']"
                )
                if nao_lida:

                    print("Nova conversa encontrada!")

                    nome = conversa.find_element(
                        By.CSS_SELECTOR,
                        "div[data-testid='cell-frame-title']"
                    ).text

                    print(nome)