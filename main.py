from positivos import TestesPositivos
from negativos import TestesNegativos
from colorama import init, Fore, Style
init(autoreset=True)

def menu():
    run_pos = TestesPositivos()
    run_neg = TestesNegativos()

    # MONTAMOS AS LISTAS DE EXECUÇÃO
    lista_positivos = [
        run_pos.tp_01,
        run_pos.tp_02,
        run_pos.tp_03,
        run_pos.tp_04,
        run_pos.tp_05,
        run_pos.tp_06,
        run_pos.tp_07,
        run_pos.tp_08,
        run_pos.tp_09,
        run_pos.tp_10,
        run_pos.tp_11,
        run_pos.tp_12,
        run_pos.tp_13,
        run_pos.tp_14,
        run_pos.tp_15,
        run_pos.tp_16,
        run_pos.tp_17,
        run_pos.tp_18,
        run_pos.tp_19,
        run_pos.tp_20
    ]

    lista_negativos = [
        run_neg.tn_01,
        run_neg.tn_02,
        run_neg.tn_03,
        run_neg.tn_04,
        run_neg.tn_05,
        run_neg.tn_06,
        run_neg.tn_07,
        run_neg.tn_08,
        run_neg.tn_09,
        run_neg.tn_10,
        run_neg.tn_11,
        run_neg.tn_12,
        run_neg.tn_13,
        run_neg.tn_14,
        run_neg.tn_15,
        run_neg.tn_16,
        run_neg.tn_17,
        run_neg.tn_18,
        run_neg.tn_19,
        run_neg.tn_20
    ]

    while True:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}--- MENU PRINCIPAL ---{Style.RESET_ALL}")
        print("1 - Testes Positivos")
        print("2 - Testes Negativos")
        print("3 - Todos os Testes")
        print("4 - Testes Rápidos Positivos")
        print("5 - Testes Rápidos Negativos")
        print("6 - Testes Rápidos Todos")
        print("0 - Sair")
        
        try:
            o = int(input("Opção: "))
            
            if o == 1:
                run_pos.executar(lista_positivos, "POSITIVOS")
            elif o == 2:
                run_neg.executar(lista_negativos, "NEGATIVOS")
            elif o == 3:
                run_pos.executar(lista_positivos, "BATERIA POSITIVA")
                run_neg.executar(lista_negativos, "BATERIA NEGATIVA")
            elif o == 4:             
                if run_pos.driver: run_pos.driver.quit(); run_pos.driver = None
                if run_neg.driver: run_neg.driver.quit(); run_neg.driver = None
                run_pos.headless = True 
                run_pos.executar(lista_positivos, "POSITIVOS RÁPIDOS")
                run_pos.headless = False
            elif o == 5:      
                if run_pos.driver: run_pos.driver.quit(); run_pos.driver = None
                if run_neg.driver: run_neg.driver.quit(); run_neg.driver = None       
                run_neg.headless = True  
                run_neg.executar(lista_negativos, "NEGATIVOS RÁPIDOS")
                run_neg.headless = False
            elif o == 6:  
                if run_pos.driver: run_pos.driver.quit(); run_pos.driver = None
                if run_neg.driver: run_neg.driver.quit(); run_neg.driver = None           
                run_pos.headless = True 
                run_neg.headless = True 
                run_pos.executar(lista_positivos, "BATERIA POSITIVA")
                run_neg.driver = run_pos.driver 
                run_neg.executar(lista_negativos, "BATERIA NEGATIVA")
                run_pos.headless = False
                run_neg.headless = False
            elif o == 0:
                run_pos.encerrar()
                run_neg.encerrar()
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite apenas números.")


if __name__ == "__main__":
    menu()