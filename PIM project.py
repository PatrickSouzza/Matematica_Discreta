print("\033[1;31mEste programa serve para explicar o 'Principio de Indução Finita' ou 'PIF'\033[0;0m")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
loop = True
while loop == True:
    menu = (input("\033[1;31mSe quiser saber sobre a teoria digite 'sobre' se quiser  começar o teste digite 'start' => \033[0;0m"))
    print("----------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------")
    if menu == "sobre":
        print(f"A indução matemática é considerada como uma forma de prova utilizada para demonstrar a verdade de um determinado número infinito de preposições.\nBasicamente esta forma de prova é utilizada para responder a seguinte questão: será tal afirmação verdadeira sempre, ou seja, vale para qualquer número natural?\nExiste um exemplo que geralmente acaba sendo utilizado para este processo que é chamado de efeito dominó. Basta pensar em uma grande fila de dominós em pé.\nSe você conseguir assegurar que o primeiro dominó cairá e sempre que um dominó cair, seu próximo vizinho também cairá, pode concluir que todos os dominós cairão.\n\n ")
    elif menu == "start":
        n = (int(input("\033[1;31mEscolha qualquer numero e o digite aqui => \033[0;0m")))
        print("----------------------------------------------------------------------------------------")
        x = (int(input("\033[1;31mEscolha um numero maior que o anterior e o digite aqui => \033[0;0m")))
        print("----------------------------------------------------------------------------------------")
        for seq in range(n,x):
            print(f"O dominó de numero {seq} caiu. n + {seq}")  
            print("-----------------------------------")
            print("")
        (
            print("\033[1;31mNão importa qual numero de dominó que você escolher, se o (n) dominó escolhido cair o proximo dominó (n+1) sempre irá cair.\nPortanto sempre que algo for usual ao anterior será para seu sucessor. \033[0;0m")
        )
        
        
    else:
        print("\033[1;31mPor favor escolha entre sobre e start.\033[0;0m\n")

    while True:
            voltar_indice = str(input('Deseja retornar ao menu?(s/n)\n'))
            if voltar_indice != 's' and voltar_indice != 'sim' and voltar_indice != 'S' and voltar_indice != 'SIM' and voltar_indice != 'n' and voltar_indice != 'nao' and voltar_indice != 'não' and voltar_indice != 'N' and voltar_indice != 'NAO' and voltar_indice != 'NÃO':
                continue
            elif voltar_indice == 's' or voltar_indice == 'sim' or voltar_indice == 'S' or voltar_indice == 'SIM':
                break
            else:
                loop = False
                break
            continue

