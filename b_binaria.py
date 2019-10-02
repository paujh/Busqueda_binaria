#Busqueda de un elemento en una lista, teniendo como condicional que la lista que nos den YA esta ordenada
def b_binaria(lista,item):
  #Decidi marcar primero un punto igual a 0, reemplazando el ln != 0
  p = 0
  #En la misma variable a meti las dos operaciones (sacar la longitud y restarle 1)
  a = len(lista)-1
  bandera = False
  while p < a and bandera == False:
    #Marcaremos la mitad de nuestra lista
    p_medio = (p + a)//2
    #Primero verificamos que el elemento que se desea buscar, este dentro del rango de nuestra lista ordenada
    if lista[a] < item:
      bandera = True
      return False
    elif lista[p] > item:
      bandera = True
      return False
    #Ahora hacemos la comparacion con el elemento de en medio, el primer elemento y el ultimo para no tener que hacer operaciones extras
    elif lista[p_medio] == item:
      bandera = True
    elif lista[a] == item:
      bandera = True
    elif lista[p] == item:
      bandera = True
    #Si ninguna de las anteriores se cumple, vamos cambiando los valores y decidimos si queremos ir a la mitad izquiera o mitad derecha de nuestra lista, y asi sucesivamente comparando con el elemento de en medio del rango que seleccionemos 
    else:
      if item < lista[p_medio]:
        a = p_medio-1
      else:
        p = p_medio+1
  return bandera

#Ejemplos
#l = [2,4,6,8,10,12,14]
#print(b_binaria(l,3))
#print(b_binaria(l,10))
#print(b_binaria(l,1))
#print(b_binaria(l,8))
#print(b_binaria(l,-1))
#print(b_binaria(l,20))
