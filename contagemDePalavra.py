def caractere(lista):
    
    frequencia = {}
    
    for palavras in lista:
        
        if palavras in frequencia:
            frequencia[palavras] +=  1 
        else:
            frequencia[palavras] = 1
            
    return frequencia

lista  = ["banana", "maçã", "banana" , "laranja", "maçã", "maçã"]

print(caractere(lista))