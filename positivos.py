from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from base import SauceBase  


class TestesPositivos(SauceBase):
    def tp_01(self):
        """TP01 - Login com Sucesso (Standard User)"""
        try:
            self.iniciar_driver()
            self.driver.get("https://www.saucedemo.com")
            self.preenche_login(self.driver, "standard_user", "secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()

            if "inventory.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 1: Login feito com sucesso!")
                return(True, "Teste 1 - Sucesso!")        
            return (False, "Teste 1 - Falha!")
        except Exception as e:
            return (False,f"Teste 1: Erro {e}")
        
    def tp_02(self):
        """TP02 - Adicionar Produto ao Carrinho (Vitrine)"""
        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
            carrinho_simbolo = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            if carrinho_simbolo == "1":
                self.alertar(self.driver, "TESTE 2: Adicionado ao carrinho com sucesso!")
                return(True, "Teste 2 - Sucesso!")
            return (False, "Teste 2 - Falha!")
        except Exception as e:
            return (False,f"Teste 2: Erro {e}")
        
    def tp_03(self):
        """TP03 - Remover Produto do Carrinho (Vitrine)"""
        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

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
        """TP04 - Acessar Página do Carrinho"""
        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            self.driver.find_element(By.ID, "shopping_cart_container").click()

            if "cart.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 4: Página do carrinho acessada!")
                return(True, "Teste 4 - Sucesso!")
            return (False, "Teste 4 - Falha!")
        except Exception as e:
            return (False,f"Teste 4: Erro {e}")
    
    def tp_05(self):
        """TP05 - Iniciar Checkout (Com Itens)"""
        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/cart.html")

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
        """TP06 - Preencher Formulário de Entrega"""
        try:
            if self.driver is None:
                self.garantir_login()

            if "checkout-step-one" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/cart.html")
                badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
                if len(badges) == 0:
                    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
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
        """TP07 - Finalizar Compra com Sucesso"""

        try:
            if self.driver is None:
                self.garantir_login()
            
            if "checkout-step-two" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")
                badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

                if len(badges) == 0:
                    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
                self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
                self.driver.find_element(By.ID, "checkout").click()
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
        """TP08 - Filtro Z-A (Ordem Alfabética Decrescente)"""

        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            resposta = self.verificar_filtro_nome("za", True)

            if resposta == True:
                self.alertar(self.driver, "TESTE 8: Filtro Z-A funcionando!")
                return (True, "Teste 8 - Sucesso!")
            return (False, "Teste 8 - Falha!")
        except Exception as e:
            return (False, f"Teste 8 - Erro {e}")
        
    def tp_09(self):
        """TP09 - Filtro A-Z (Ordem Alfabética Crescente)"""

        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            resposta = self.verificar_filtro_nome("az", False)

            if resposta == True:
                self.alertar(self.driver, "TESTE 9: Filtro A-Z funcionando!")
                return (True, "Teste 9 - Sucesso!")
            return (False, "Teste 9 - Falha!")
        except Exception as e:
            return (False, f"Teste 9 - Erro {e}")
        
    def tp_10(self):
        """TP10 - Filtro Preço (Menor para Maior)"""
        try: 
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            resposta = self.verifica_filtro_preco("lohi",False)

            if resposta == True:
                self.alertar(self.driver, "TESTE 10: Preços ordenados corretamente!")
                return (True, "Teste 10 - Sucesso!")
            return (False, "Teste 10 - Falha!")
        except Exception as e:
            return (False, f"Teste 10 - Erro {e}")
        
    def tp_11(self):
        """TP11 - Filtro Preço (Maior para Menor)"""
        try: 
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            resposta = self.verifica_filtro_preco("hilo",True)

            if resposta == True:
                self.alertar(self.driver, "TESTE 11: Preços ordenados corretamente!")
                return (True, "Teste 11 - Sucesso!")
            return (False, "Teste 11 - Falha!")
        except Exception as e:
            return (False, f"Teste 11 - Erro {e}")
        
    def tp_12(self):
        """TP12 - Verificar Links do Rodapé (Redes Sociais)"""
        try: 
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)

            twitter = self.driver.find_elements(By.CLASS_NAME, "social_twitter")
            facebook = self.driver.find_elements(By.CLASS_NAME, "social_facebook")
            linkedin = self.driver.find_elements(By.CLASS_NAME, "social_linkedin")

            if len(twitter) > 0 and len(facebook) > 0 and len(linkedin) > 0:
                self.alertar(self.driver, "TESTE 12: Ícones do footer visíveis!")
                return (True, "Teste 12 - Sucesso!")
            
            return (False, "Teste 12 - Falha!")
        except Exception as e:
            return(False, f"Teste 12 - Erro {e}")
        
    def tp_13(self):
        """TP13 - Abrir Detalhes do Produto"""
        try: 
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            self.driver.find_element(By.ID, "item_5_img_link").click()

            if "id=5" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 13: Abriu os detalhes do pedido!")
                return (True, "Teste 13 - Sucesso!")
            
            return (False, "Teste 13 - Falha!")
        except Exception as e:
            return(False, f"Teste 13 - Erro {e}")
    
    def tp_14(self):
        """TP14 - Adicionar ao Carrinho via Detalhes"""
        try:
            self.garantir_url("id=5", "https://www.saucedemo.com/inventory-item.html?id=5")
            time.sleep(1)

            botao = self.driver.find_element(By.CLASS_NAME, "btn_inventory")

            if "REMOVE" in botao.text.upper():
                botao.click()
                time.sleep(0.5)
                botao = self.driver.find_element(By.CLASS_NAME, "btn_inventory")

            if "ADD" in botao.text.upper():
                botao.click()
            else:
                return (False, f"Teste 14 - Falha! O botão está com texto estranho: {botao.text}")

            time.sleep(0.5)
            badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

            if len(badges) > 0:
                self.alertar(self.driver, "TESTE 14: Item adicionado com sucesso!")
                return (True, "Teste 14 - Sucesso!")
                
            return (False, "Teste 14 - Falha! Badge não apareceu.")

        except Exception as e:
            return (False, f"Teste 14 - Erro {e}")
        
    def tp_15(self):
        """TP15 - Voltar para Home (Botão Back)"""
        try:
            self.garantir_url("id=5","https://www.saucedemo.com/inventory-item.html?id=5")

            self.driver.find_element(By.ID, "back-to-products").click()

            if "inventory.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 15: Retornou para a home!")
                return (True, "Teste 15 - Sucesso!")
                
            return (False, "Teste 15 - Falha!")
        except Exception as e:
            return(False, f"Teste 15 - Erro {e}")
        
    def tp_16(self):
        """TP16 - Botão Continue Shopping (Carrinho)"""
        try:
            self.garantir_url("inventory.html", "https://www.saucedemo.com/inventory.html")

            self.driver.find_element(By.ID, "shopping_cart_container").click()
            self.driver.find_element(By.ID, "continue-shopping").click()

            if "inventory.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 16: Retornou para a home!")
                return (True, "Teste 16 - Sucesso!")
                    
            return (False, "Teste 16 - Falha!")
        except Exception as e:
            return(False, f"Teste 16 - Erro {e}")
        
    def tp_17(self):
        """TP17 - Cancelar Checkout (Etapa 1 - Dados)"""
        try:
            if self.driver is None:
                self.garantir_login()

            if "checkout-step-one" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/cart.html")
                self.driver.find_element(By.ID, "checkout").click()

            self.driver.find_element(By.ID, "cancel").click()
            time.sleep(0.5)

            if "cart.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 17: Botão Cancelar funcionou!")
                return (True, "Teste 17 - Sucesso!")
            
            return (False, "Teste 17 - Falha!")

        except Exception as e:
            return (False, f"Teste 17 - Erro {e}")
        
    def tp_18(self):
        """TP18 - Cancelar Checkout (Etapa 2 - Resumo)"""
        try:
            if self.driver is None:
                self.garantir_login()

            if "checkout-step-two" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")
                try: 
                    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
                except: 
                    pass
                self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
                self.driver.find_element(By.ID, "checkout").click()
                self.preenche_checkout("Fulano", "Da Silva", "123456")
                self.driver.find_element(By.ID, "continue").click()

            self.driver.find_element(By.ID, "cancel").click()
            time.sleep(0.5)

            if "inventory.html" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 18: Cancelamento no resumo OK!")
                return (True, "Teste 18 - Sucesso!")
            
            return (False, "Teste 18 - Falha!")
        except Exception as e:
            return (False, f"Teste 18 - Erro {e}")
        
    def tp_19(self):
        """TP19 - Reset App State (Limpar Sessão)"""
        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")

            try:
                self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            except:
                pass

            badges_antes = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
            if len(badges_antes) == 0:
                return (False, "Teste 19 - Não conseguiu adicionar item.")
            
            self.driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(1) 
            self.driver.find_element(By.ID, "reset_sidebar_link").click()
            self.driver.find_element(By.ID, "react-burger-cross-btn").click()
            time.sleep(0.5)

            badges_depois = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

            if len(badges_depois) == 0:
                self.alertar(self.driver, "TESTE 19: App Resetado!")
                return (True, "Teste 19 - Sucesso!")
            
            return (False, "Teste 19 - Falha!")

        except Exception as e:
            return (False, f"Teste 19 - Erro {e}")
        
    def tp_20(self):
        """TP20 - Logout do Sistema"""
        try:
            self.garantir_url("inventory.html","https://www.saucedemo.com/inventory.html")
            
            self.driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(1) 
            self.driver.find_element(By.ID, "logout_sidebar_link").click()
            time.sleep(0.5)

            if "https://www.saucedemo.com" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 20 - Logout feito com sucesso!")
                return (True, "Teste 20 - Sucesso!")
            return (False, "Teste 20 - Falha!")
        except Exception as e:
            return (False, f"Teste 20 - Erro {e}")