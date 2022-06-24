def arqExiste(nome):
    try:
        a = open(nome,"rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        b = open(nome ,"wt+")
        b.close()
    except:
        print("Houve um erro na criação do documento")
    finally:
        print("Arquivo funcionando perfeitamente")

def lerArquivo(nome):
    try:
        c = open(nome ,"rt")
    except:
        print("\033[1;31mErro nao foi encontrado seu arquivo\033[m")
    else:
        print(c.read())

def arqCadastro(nome):
    try:
        d = open(nome, "at")
        no = str(input("Nome: "))
        id = int(input("Idade: "))
        d.writelines(f"Nome:{no}  - Idade:{id} \n")
    except:
        print("Algo deu errado no seu sistema")
    finally:
        print("Cadastrado com Sucesso")





