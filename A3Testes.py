from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def iniciar_drive():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def digitar_devagar(elemt, text):
    for letra in text:
        elemt.send_keys(letra)
        time.sleep(0.08)

def alertar(driver, mensagem):
    driver.execute_script(f"alert('{mensagem}')")
    wait = WebDriverWait(driver, 5)
    wait.until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    texto_alerta = alerta.text
    print(f"Texto do alerta: {texto_alerta}")
    time.sleep(3) 
    alerta.accept()

def preenche_login(driver, user_login, user_pass):
    usuario = driver.find_element(By.ID, "user-name")
    digitar_devagar(usuario, user_login)
    time.sleep(1)
    senha = driver.find_element(By.ID, "password")
    digitar_devagar(senha, user_pass)
    time.sleep(1)

def executar_testes_positivos():
    driver = iniciar_drive()

    try:
        ### TESTE 01 ###
        driver.get("https://www.saucedemo.com")
        time.sleep(1)
        preenche_login(driver, "standard_user", "secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        if "inventory.html" in driver.current_url:
            alertar(driver, "TESTE 1: Login feito com sucesso!")
            print("TESTE 1: Login feito com sucesso!")
            
        else:
            print("TESTE 1: Login Falhou")

        ### TESTE 02 ###
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        carrinho_simbolo = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        if carrinho_simbolo == "1":
            alertar(driver, "TESTE 2: Adicionado ao carrinho com sucesso!")
            print("TESTE 1 feito com sucesso!")
            
        else:
            print("TESTE 2 Falhou")

        ### TESTE 03 ###



    except Exception as e:
        print(f"Erro na execução: {e}")
    finally:
        driver.quit()

    
def executar_testes_negativos():
    driver = iniciar_drive()

    try:
        #Teste 1 - Login sem usuário
        driver.get("https://www.saucedemo.com")
        time.sleep(1)
        preenche_login(driver, "", "secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        if "Epic sadface: Username is required" in msg: 
            print("Teste 1: Passou!") 
            alertar(driver, "TESTE 1 foi um sucesso!")
        else: 
            print("TESTE 1: Login Falhou")

        #Teste 2 - Login sem senha
        driver.get("https://www.saucedemo.com")
        time.sleep(1)
        preenche_login(driver, "standard_user", "")
        driver.find_element(By.ID, "login-button").click()
        msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        if "Epic sadface: Password is required" in msg: 
            print("Teste 2: Passou!") 
            alertar(driver, "TESTE 2 foi um sucesso!")
        else: 
            print("TESTE 2 Falhou")
        


    except Exception as e:
        print(f"Erro na execução: {e}")
    finally:
        driver.quit()


print("Qual tipo de teste você quer fazer: \n1 - Testes positivos\n2 - Testes negativos\n")
n = int(input())
if n == 1:
    executar_testes_positivos()
elif n == 2:
    executar_testes_negativos()
else: 
    print("Você não digitou corretamente")


