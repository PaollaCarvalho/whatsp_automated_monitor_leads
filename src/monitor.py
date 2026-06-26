import time
from selenium.webdriver.common.by import By
from src.lead_detector import LeadDetector
from src.lead_extractor import LeadExtractor

class WhatsAppMonitor:

    def __init__(self, driver):
        self.driver = driver
   

    def monitorar(self):

        print("Monitor iniciado...")

        while True:

            conversas = self.obter_conversas()

            for conversa in conversas:

                nao_lida = conversa.find_elements(
                    By.CSS_SELECTOR,
                    "span[data-testid='icon-unread-count']"
                )

                if not nao_lida:
                    continue

                print("Nova conversa!")

                #conversa.click()
                print(conversa.text)
                break

                time.sleep(2)

                if LeadDetector.is_ctwa(self.driver):

                    print(">>> LEAD VINDO DE ANÚNCIO <<<")

                else:

                    print("Conversa comum.")

            time.sleep(5)