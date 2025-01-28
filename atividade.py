import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAutomationExercise(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configura o driver do Edge e abre o site"""
        edge_driver_path = r"C:\Users\Luiara\Downloads\edgedriver_win64\msedgedriver.exe"
        service = Service(edge_driver_path)
        cls.driver = webdriver.Edge(service=service)
        cls.driver.get("https://automationexercise.com/")
        cls.driver.maximize_window()

    def test_site_accessibility(self):
        """Verifica se o site está acessível verificando o título"""
        driver = self.driver
        self.assertIn("Automation Exercise", driver.title, "O título da página não contém 'Automation Exercise'")

    def test_add_product_to_cart(self):
        """Verifica se um produto pode ser adicionado ao carrinho"""
        driver = self.driver
        try:
            # Espera até o produto ser visível e clica nele
            product = WebDriverWait(driver, 30).until(  # Aumentado o tempo de espera
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product_details/1']"))
            )
            product.click()

            # Espera até o botão de adicionar ao carrinho aparecer
            add_to_cart_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-success')]"))
            )
            add_to_cart_button.click()

            # Espera até o botão de visualização do carrinho aparecer
            cart_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/view_cart']"))
            )
            cart_button.click()

            # Verifica se o carrinho contém o item esperado
            cart_items = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']"))
            )
            self.assertIn("Shopping Cart", cart_items.text, "Carrinho não contém o produto adicionado.")
        
        except TimeoutException:
            self.driver.save_screenshot('add_product_timeout.png')  # Captura de tela em caso de falha
            self.fail("O teste falhou devido ao tempo limite excedido ao adicionar o produto ao carrinho.")

    def test_login_process(self):
        """Verifica o processo de login no site"""
        driver = self.driver
        try:
            # Clica no link de login
            login_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
            )
            login_button.click()

            # Preenche o formulário de login
            email_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys("luiarastream@gmail.com")

            password_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys("123456")

            submit_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )
            submit_button.click()

            # Espera até o nome do usuário aparecer após o login
            account_name = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
            )
            self.assertTrue(account_name.is_displayed(), "Login falhou ou a conta não foi encontrada.")
        
        except TimeoutException:
            self.driver.save_screenshot('login_timeout.png')  # Captura de tela em caso de falha
            self.fail("O teste de login falhou devido ao tempo limite excedido.")

    @classmethod
    def tearDownClass(cls):
        """Fecha o navegador após os testes"""
        if cls.driver:
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
