def soma_na_lista(n, lista):
  for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j and lista[i] + lista[j] == n:
            return True
  return False