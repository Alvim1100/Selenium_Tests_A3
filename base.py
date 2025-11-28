from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
        if self.driver: 
            self.driver.quit()

    def digitar_devagar(self,elemt, text):
        for letra in text:
            elemt.send_keys(letra)
            time.sleep(0.05)

    def alertar(self,driver, mensagem):
        try:
            driver.execute_script(f"alert('{mensagem}')")
            wait = WebDriverWait(driver, 5)
            wait.until(EC.alert_is_present())
            alerta = driver.switch_to.alert
            time.sleep(1.5) 
            alerta.accept()
        except: pass

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

    def garantir_url(self, parte_desejada , url):
        if self.driver is None:
                self.garantir_login()

        if parte_desejada not in self.driver.current_url:
            self.driver.get(url)

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

    def verificar_filtro_nome(self, tipo, classificacao):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value(tipo)
        time.sleep(0.5)
        
        elementos = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        lista_do_site = [elem.text for elem in elementos]
        lista_esperada = sorted(lista_do_site, reverse=classificacao)

        if lista_do_site == lista_esperada:
            return True
        else: 
            return False
        
    def verifica_filtro_preco(self,tipo,classificacao):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value(tipo)
        time.sleep(0.5)

        elementos = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    
        lista_numeros = []
        for elem in elementos:
            texto_limpo = elem.text.replace("$", "") # Remove o cifrão
            numero = float(texto_limpo)              # Transforma em número real
            lista_numeros.append(numero)

        lista_esperada = sorted(lista_numeros, reverse=classificacao)

        if lista_numeros == lista_esperada:
            return True
        else: return False

    def executar(self, lista_de_metodos, tipo_teste):
        print(f"><><><><> RODANDO TESTES {tipo_teste} <><><><><")
        self.resultados = []

        for teste in lista_de_metodos:
            descricao = teste.__doc__

            if not descricao:
                descricao = teste.__name__ 
            
            descricao = descricao.strip()
            passou, mensagem = teste()
            icone = "✔" if passou else "✘"

            # Formato: [✔] TP01 - Login Standard: Mensagem do sistema
            linha_final = f"[{icone}] {descricao}: {mensagem}"
            
            print(linha_final)
            self.resultados.append(linha_final)
            time.sleep(0.5)