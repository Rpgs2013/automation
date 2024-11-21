class Locator:
    def __init__(self, driver: WebDriver):
        self.web = driver
    
    def get_element_by_text(self, text: str):
        xpath = f'//*[contains(text(), "¨{text}")]'
        element = self.web.find_element(By.XPATH, xpath)
        return element
    
    def get_element_by_matching_text(self, text: str):
        xpath = f'//*[text(), "{text}")]'
        element = self.web.find_element(By.XPATH, xpath)
        return element