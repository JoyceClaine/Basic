#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Exercício contábil
Classe Python do Google

O main () abaixo já está definido e completo. Chama print_words ()
e print_top () funções que você escreve.

1. Para o sinalizador --count, implemente uma função print_words (filename) que conta
quantas vezes cada palavra aparece no texto e imprime:
word1 count1
word2 count2
...

Imprima a lista acima em ordem classificada por palavra (python classificará pontuação para
vem antes das letras - tudo bem). Guarde todas as palavras em minúsculas
então 'O' e 'o' contam como a mesma palavra.

2. Para o sinalizador --topcount, implemente um print_top (filename) que é semelhante
para print_words (), mas que imprime apenas as 20 palavras mais comuns classificadas
então a palavra mais comum é primeiro, depois a mais comum e assim por diante.

Use str.split () (sem argumentos) para dividir em todos os espaços em branco.

Fluxo de trabalho: não construa o programa inteiro de uma só vez. Obtê-lo para um intermediário
marcar e imprimir sua estrutura de dados e sys.exit (0).
Quando isso estiver funcionando, tente o próximo marco.

Opcional: defina uma função auxiliar para evitar a duplicação de código dentro
print_words () e print_top ().


"""
import sys

def word_count_dict(filename): 
  word_count = {} 
  input_file = open(filename, 'r')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  
  return word_count

def print_words(filename):
  word_count = word_count_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print(word, word_count[word])
    
def get_count(word_count_tuple):
  return word_count_tuple[1]

def print_top(filename):
  word_count = word_count_dict(filename)
  items = sorted(word_count.items(), key=get_count, reverse=True)
  for item in items[:20]:
    print (item[0], item[1])
    
# Defina as funções print_words (filename) e print_top (filename).
# Você poderia escrever uma função de utilidade auxiliar que lê um arquivo
# e cria e retorna uma palavra / conta para ele.
# Então print_words () e print_top () podem apenas chamar a função de utilidade.

###

# Este código de análise de argumento de linha de comando básico é fornecido e
# chama as funções print_words () e print_top () que você deve definir.

def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
