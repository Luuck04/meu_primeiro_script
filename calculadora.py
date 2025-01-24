num1 = float(input('Digite um numero:\n'))
num2 = float(input('Digite um numero:\n'))

operacao = input('Escolha a operação (+,-,*,/):')

if operacao == '+':
  resultado = num1+num2
elif operacao == '-':
  resultado = num1-num2
elif operacao =='*':
  resultado = num1*num2
elif operacao == '/':
  resultado = num1/num2
  if num2 != 0:
    resultado = num1/num2
  else:
    resultado = 'Erro! Divisão por zero.'
else:
  print('Não foi possível identificar a operação!')

print('O resultado é:',resultado)
