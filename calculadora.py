
#Menu Inicial

while True:


  print('Calculadora Digital')
  print('\nOperacoes disponiveis:')
  print('1 - Soma (+):')
  print('2 - Subtracao (-):')
  print('3 - Multiplicacao (*):')
  print('4 - Divisao (/):')
  print('5 - Sair!')

  operacoes = int(input('\nQual operacao deseja realizar? (1 a 5) '))

# chave para sair da calculadora

  if operacoes == 5:
    print('\nObrigado por utilizar a calculadora digital!')
    break
# escolher as oprações

  if operacoes < 1 or operacoes > 5:
    print('\nOperacao invalida! Tente novamente.')
    continue

  else:
    num1 = float(input('\nDigite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))

# calcular as operaçoes

  if operacoes == 1:
    resultado = num1 + num2
    operacao = '+'

  elif operacoes == 2:
    resultado = num1 - num2
    operacao = '-'

  elif operacoes == 3:
    resultado = num1 * num2
    operacao = '*'

  elif operacoes == 4:
    resultado = num1 / num2
    operacao = '/'

  print(f'\nResultado: {num1} {operacao} {num2} = {resultado}')

# menu perguntar se deseja realizar outra operação

  while True:
        retornar = input('\nDeseja realizar outra operacao? (sim ou não): ').lower()
        if retornar == "sim":
            break

        elif retornar == "nao":
            print('\nObrigado por utilizar a calculadora digital!')
            exit()

        else:
            print('\nResposta inválida! Tente novamente.')