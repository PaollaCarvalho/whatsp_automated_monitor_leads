from selenium.webdriver.common.by import By


class LeadExtractor:

    @staticmethod
    def get_name(driver):

        elemento = driver.find_element(
            By.CSS_SELECTOR,
            "header span[dir='auto']"
        )

        return elemento.text