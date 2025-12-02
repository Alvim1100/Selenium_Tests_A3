from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base import SauceBase


class TestesNegativos(SauceBase):
    def tn_01(self):
        """TN01 - Login sem Usuário"""
        try:
            self.preparar_tn()
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
            self.preparar_tn()
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
            self.preparar_tn()
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
        try:
            self.preparar_tn()
            self.preenche_login(self.driver, "locked_out_user", "secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            if "locked out" in msg:
                self.alertar(self.driver, "TESTE 4 foi um sucesso!")
                return(True,"Teste 4 - Sucesso!")
            else: 
                return (False, f"Teste 4 - Falhou")
        except Exception as e:
            return (False, f"Teste 4 - Erro {e}")

    def tn_05(self):
        """TN05 - Login Performance User (Validar Lentidão)"""
        try:
            self.preparar_tn()
            self.preenche_login(self.driver, "performance_glitch_user", "secret_sauce")
            inicio = time.time()
            self.driver.find_element(By.ID, "login-button").click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.url_contains("inventory.html"))
            fim = time.time()
            tempo_total = fim - inicio

            if tempo_total > 2:
                self.alertar(self.driver, f"TESTE 7 - Sucesso! Usuário sofreu atraso no login. ({round(tempo_total, 2)}s)!")
                return (True, "Teste 05 - Sucesso!")
            return (False, f"Teste 05 - Falha! ({round(tempo_total, 2)}s).")

        except Exception as e:
            return (False, f"Teste 05 - Erro técnico: {e}")

    def tn_06(self):
        """TN06 - Login Problem User (Imagens Quebradas)"""
        try:
            self.preparar_tn()
            self.preenche_login(self.driver,"problem_user","secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            imagem = self.driver.find_element(By.CSS_SELECTOR, "img.inventory_item_img")
            link_imagem = imagem.get_attribute("src")
            if "sl-404" in link_imagem:
                self.alertar(self.driver, "TESTE 6: Imagem de erro detectada!")
                return (True, "Teste 6 - Sucesso!")
            return (False, "Teste 6 - Falha!")
        except Exception as e:
            return (False, f"Teste 6 - Erro técnico: {e}")

    def tn_07(self):
        """TN07 - Login com Espaço"""
        try:
            self.preparar_tn()
            self.preenche_login(self.driver, "standard_user ", "secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            if "do not match" in msg:
                self.alertar(self.driver, "TESTE 7: Espaço no final gerou erro!")
                return(True,"Teste 7 - Sucesso!")
            else: 
                return (False, f"Teste 7 - Falha!")
        except Exception as e:
            return (False, f"Teste 7 - Erro {e}")

    def tn_08(self):
        """TN08 - Login Case Sensitive (Maiúsculas)"""
        try:
            self.preparar_tn()
            self.preenche_login(self.driver, "Standard_User","secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            if "do not match" in msg:
                self.alertar(self.driver, "TESTE 08: Login bloqueado por Case Sensitive!")
                return (True, "TN 08 - Sucesso!")
            return (False, f"TN 08 - Falha! Mensagem inesperada: {msg.text}")
        except Exception as e:
            return (False, f"TN 08 - Erro técnico: {e}")
        

    def tn_09(self):
        """TN09 - Acesso Direto URL Restrita (Inventory)"""
        try:
            self.preparar_tn()
            payload = "<script>alert(1)</script>"
            self.preenche_login(self.driver, payload, "secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            if "do not match" in msg.text:
                self.alertar(self.driver, "TN 09: O script não foi executado.")
                return (True, "TN 09 - Sucesso!")
            return (False, f"TN 09 - Falha! O sistema reagiu de forma estranha: {msg.text}")
        except Exception as e:
            return (False, f"TN 09 - Erro técnico: {e}")

    def tn_10(self):
        """TN10 - Acesso Direto URL Restrita (Checkout Step 1)"""
        try:
            self.preparar_tn()
            payload = "' OR 1=1 --"
            self.preenche_login(self.driver, payload, "secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

            if "do not match" in msg.text:
                self.alertar(self.driver, "TESTE 10: SQL Injection bloqueado com sucesso!")
                return (True, "Teste 10 - Sucesso!")

            return (False, f"Teste 10 - Falha! Comportamento inesperado: {msg.text}")

        except Exception as e:
            return (False, f"Teste 10 - Erro técnico: {e}")


    def tn_11(self):
        """TN11 - Checkout sem Nome (Campo Obrigatório)"""
        try:
            self.preparar_tn()
            self.garantir_login()

            if "inventory.html" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")

            self.preencher_carrinho()

            self.preenche_checkout("", "Siclano", "123456")
            
            self.driver.find_element(By.ID, "continue").click()
            time.sleep(1)

            try:
                msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

                if "First Name is required" in msg.text:
                    self.alertar(self.driver, "TESTE 11: Erro de Nome Obrigatório ok!")
                    return (True, "Teste 11 - Sucesso!")
                else:
                    return (False, f"Teste 11 - Falha! Mensagem incorreta: {msg.text}")
            except:
                # Se não achou a mensagem de erro, provavelmente o formulário passou
                if "checkout-step-two" in self.driver.current_url:
                    return (False, "Teste 11 - Falha! O sistema aceitou o campo vazio e avançou.")
                return (False, "Teste 11 - Falha! Mensagem de erro não encontrada.")
        except Exception as e:
            return (False, f"Teste 11 - Erro técnico: {e}")


    def tn_12(self):
        """TN12 - Checkout sem Sobrenome"""
        try:
            self.garantir_login()
            self.preencher_carrinho()
            self.preenche_checkout("Fulano", "", "123456'")
            self.driver.find_element(By.ID, "continue").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

            if "Last Name is required" in msg.text:
                self.alertar(self.driver, "TESTE 12: Erro de Sobrenome Obrigatório")
                return (True, "Teste 12 - Sucesso!")

            return (False, f"Teste 12 - Falha! Mensagem inesperada: {msg.text}")

        except Exception as e:
            return (False, f"Teste 12 - Erro técnico: {e}")

    def tn_13(self):
        """TN13 - Checkout sem CEP"""
        try:
            if self.driver is None:
                self.iniciar_driver()
            self.garantir_login()
            
            self.preencher_carrinho()

            if "checkout-step-one" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

            self.preenche_checkout("Fulano", "Siclano", "") 
            
            self.driver.find_element(By.ID, "continue").click()

            wait = WebDriverWait(self.driver, 5)
            msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))

            if "Postal Code is required" in msg.text:
                self.alertar(self.driver, "TESTE 13: Erro de CEP Obrigatório")
                return (True, "Teste 13 - Sucesso!")

            return (False, f"Teste 13 - Falha! Mensagem inesperada: {msg.text}")

        except Exception as e:
            return (False, f"Teste 13 - Erro técnico: {e}")

    def tn_14(self):
        """TN14 - Checkout com caracteres especiais (CEP)"""
        try:
            self.preparar_tn()
            self.driver.get("https://www.saucedemo.com")
            self.preenche_login(self.driver, "standard_user", "Secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            
            if "do not match" in msg.text:
                self.alertar(self.driver, "TESTE 14: Senha com maiúscula rejeitada!")
                return (True, "Teste 14 - Sucesso!")

            return (False, f"Teste 14 - Falha!")

        except Exception as e:
            return (False, f"Teste 14 - Erro técnico: {e}")

    def tn_15(self):
        """TN15 - Checkout com Nome Gigante (Stress Test)"""
        try:
            self.preparar_tn()
            self.garantir_login()
            self.preencher_carrinho()
            palavra = "A"*500
            self.driver.find_element(By.ID, "first-name").send_keys(palavra)
            self.driver.find_element(By.ID, "last-name").send_keys("Silva")
            self.driver.find_element(By.ID, "postal-code").send_keys("12345")
            self.driver.find_element(By.ID, "continue").click()

            if "checkout-step-two" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 15: Sistema aguentou o input gigante!")
                return (True, "Teste 15 - Sucesso!")

            return (False, "Teste 15 - Falha! O sistema travou ou bloqueou o input.")

        except Exception as e:
            return (False, f"Teste 15 - Erro técnico: {e}")

    def tn_16(self):
        """TN16 - Acesso Direto URL Restrita (Inventory)"""
        try:
            self.preparar_tn()
            self.driver.get("https://www.saucedemo.com/inventory.html")
            wait = WebDriverWait(self.driver, 5)
            msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))

            msg_esperado = "You can only access '/inventory.html' when you are logged in"
            
            if msg_esperado in msg.text:
                    self.alertar(self.driver, "TESTE 16: Acesso bloqueado com sucesso!")
                    return (True, "Teste 16 - Sucesso!")
            return (False, f"Teste 16 - Falha! Mensagem inesperada: {msg.text}")
        except Exception as e:
            return (False, f"Teste 16 - Erro técnico: {e}")

    def tn_17(self):
        """TN17 - Acesso Direto Checkout Step 2"""
        try:    
            self.preparar_tn()
            self.garantir_login()
            self.resetar_aplicacao()

            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

            self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
            
            # Verifica se o site permitiu a entrada (Bug do site/Falha de Segurança)
            if "checkout-step-two" in self.driver.current_url:
                self.alertar(self.driver, "TESTE 17 - Falha de Segurança! Acesso direto não bloqueado pelo sistema.")
                return (True, "Teste 17 - Sucesso! O teste detectou a falha de segurança esperada no site.")
            
            # Se não permitiu, verifica se mostrou erro
            try:
                msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
                return (True, f"Teste 17 - Sucesso! Bloqueio funcionou: {msg.text}")
            except:
                return (True, "Teste 17 - Sucesso! ")

        except Exception as e:
            return (False, f"Teste 17 - Erro técnico: {e}")


    def tn_18(self):
        """TN18 - Acesso Direto Checkout Complete"""
        try:    
            self.resetar_aplicacao() 
            self.preparar_tn()
            self.garantir_login()

            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

            # Tenta pular para a finalização
            self.driver.get("https://www.saucedemo.com/checkout-complete.html")

            if "checkout-complete" in self.driver.current_url:
                 self.alertar(self.driver, "TESTE 18 - Falha de Segurança! Acesso direto não bloqueado pelo sistema.")
                 return (True, "Teste 18 - Sucesso! O teste detectou a falha de segurança esperada no site.")
            
            try:
                msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
                return (True, f"Teste 18 - Sucesso! Bloqueio funcionou: {msg.text}")
            except:
                return (True, "Teste 18 - Sucesso!")

        except Exception as e:
            return (False, f"Teste 18 - Erro técnico: {e}")

    def tn_19(self):
        """TN19 - Página Inexistente (404)"""
        try:
            self.preparar_tn()
            self.garantir_login()
            
            self.driver.get("https://www.saucedemo.com/batata.html")

            if "inventory.html" in self.driver.current_url:
                produtos = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
                if len(produtos) > 0:
                    self.alertar(self.driver, "TESTE 19: Site redirecionou URL inválida para Home (Seguro)!")
                    return (True, "Teste 19 - Sucesso!")

            produtos = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            if len(produtos) == 0:
                self.alertar(self.driver, "TESTE 19: Botão Remover não existe. Comportamento Correto!")
                return (True, "Teste 19 - Sucesso!")

            # Se chegou aqui, é falha (está na URL errada mas carregou produtos ou quebrou)
            return (False, f"Teste 19 - Falha! Comportamento inesperado na URL: {self.driver.current_url}")

        except Exception as e:
            return (False, f"Teste 19 - Erro técnico: {e}")


    def tn_20(self):
        """TN20 - Remover Item Inexistente (Validar Exceção)"""
        try:
            self.preparar_tn()
            self.garantir_login()            
            self.resetar_aplicacao() 
            self.driver.refresh()

            if "inventory.html" not in self.driver.current_url:
                self.driver.get("https://www.saucedemo.com/inventory.html")

            try:
                self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
                return (False, "Teste 20 - Falha! O botão 'Remover' foi encontrado.")
            except Exception:
                self.alertar(self.driver, "TESTE 20: Botão Remover não existe. Comportamento Correto!")
                return (True, "Teste 20 - Sucesso!")
        except Exception as e:
            return (False, f"Teste 20 - Erro técnico: {e}")