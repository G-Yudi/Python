import pandas as pd #Lê arquivos do excel
import time #Para adquirir a data e a hora atuais
from pathlib import Path #Criar novos arquivos

# Declarando a lista de itens
Itens = list()

# Definindo o local do arquivo e lendo o conteúdo
arquivo=("C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Python\\Python\\Tabajara.xlsx")
dado=pd.read_excel(arquivo)

# Função que gera um cupom fiscal em .txt
def Cupom_Fiscal():
    # Função para definir o preço que será pago
    def Preco():
        if Quant > 5:
            Preco_Maior = dado.loc[dado['Tipo']==Carne, 'Acima de 5 Kg'].values[0] #Localiza somente o valor, por causa do .values[0], na linha da Carne e coluna 'Acima de 5 Kg'
            Total = Preco_Maior*Quant
            Desconto = 0
            if Payment == 'Sim':
                Desconto = 0.05*Preco_Maior*Quant

            Preco_Final = Total - Desconto

        else:
            Preco_Menor = dado.loc[dado['Tipo']==Carne, 'Até 5 Kg'].values[0]
            Total = Preco_Menor*Quant
            Desconto = 0
            if Payment == 'Sim':
                Desconto = 0.05*Preco_Menor*Quant

            Preco_Final = Total - Desconto
        return Total, Desconto, Preco_Final

    Total, Desconto, Preco_Final = Preco()
    #Emite a data e hora atual
    Tempo = time.strftime('%Y_%m_%d %H.%M.%S', time.localtime())
    
    #Cria um .txt em um determinado diretório
    Caminho = Path(f'C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Python\\Python\\Cupom Fiscal\\{Tempo}.txt') #caminho do arquivo
    Caminho.touch()
    
    #Abre o arquivo para escrita no final deste
    Abrindo = open(Caminho,'a')
    
    Itens.append('Tipo de carne: %s' %Carne)
    Itens.append('\nQuantidade: %.2f kg' %Quant)
    Itens.append('\nTotal: R$ %.2f' %Total)
    Itens.append('\nTipo de pagamento: %s' %Payment)
    Itens.append('\nDesconto: R$ %.2f' %Desconto)
    Itens.append('\nPreço a pagar: R$ %.2f' %Preco_Final)

    Abrindo.writelines(Itens) #Escreve todos os itens acima no .txt
    
    return print("Cupom gerado com sucesso!")

while(True):
    # Definindo o tipo de carne que deseja
    print(dado)
    Carne = input("Qual a carne deseja?\n").capitalize() #Capitalize = Upper case the first letter
    
    # Verifica se todos os dados inseridos estão corretos
    if (dado['Tipo'] == Carne).any(): #Verifica se tem algo na coluna 'Lista' digitado no input Carne
        Quant = float(input("Quantos kg deseja?\n"))
        Payment = input("Deseja pagar com o Cartão Tabajara? (Sim/Não)\n").capitalize()

        if Quant > 0:
            Cupom_Fiscal()
            break

        else:
            print ("Por favor, insira a quantidade correta ou o método de pagamento.")
    
    else:
        print("Coloque uma carne que está na lista, por favor.")
