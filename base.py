from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


class SauceBase:
    def __init__(self):
        self.resultados = []
        self.driver = None

    def iniciar_driver(self):
        if self.driver is None:
            options = Options()

            # --- PREFERÊNCIAS DO USUÁRIO ---
            prefs = {
                # 1. Desliga o Gerenciador de Senhas
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                
                # 2. Desliga o alerta de vazamento de dados
                "profile.password_manager_leak_detection": False,
                
                # 3. Desliga o Safe Browsing
                "safebrowsing.enabled": False,
                "safebrowsing.disable_download_protection": True,
                
                # 4. Bloqueia notificações gerais
                "profile.default_content_setting_values.notifications": 2
            }
            options.add_experimental_option("prefs", prefs)

            # Desativa recursos visuais de segurança
            options.add_argument("--disable-features=PasswordLeakDetection")
            options.add_argument("--disable-save-password-bubble")
            
            # Evita detecção de automação
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("--start-maximized")

            self.driver = webdriver.Chrome(options=options)
            
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
        input_nome = self.driver.find_element(By.ID, "first-name")
        input_sobrenome = self.driver.find_element(By.ID, "last-name")
        input_cep = self.driver.find_element(By.ID, "postal-code")

        input_nome.clear()
        input_sobrenome.clear()
        input_cep.clear()

        self.digitar_devagar(input_nome, nome)
        self.digitar_devagar(input_sobrenome, sobrenome)
        self.digitar_devagar(input_cep, cep)

    def garantir_login(self):
        if self.driver is None:
            self.iniciar_driver()
            
        try:
            if "saucedemo.com" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com")
            if len(self.driver.find_elements(By.ID, "react-burger-menu-btn")) > 0:
                return
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
            self.driver.find_element(By.ID, "login-button").click() 
        except Exception as e:
            print(f"Erro no garantir_login: {e}")

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

    def preparar_tn(self):
        self.iniciar_driver()
        self.garantir_logout()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def preencher_carrinho(self):
        try:
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
            
            if "checkout-step-one" not in self.driver.current_url:    
                self.garantir_url("inventory.html", "https://www.saucedemo.com/inventory.html")

                botoes_remove = self.driver.find_elements(By.ID, "remove-sauce-labs-backpack")
                
                if len(botoes_remove) == 0:
                    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
                
                self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
                
        except Exception as e:
            raise e