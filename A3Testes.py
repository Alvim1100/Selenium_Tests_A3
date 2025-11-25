from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SauceDemoTestes:
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
            time.sleep(0.08)

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
    
    ### TESTES POSITIVOS ###

    def tp_01(self):
        try:
            self.iniciar_driver()
            self.driver.get("https://www.saucedemo.com")
            time.sleep(0.5)
            self.preenche_login(self.driver, "standard_user", "secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()

            if "inventory.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 1: Login feito com sucesso!")
                return(True, "Teste 1 - Sucesso!")        
            return (False, "Teste 1 - Falha!")
        except Exception as e:
            return (False,f"Teste 1: Erro {e}")
        
    def tp_02(self):
        try:
            if self.driver is None:
                self.garantir_login()

            if "inventory" not in self.driver.current_url:
                self.garantir_login()

            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
            carrinho_simbolo = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            if carrinho_simbolo == "1":
                self.alertar(self.driver, "TESTE 2: Adicionado ao carrinho com sucesso!")
                return(True, "Teste 2 - Sucesso!")
            return (False, "Teste 2 - Falha!")
        except Exception as e:
            return (False,f"Teste 2: Erro {e}")



    ### TESTES NEGATIVOS ###

    def tn_01(self):
        #Teste 1 - Login sem usuario
        try:
            self.iniciar_driver()
            self.garantir_logout()
            self.driver.refresh()
            self.driver.get("https://www.saucedemo.com")
            time.sleep(1)
            self.preenche_login(self.driver, "", "secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            if "Epic sadface: Username is required" in msg: 
                self.alertar(self.driver, "TESTE 1 foi um sucesso!")
                return (True, "Teste 1 - Sucesso!") 
            else: 
                return (False, f"Teste 1 - Falhou")
        except Exception as e:
            return(False, f"Teste 1: Erro {e}")
        
    def tn_02(self):
        #Teste 2 - Login sem senha
        try:    
            self.garantir_logout()
            self.driver.refresh()
            time.sleep(1)
            self.preenche_login(self.driver, "standard_user", "")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            if "Epic sadface: Password is required" in msg: 
                self.alertar(self.driver, "TESTE 2 foi um sucesso!")
                 
            else: 
                return (False, f"Teste 2 - Falhou")
        except Exception as e:
            return (False, f"Teste 2 - Erro {e}")
        
    def tn_03(self):
            #Teste 3 - Login dados invalidos
        try:
            self.garantir_logout()
            self.driver.refresh()
            time.sleep(1)
            self.preenche_login(self.driver, "user", "123")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            if "Epic sadface: Username and password do not match any user in this service" in msg: 
                self.alertar(self.driver, "TESTE 3 foi um sucesso!")
                return(True,"Teste 3 - Sucesso!")
            else: 
                return (False, f"Teste 3 - Falhou")
        except Exception as e:
            return (False, f"Teste 3 - Erro {e}")


    def executar(self, lista_de_metodos, tipo_teste):
        print(f"><><><><> RODANDO TESTES {tipo_teste} <><><><><")
        self.resultados = []

        for teste in lista_de_metodos:
            passou, mensagem = teste()
            icone = "✔" if passou else "✘"
            print(f"{icone} {mensagem}")

            self.resultados.append(f"{icone} {mensagem}")
            time.sleep(0.5)


# MENU #
if __name__ == "__main__":
    teste = SauceDemoTestes()

    lista_positivos = [
        teste.tp_01,
        teste.tp_02
    ]

    lista_negativos = [
        teste.tn_01,
        teste.tn_02,
        teste.tn_03
    ]

    while True:
        print("--- Menu ---\n1 - Testes positivos\n2 - Testes negativos\n 3 - Todos os testes\n 0 - Sair")
        o = int(input())

        if o == 1:
            teste.executar(lista_positivos, "POSITIVOS")
        elif o == 2: 
            teste.executar(lista_negativos, "NEGATIVOS")
        elif o == 3:
            teste.executar(lista_positivos + lista_negativos, "POSITIVOS E NEGATIVOS")
        elif o == 0:
            break
        else:
            print("Opção invalida!")

    


