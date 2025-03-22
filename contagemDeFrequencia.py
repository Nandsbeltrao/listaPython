
def frequencia(lista):
    
    dicionario = {}
    
    for caractere in lista:
        
        if caractere in dicionario:
            dicionario[caractere] += 1 
        else:
            dicionario[caractere] = 1
            
    return dicionario

dicionario = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']

print(frequencia(dicionario))
        
    
    