notasAlunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}

def media(notas):
    
    mediaAlunos = []
    
    for aluno, notas in notasAlunos.items():
        mediaAluno = sum(notas)/ len(notas)
        mediaAlunos.append((aluno, round(mediaAluno, 2)))
        
    return mediaAlunos

print(media(notasAlunos))
        