from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.models.lead import Lead
from datetime import datetime, timedelta


class ContactExtractor:

    @staticmethod
    def extract(driver):

        wait = WebDriverWait(driver, 10)

        painel = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='chat-info-drawer']")
            )
        )

        telefone = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='contact-info-subtitle selectable-text']")
            )
        ).text

        nome = painel.find_element(
            By.CSS_SELECTOR,
            "[data-testid='selectable-text']"
        ).text

        return Lead(
            nome=nome.replace("~", "").strip(),
            telefone=telefone,
            data= datetime.now())