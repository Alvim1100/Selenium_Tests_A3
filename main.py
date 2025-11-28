from positivos import TestesPositivos
from negativos import TestesNegativos

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
        run_pos.tp_09
    ]

    lista_negativos = [
        run_neg.tn_01,
        run_neg.tn_02,
        run_neg.tn_03
    ]

    while True:
        print("\n--- MENU ---")
        print("1 - Testes Positivos")
        print("2 - Testes Negativos")
        print("3 - Todos os Testes")
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