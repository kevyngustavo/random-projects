import pandas as pd
import numpy as np



print("Bem-vindo ao sistema!")








def questions(list_questions):

    # Função que recebe uma lista de perguntas e retorna uma lista de respostas

    response = []
    for question in list_questions:
        response.append(input(question + ": "))

    return response

def add_line(df):
    
    # Pega a lista de resposta e insere na linha do DataFrame e returna um dataframe com a nova linha 
    df.loc[len(df.index)+1] = questions(list(df.columns))
    return df


def define():
    
    try:

        df = pd.read_csv(input("Digite o arquivo e sua localização: "), sep=input("Digite o separador: "))

        print("Exibindo tabela...")
            
        print(df)
        return df

    except:
        print("Um erro ocorreu. Tente novamente.")
        return False

def show(df):
    df.display()

def menu():
    system = True
    var = "NOT"
    df = ""
    options()
    while(system):
        var = input(">> ")
        if(var == "imp"):
            df = define()
        elif(var == "insert"):
            df = add_line(df)
        elif(var == "show"):
            print(df)
        elif(var == "exp"):
            df.to_csv(input("Nome do documento: "), index=False, sep=input("Separador: "))
        elif(var == "exit"):
            system=False
            print("Adeus...")
        else:
            print("Digite novamente")

def options():
    print("imp - definir dataframe")
    print("insert - inserir linha no dataframe")
    print("show - exibir dataframe")
    print("exp - exportar dataframe para csv")
    print("exit - sair do sistema")

menu()
