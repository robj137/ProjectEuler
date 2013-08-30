#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import math

lista_primos=[2]

print "Digite o numero\n"

input=raw_input()

numero=int(input) #converte input para inteiro

def ehprimo(lista,numero):
  j=3
  while j<=numero:
    num_divisores=0
    for i in lista:
      if j%i==0:
        num_divisores=num_divisores+1
        break
    if num_divisores==0: 
      lista.append(j)
      #print "Adicionando na lista "
      #print j
    j=j+1
  
  return lista
  
  
lista_primos=ehprimo(lista_primos,numero) 

print lista_primos

soma=0
