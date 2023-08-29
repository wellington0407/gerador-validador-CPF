import os

os.system('cls')

cpf = input('Digite um CPF :')
cpf = cpf.replace('.', '') \
         .replace('-', '')

digito1 = False
digito2 = False

def validar (cpf_tratado):
    v1 = 0
    contador = len(cpf_tratado) +1
    for numero in cpf_tratado: 

        v1 += (int(numero) * contador)
        contador -= 1 

    v1 = (v1 * 10) % 11

    v1 =  0  if  v1 > 9 else v1

    if v1 == int(cpf[len(cpf_tratado):len(cpf_tratado) +1]):
        return True
    else :
        return False


digito1 = validar(cpf[0:9])       
digito2 = validar(cpf[0:10]) 


if (digito1 and digito2):
    print('CPF correto')
else :
    print(f'CPF invalido')