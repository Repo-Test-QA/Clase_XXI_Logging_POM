from selenium.webdriver.common.by import By

class Dresses:
    def __init__(self, driver):
        self.driver = driver
                
        self.category_name = (By.CLASS_NAME, 'cat-name')

    def get_category_name(self):
        #Voy a devover el texto del elemento localizado
        return self.driver.find_element(*self.category_name).text
