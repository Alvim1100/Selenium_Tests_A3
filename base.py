from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SauceBase:
    def __init__(self):
        self.resultados = []
        self.driver = None

    def iniciar_driver(self):
            if self.driver is None:
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
            return self.driver
        
    def encerrar(self):
        print("\n--- RELATÓRIO FINAL ---")
        for resultado in self.resultados:
            print(resultado)
        self.driver.quit()

    def digitar_devagar(self,elemt, text):
        for letra in text:
            elemt.send_keys(letra)
            time.sleep(0.05)

    def alertar(self,driver, mensagem):
        driver.execute_script(f"alert('{mensagem}')")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.alert_is_present())
        alerta = driver.switch_to.alert
        time.sleep(3) 
        alerta.accept()

    def preenche_login(self, driver, user_login, user_pass):
        usuario = driver.find_element(By.ID, "user-name")
        self.digitar_devagar(usuario, user_login)
        time.sleep(1)
        senha = driver.find_element(By.ID, "password")
        self.digitar_devagar(senha, user_pass)
        time.sleep(1)

    def preenche_checkout(self, nome, sobrenome, cep):
        self.digitar_devagar(self.driver.find_element(By.ID, "first-name"), nome)
        self.digitar_devagar(self.driver.find_element(By.ID, "last-name"), sobrenome)
        self.digitar_devagar(self.driver.find_element(By.ID, "postal-code"), cep)

    def garantir_login(self):
        if self.driver is None:
            self.iniciar_driver()
        try:
            # Se não estiver no site certo, vai pra lá
            if "saucedemo.com" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com")
            
            # Tenta logar 
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
        except:
            pass

    def garantir_logout(self):
        if "inventory" in self.driver.current_url:
            try:
                self.driver.find_element(By.ID, "react-burger-menu-btn").click()
                time.sleep(1)
                self.driver.find_element(By.ID, "logout_sidebar_link").click()
            except:
                pass

        if "saucedemo.com" not in self.driver.current_url:
            self.driver.get("https://www.saucedemo.com")

    def executar(self, lista_de_metodos, tipo_teste):
        print(f"><><><><> RODANDO TESTES {tipo_teste} <><><><><")
        self.resultados = []

        for teste in lista_de_metodos:
            passou, mensagem = teste()
            icone = "✔" if passou else "✘"
            print(f"{icone} {mensagem}")

            self.resultados.append(f"{icone} {mensagem}")
            time.sleep(0.5)