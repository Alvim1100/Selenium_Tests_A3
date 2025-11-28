from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from base import SauceBase


class TestesNegativos(SauceBase):
    def tn_01(self):
        """TN01 - Login sem Usuário"""
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
        """TN02 - Login sem Senha"""
        try:    
            self.garantir_logout()
            self.driver.refresh()
            time.sleep(1)
            self.preenche_login(self.driver, "standard_user", "")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            if "Epic sadface: Password is required" in msg: 
                self.alertar(self.driver, "TESTE 2 foi um sucesso!")
                return(True,"Teste 2 - Sucesso!")
            else: 
                return (False, f"Teste 2 - Falhou")
        except Exception as e:
            return (False, f"Teste 2 - Erro {e}")
        
    def tn_03(self):
        """TN03 - Login com Dados Inválidos"""
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
        

    def tn_04(self):
        """TN04 - Login com Usuário Bloqueado"""
        # ... código ...

    def tn_05(self):
        """TN05 - Login Case Sensitive (Maiúsculas Erradas)"""
        # ... código ...

    def tn_06(self):
        """TN06 - Login com Espaço em Branco Extra"""
        # ... código ...

    def tn_07(self):
        """TN07 - Login Problem User (Imagens Quebradas)"""
        # ... código ...

    def tn_08(self):
        """TN08 - Login Performance User (Tempo Limite)"""
        # ... código ...

    def tn_09(self):
        """TN09 - Acesso Direto URL Restrita (Inventory)"""
        # ... código ...

    def tn_10(self):
        """TN10 - Acesso Direto URL Restrita (Checkout Step 1)"""
        # ... código ...

    def tn_11(self):
        """TN11 - Acesso Direto URL Restrita (Checkout Step 2)"""
        # ... código ...

    def tn_12(self):
        """TN12 - Acesso Direto URL Restrita (Finish)"""
        # ... código ...

    def tn_13(self):
        """TN13 - Acesso a Página Inexistente (404)"""
        # ... código ...

    def tn_14(self):
        """TN14 - Checkout sem Nome"""
        # ... código ...

    def tn_15(self):
        """TN15 - Checkout sem Sobrenome"""
        # ... código ...

    def tn_16(self):
        """TN16 - Checkout sem CEP"""
        # ... código ...

    def tn_17(self):
        """TN17 - Checkout com Injeção de Script (XSS)"""
        # ... código ...

    def tn_18(self):
        """TN18 - Checkout com Nome Gigante (Stress Test)"""
        # ... código ...

    def tn_19(self):
        """TN19 - Remover Item Inexistente via Código"""
        # ... código ...

    def tn_20(self):
        """TN20 - Tentar Checkout com Carrinho Vazio"""