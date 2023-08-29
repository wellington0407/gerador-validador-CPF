import os
import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0,9))

def validar (cpf_tratado):
    v1 = 0
    contador = len(cpf_tratado) +1
    for numero in cpf_tratado: 

        v1 += (int(numero) * contador)
        contador -= 1 

    v1 = (v1 * 10) % 11

    v1 =  0  if  v1 > 9 else v1

    return str(v1)

digito1 = validar(cpf)       
digito2 = validar(cpf + digito1) 

print(cpf + digito1 + digito2)
