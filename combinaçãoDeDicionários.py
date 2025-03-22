d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}

def combinação(d1, d2):
    resultado = {}
    
    for chave, valor in d1.items():
        resultado[chave] = valor
    
    
    for chave, valor in d2.items():
        if chave in resultado:
            resultado[chave] += valor  
        else:
            resultado[chave] = valor  
    
    return resultado


print(combinação(d1,d2))