list_numeros = [2,4,10,3,9,7,15,22]

def numerosPares(list_numeros):
    pares = []
    
    for numero in list_numeros:
        if numero % 2 == 0:
            pares.append(numero)

    print("A soma dos números pares são:", sum(pares))
    
numerosPares(list_numeros)

    

