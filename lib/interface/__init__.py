from lib.arquivo import *

def linha(tam = 50):
    print(tam * "-")

def texto(msg):
    print(msg.center(50))

def menu(lista):
    linha()
    while True:
        try:
            contador = 1
            for i in lista:
                print(f"{contador} - {i}")
                contador += 1
            op = int(input("Qual numero deseja: "))
            if op == 1:
                linha()
                texto("\033[1;30;42mConsulta cadastros\033[m\n")
                lerArquivo("teste.txt")
                linha()
                print("\n")
            elif op == 2:
                linha()
                texto("\033[1;30;42mCadastrar\033[m\n")
                arqCadastro("teste.txt")
                linha()
                print("\n")
            elif op == 4:
                linha()
                texto("\033[1;30;42mSair\033[m\n")
                print("\n")
                break
            else:
                print("\n\t\033[1;31m Erro! Por favor seleciona somente numero do menu. \033[m\n")
        except ValueError:
            print("\n \033[1;31mSistemas só aceita numeros\033[m\n")
    linha()