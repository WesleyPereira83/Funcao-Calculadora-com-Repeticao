#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela.


import sys

def adicao(a,b):
    return(n1+n2)
def subtracao(a,b):
    return(n1-n2)
def multiplicacao(a,b):
    return(n1*n2)
def divisao(a,b):
    return(n1/n2)

def cabecalho():

    print('-' *26)
    print('    CALCULADORA BÁSICA')
    print('-' *26)
    print('''  1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    0. Sair''')
    print('-' *26)

x = 1
while x !=0:
    print(' ')
    cabecalho() 
    x = int(input('\nEscolha uma das opções citadas acima: '))
    if x == 1:
        print(' ')
        print('\nOpção escolhida => SOMA: ')
    elif x == 2:
        print(' ')
        print('\nOpção escolhida => SUBSTRAÇÃO: ')
    elif x == 3:
        print(' ')
        print('\nOpção escolhida => MULTIPLICAÇÃO: ')
    elif x == 4:
        print(' ')
        print('\nOpção escolhida => DIVISÃO: ')
    elif x > 4:
        print(' ')
        print('\nEsta opção não existe. ')
        print(' ')
        cabecalho()
        x = int(input('\nEscolha uma das opções citadas acima: '))
    else:
        x == 0
        print('\nProcesso encerrado. \n')
        exit(0)
  
    n1 = float(input('\nInsira o primeiro número: \n'))
    n2 = float(input('\nInsira o segundo número: \n'))

    if x == 1:
        print(' \n=> Resultado da soma entre ', '(',n1, '+' ,n2,')', 'é', float(adicao(n1, n2)),'.')
    if x == 2:
        print(' \n=> Resultado da subtração entre ', '(',n1, '-' ,n2,')', 'é', float(subtracao(n1, n2)),'.')
    if x == 3:
        print(' \n=> Resultado da multiplicação entre ', '(',n1, '*' ,n2,')', 'é', float(multiplicacao(n1, n2)),'.')
    if x == 4:
        print(' \n=> Resultado da divisão entre ', '(',n1, '/' ,n2,')', 'é', float(divisao(n1, n2)),'.')

