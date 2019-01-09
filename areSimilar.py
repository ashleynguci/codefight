def areSimilar(a, b):
    lista = []
    listb  =[]
    if a == b:
        return True
    for i in range(len(a)):
            if a[i] != b[i]:
                lista.append(a[i])
                listb.append(b[i])
    if len(lista) >2:
        return False
    elif lista[0]==listb[1]:
        return True
    else:
        return False



                            
    
