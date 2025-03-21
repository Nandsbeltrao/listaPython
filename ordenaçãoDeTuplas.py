tuplas = [("Samuel", 25), ("Karynne", 30), ("Carol", 32), ("Kleber", 27), ("Vinicius", 22)]


def listaOrdenada(tuplas):
    return sorted(tuplas, key=lambda x: x[1] , reverse = True)


print(listaOrdenada(tuplas))

