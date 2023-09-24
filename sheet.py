import pandas as pd
import numpy as np



print("Bem-vindo ao sistema!")



# Insert Data

def add_column(df):

    print("")

    name_column = input("Nome da coluna: ")
    print("Inseria os dados na ordem das colunas. Caso contrário, os dados saíram vazios.")
 
def add_line(df):
    # Pega a lista de resposta e insere na linha do DataFrame e returna um dataframe com a nova linha 
    df.loc[len(df.index)+1] = questions(list(df.columns))
    return df


# Questions for insert the data
def questions(list_questions):

    # Função que recebe uma lista de perguntas e retorna uma lista de respostas

    response = []
    for question in list_questions:
        response.append(input(question + ": "))

    return response

def define():    
    try:

        df = pd.read_csv(input("Digite o arquivo e sua localização: "), sep=input("Digite o separador: "))

        print("Exibindo tabela...")
            
        print(df)
        return df

    except:
        print("Um erro ocorreu. Tente novamente.")
        return False



def cshow(df):
    print(df.columns)
    print(df[input("colunm: ").split(",")])

def lshow(df):
    print(df.index)
    print(df.loc[[int(x) for x in input("line: ").split(",") ]])



def options():
    print("* imp - definir dataframe")
    print("* exp - exportar dataframe para csv")
    print("* iline - inserir linha no dataframe")
    # print("* icol - inserir coluna")
    print("* r(colum, line) - mudar um dado em uma determinada coluna e linha")
    print("* show - exibir dataframe")
    print("     * cshow(colum) - exibir determinada coluna")
    print("     * lshow(index) - exibir determinada linha do dataframe ")
    print("* exit - sair do sistema")



def menu():
    system = True
    var = "NOT"
    df = ""

    while(system):
        var = input(">> ")
        try:
            if(var == "imp"):
                df = define()
            elif(var == "iline"):
                df = add_line(df)
            # elif(var == "icol"):
            #     df = add_column(df)
            elif(var == "show"):
                print(df)
            elif(var == "cshow"):
                cshow(df)
            elif(var == "lshow"):
                lshow(df)
            elif(var == "options"):
                options()
            elif(var == "exp"):
                df.to_csv(input("Nome do documento: "), index=False, sep=input("Separador: "))
            elif(var == "exit"):
                system=False
                print("Adeus...")
            else:
                print("Digite novamente")
                options()

        except:
            print("ERRO!")

menu()
