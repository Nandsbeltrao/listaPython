listaNumeros = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

def topFrequentes(listaNumeros):
    
    frequencias = {}
    
    for numero in listaNumeros:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1
            
    listaOrdenada = sorted(frequencias, key= lambda x: (-frequencias[x]))
    
    return listaOrdenada[:3]

print(topFrequentes(listaNumeros))