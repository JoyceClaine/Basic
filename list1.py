#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios de lista básica
# Preencha o código para as funções abaixo. main () já está configurado
# para chamar as funções com algumas entradas diferentes,
# imprimindo 'OK' quando cada função está correta.
# O código inicial para cada função inclui um 'retorno'
# que é apenas um espaço reservado para o seu código.
# Tudo bem se você não completar todas as funções, e lá
# são algumas funções adicionais para tentar list2.py.

# A. match_ends
# Dada uma lista de strings, retorne a contagem do número de
# strings em que o comprimento da string é 2 ou mais e o primeiro
# e últimos caracteres da string são os mesmos.
# Nota: python não possui um operador ++, mas + = funciona.

def match_ends(words):
  a = 0
  for x in words:
    if len(x) >= 2 and x[0] == x[-1]:
      a += 1
  return a



# B. front_x
# Dada uma lista de strings, retorne uma lista com as strings
# na ordem classificada, exceto agrupar todas as cadeias que começam com 'x' primeiro.
# por exemplo. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: isso pode ser feito fazendo 2 listas e classificando cada uma delas
# antes de combiná-los.

def front_x(words):
  listaA = []
  listaB = []
  for i in words:
    if i.startswith('x'):
      listaA.append(i)
    else:
      listaB.append(i)
  return sorted(listaA) + sorted(listaB)




# C. sort_last
# Dada uma lista de tuplas não vazias, retorne uma lista classificada em
# ordem pelo último elemento em cada tupla.
# por exemplo. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] rendimentos
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use uma chave personalizada = função para extrair o último elemento de cada tupla.

def last(a):
  return a[-1]
def sort_last(tuples):
  return sorted(tuples, key=last)



# Função de teste simples fornecida () usada em main () para imprimir
# o que cada função retorna versus o que ela deveria retornar.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Chama as funções acima com entradas interessantes.

def main():
  print ('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print ('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print ('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
