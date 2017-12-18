# Cristina Consolación Martínez Ortega

#Funciones en python:



#Suma de una lista:

def suma(l):
    acum=0
    for x in l:
        acum+=x
    return acum

#Suma de cuadrados de una lista:

def sum(x,y):
    return x+y


#Maximo de una lista:

def maximo(l):
    max_val=-float("inf")
    for x in l:
        if x>max_val:
            max_val=x
    return max_val

# Multiplicacion de escalar por una matriz:

def prod_map(x,l):
    res=[]
    for n in l:
        res.append(x*n)
    return res








 

