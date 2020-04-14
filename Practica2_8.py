def crearDiccionario():
    lista = list(conjunto)
    for i in range(len(lista)):
        lista[i] = (lista[i],0)
    dic = dict(lista)
    return dic

def completarDiccionario(dic):
    for i in range(len(palabra)):
        print('i=',i)
        for e in dic:
            print('e=',e)
            if (palabra[i] == e):
                dic[e] = dic[e] + 1
    return dic

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def Imprimir(dic):
    for i in dic:
        if (es_primo(dic[i]) == True):
            print('La letra',i,'aparece un total de',dic[i],'veces, por lo tanto,es primo')
        else:
            print('La letra',i,'aparece un total de',dic[i],'veces, por lo tanto NO es primo')


palabra = input('Ingresa una palabra\n')
#palabra = 'adivina'
conjunto = set(palabra)
dic = crearDiccionario()
dic = completarDiccionario(dic)
Imprimir(dic)
input()
