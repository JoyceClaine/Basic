#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios básicos de cordas
# Preencha o código para as funções abaixo. main () já está configurado
# para chamar as funções com algumas entradas diferentes,
# imprimindo 'OK' quando cada função está correta.
# O código inicial para cada função inclui um 'retorno'
# que é apenas um espaço reservado para o seu código.
# Tudo bem se você não completar todas as funções, e lá
# são algumas funções adicionais para tentar em string2.py.


# A. donuts
# Dada uma contagem int de um número de donuts, retorne uma string
# do formulário "Número de donuts: <count>", em que <count> é o número
# passado. No entanto, se a contagem for 10 ou mais, use a palavra 'muitos'
# em vez da contagem real.
# Então donuts (5) retorna 'Número de donuts: 5'
# e donuts (23) retorna 'Número de donuts: muitos'

def donuts(count):
    if count <= 9:
        return('Number of donuts: {}'.format(count))
    else:
        return('Number of donuts: many')
     


# B. both_ends
# Dada uma string s, retorna uma string feita dos 2 primeiros
# e os últimos 2 caracteres da string original,
# so 'spring' produz 'spng'. No entanto, se o comprimento da string
# é menor que 2, retorna a string vazia.

def both_ends(s):
    if len(s) <= 2:
        return('')
    else:
        a = s[0:2]
        b = s[-2:]
        return (a+b)


# C. fix_start
# Dada uma string s, retorna uma string
# onde todas as ocorrências de seu primeiro caractere
# foi alterado para '*', exceto não altere
# o primeiro char em si.
# por exemplo. 'babble' rende 'ba ** le'
# Suponha que a string tenha o comprimento 1 ou mais.
# Dica: s.replace (stra, strb) retorna uma versão da string s
# onde todas as ocorrências de stra foram substituídas por strb.

def fix_start(s):
    a = s[0]
    b = len(s)
    troca = s.replace(a,'*')
    return (a+troca[1:])


# D. MixUp
# Dado as strings aeb, retorne uma única string com aeb separada
# por um espaço '<a> <b>', exceto trocar os dois primeiros caracteres de cada string.
# por exemplo.
# 'mix', pod '->' pox mid '
# 'dog', 'dinner' -> 'dig donner'
# Suponha que a e b tenham comprimento 2 ou mais.

def mix_up(a, b):
    a1 = b[0:2] + a[2:]
    b1 = a[0:2] + b[2:]
    return a1 + ' ' + b1


# Fornecido função simples de teste () usada em main () para imprimir
# o que cada função retorna versus o que ela deveria retornar.

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Fornecido main () chama as funções acima com entradas interessantes,
# usando test () para verificar se cada resultado está correto ou não.

def main():
  print ('donuts')
  # Cada linha chama donuts, compara seu resultado ao esperado para essa chamada.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print
  print ('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends(''), '')
  test(both_ends('xyz'), 'xyyz')

  
  print
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


  #Standard boilerplate to call the main() function.
 
if __name__ == '__main__':
  main()
