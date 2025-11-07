from matematico import *

continuar = ''

while True:
    continuar = str(input('\nDeseja calcular [S/N]? '))
    
    if continuar.lower() == 'n':
        break
    else:
        try:
            operacao = str(input('Qual operação deseja fazer? Digite \n1 para soma\n2 para subtração\n3 para multiplicação\n4 para divisão\n'))

            if operacao == '1':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(soma(num1, num2))
                print('')
            elif operacao == '2':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(sub(num1, num2))
                print('')
            elif operacao == '3':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(mult(num1, num2))
                print('')
            elif operacao == '4':
                num1 = int(input('Digite um número: '))
                num2 = int(input('Digite outro número: '))
                print(div(num1, num2))
                print('')
            else:
                print('\nVocê digitou uma opçaõ inválida, tente novamente.\n')
        except:
            print('Ocorreu algum erro inesperado. Tente novamente.')
    print('\nObrigado por utilizar a calculadora.')