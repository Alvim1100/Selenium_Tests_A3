from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from base import SauceBase  


class TestesPositivos(SauceBase):
    def tp_01(self):
        # Teste 1 - Login com sucesso
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
        # Teste 2 - Adiciona ao carrinho
        try:
            if self.driver is None:
                self.garantir_login()

            if "inventory" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")

            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
            carrinho_simbolo = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            if carrinho_simbolo == "1":
                self.alertar(self.driver, "TESTE 2: Adicionado ao carrinho com sucesso!")
                return(True, "Teste 2 - Sucesso!")
            return (False, "Teste 2 - Falha!")
        except Exception as e:
            return (False,f"Teste 2: Erro {e}")
        
    def tp_03(self):
        # Teste 3 - Remove do carrinho
        try:
            if self.driver is None:
                self.garantir_login()

            if "inventory" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")

            botoes_remover = self.driver.find_elements(By.ID, "remove-sauce-labs-bike-light")
            if len(botoes_remover) > 0:
                botoes_remover[0].click()
            else:
                self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
                time.sleep(0.5)
                self.driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
            
            badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
            if len(badges) == 0:
                self.alertar(self.driver, "TESTE 3: Retirado do carrinho com sucesso!")
                return(True, "Teste 3 - Sucesso!")
            return (False, "Teste 3 - Falha!")
        except Exception as e:
            return (False,f"Teste 3: Erro {e}")
        
    def tp_04(self):
        # Teste 4 - Visualizar carrinho
        try:
            if self.driver is None:
                    self.garantir_login()

            if "inventory" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")

            self.driver.find_element(By.ID, "shopping_cart_container").click()

            if "cart.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 4: Página do carrinho acessada!")
                return(True, "Teste 4 - Sucesso!")
            return (False, "Teste 4 - Falha!")
        except Exception as e:
            return (False,f"Teste 4: Erro {e}")
    
    def tp_05(self):
        # Teste 5 - Clicar em "Checkout" no carrinho.
        try:
            if self.driver is None:
                    self.garantir_login()

            if "cart" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/cart.html")

            badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

            if len(badges) == 0:
                self.driver.find_element(By.ID, "continue-shopping").click()
                time.sleep(0.5)
                self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
                self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

            self.driver.find_element(By.ID, "checkout").click()

            if "checkout-step-one" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 5: Página do checkout acessada!")
                return (True, "Teste 5 - Sucesso!")
            return(False, "Teste 5 - Falha!")
        
        except Exception as e:
            return (False, f"Teste 5 - Erro {e}")
        
    def tp_06(self):
        #Checkout dados

        try:
            if self.driver is None:
                self.garantir_login()

            if "checkout-step-one" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/cart.html")
                self.driver.find_element(By.ID, "checkout").click()

            self.preenche_checkout("Fulano", "Da Silva", "123456")
            self.driver.find_element(By.ID, "continue").click()

            if "checkout-step-two" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 6: Dados aceitos!")
                return (True, "Teste 6 - Sucesso!")
            
            return (False, "Teste 6 - Falha!")

        except Exception as e:
            return (False, f"Teste 6 - Erro {e}")
        
    def tp_07(self):
        # Finaliza a compra

        try:
            if self.driver is None:
                self.garantir_login
            
            if "checkout-step-two" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")
                badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

                if len(badges) == 0:
                    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
                self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
                self.driver.find_element(By.ID, "checkout").click
                self.preenche_checkout("Fulano", "Da Silva", "123456")
                self.driver.find_element(By.ID, "continue").click()
            
            self.driver.find_element(By.ID, "finish").click()

            if "checkout-complete" in self.driver.current_url:
                msg = self.driver.find_element(By.CLASS_NAME, "complete-header").text

                if "Thank you for your order" in msg:
                    self.alertar(self.driver, "TESTE 7: Compra realizada!")
                    return(True, "Teste 7 - Sucesso!")
            return(False, "Teste 7 - Falha!")
        except Exception as e:
            return(False, f"Teste 7 - Erro {e}")
        
    def tp_08(self):
        # Filtro Z-A

        try:
            if self.driver is None:
                self.garantir_login

            if "inventory.html" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")

            select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
            select.select_by_value("za")
            time.sleep(0.5)
            
            elementos = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            lista_do_site = [elem.text for elem in elementos]
            lista_esperada = sorted(lista_do_site, reverse=True)

            if lista_do_site == lista_esperada:
                self.alertar(self.driver, "TESTE 8: Filtro Z-A funcionando!")
                return (True, "Teste 8 - Sucesso!")
            return (False, "Teste 8 - Falha!")
        except Exception as e:
            return (False, f"Teste 8 - Erro {e}")
        
    def tp_09(self):
        # Filtro A - Z

        try:
            if self.driver is None:
                self.garantir_login

            if "inventory.html" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")

            select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
            select.select_by_value("az")
            time.sleep(0.5)
            
            elementos = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            lista_do_site = [elem.text for elem in elementos]
            lista_esperada = sorted(lista_do_site)

            if lista_do_site == lista_esperada:
                self.alertar(self.driver, "TESTE 9: Filtro A-Z funcionando!")
                return (True, "Teste 9 - Sucesso!")
            return (False, "Teste 9 - Falha!")
        except Exception as e:
            return (False, f"Teste 9 - Erro {e}")