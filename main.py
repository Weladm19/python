from lib.interface import *
from lib.arquivo import *

arq = "teste.txt"
if not arqExiste(arq):
    print("\033[31mCriando um arquivo (Por favor saia do sistema e volte novamente)\033[m")
    criarArq(arq)



linha()
texto("\033[7;36mCadastro\033[m")
linha()
print("\n")

texto('\033[4;37;40mMenu\033[m')
menu(["Pessoas Cadastradas","Cadastra","Sair"])
