lista = [1, "Python", [40, 30, 20]]

lista.copy()

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(lista), id(l2))  # [1, "Python", [40, 30, 20]]