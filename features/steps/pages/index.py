from selenium.webdriver.common.by import By

#En nuestra página index, vamos a mapear los elementos con los cuales
#vamos a interactuar, en nuestro caso en la página principal
#vamos a hacer click sobre el enlace DRESSES, el cual se encuentra
#como segunda opción en el menu.
class Index:
    def __init__(self, driver):
        self.driver = driver
        self.dresses_button = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')

        self.search_bar = (By.ID, 'search_query_top')
        self.search_button = (By.NAME, 'submit_search')

    def click_dresses(self):
        self.driver.find_element(*self.dresses_button).click()

    def search(self, item):
        self.driver.find_element(*self.search_bar).send_keys(item)
        self.driver.find_element(*self.search_button).click()
