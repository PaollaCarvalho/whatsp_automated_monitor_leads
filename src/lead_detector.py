import time
from selenium.webdriver.common.by import By

class LeadDetector:

    @staticmethod

    def is_ctwa(driver):

        anuncios = driver.find_elements(
            By.CSS_SELECTOR,
            "[data-testid='ctwa-agm-preview']"
        )
        return len(anuncios) > 0
