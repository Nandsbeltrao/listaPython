list_numeros = [2,4,10,3,9,7,15,22]

def numerosPares(list_numeros):
    pares = []
    
    for numero in list_numeros:
        if numero % 2 == 0:
            pares.append(numero)
       
    return sum(pares)

resultado = numerosPares(list_numeros)
print(f"A soma dos números pares são: {resultado}")

    

