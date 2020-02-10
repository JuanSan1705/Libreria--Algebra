import complejo as com
import math 

def suma_vect(v1,v2):

    if len(v1) == len(v2):
        resul = []
        for i in range(0,len(v1)):
            resul.append(com.suma(v1[i],v2[i]))
        return resul
    else:
        return "El tamaño de los vectores no coincide"

def inverso_aditivo(v1):

    resul = []
    for i in range(0,len(v1)):
        resul.append([v1[i][0]*(-1),v1[i][1]*(-1)])
    return resul

def mul_escalar_vector(e,v1):

    resul = []
    for i in range(0,len(v1)):
        resul.append(com.multiplicacion(e,v1[i]))
    return resul

def suma_matrices(ma1,ma2):

    if (len(ma1) == len(ma2)) and (len(ma1[0])== len(ma2[0])):

        matriz = [] 
        for i in range(0,len(ma1)):
            fila = []
            for j in range (0,len(ma1[0])):
                re = com.suma(m1[i][j],m2[i][j])
                fila.append(re)
            matriz.append(fila)
        return matriz
                
    else:
        return "El tamaño de las matrices no coincide"

def inversa_matriz(ma1):

    resul = []
    for i in range(0,len(ma1)):
        fila = []
        for j in range(0,len(ma1[0])):
            resul =([v1[i][j][0]*(-1),v1[i][j][1]*(-1)])
            fila.append(resul)
        resul.append(fila)
        
    return resul

def mul_escalar_matriz(e,ma1):
    
    resul = []
    for i in range(0,len(ma1)):
        fila = []
        for j in range(0,len(ma1[0])):
            resul = com.multiplicacion(e,m1[i][j])
            fila.append(resul)
        resul.append(fila)
        
    return resul

def transpuesta(ma1):
    
    f,c = len(ma1),len(ma1[0])
    matriz = [[[0,0] for i in range(f)]for j in range (c)]
    for i in range(0,c):
        for j in range(0,f):
            matriz[i][j] = ma1[j][i]
        
    return matriz

def conjugada(ma1):
        
    f,c = len(ma1),len(ma1[0])
    for i in range(0,f):
        for j in range(0,c):
            ma1[i][j] = com.conjugado(ma1[i][j])        
    return ma1

def daga(ma1):

    matriz = transpuesta(conjugada(ma1))
    return matriz

def multiplicacion_mat(ma1,ma2):
 
    fi1,co1 = len(ma1),len(ma1[0])
    fi2,co2 = len(ma2),len(ma2[0])
    
    if co1 == fi2:

        matres = [[[0,0] for i in range(fi1)]for j in range (co2)]
        for i in range (0,fi1):    
            for j in range(0,co2):
                for k in range (0,co1):
                    matres[i][j] = com.suma(matres[i][j],com.multiplicacion(ma1[i][k],ma2[k][j]))
                    print( matres[i][j])
        return matres

    else:
        return "No es posible multiplicar las matrices"

def accion_ma_ve(ma,ve):

    fi1,co1 = len(ma),len(ma[0])
    fi2,co2 = len(ve),len(ve[0])
    
    if co1 == fi2:

        matres = [[[0,0] for i in range(fi1)]for j in range (co2)]
        for i in range (0,fi1):    
            for j in range(0,co2):
                for k in range (0,co1):
                    matres[i][j] = com.suma(matres[i][j],com.multiplicacion(ma[i][k],ve[k][j]))                
        return matres

    else:
        return "No es posible multiplicar las matrices"
    
    return res 

def producto_interno(v,w):
    res = multiplicacion_mat(daga(v),w)
    return res

def norma(v):
    res = producto_interno(v,v)
    ma = math.sqrt(res)
    return ma

def distancia(v,w):
    res = norma(suma_vect(v,inverso_aditivo(w)))
    return res

def hermitania(m1):

    f,c = len(m1),len(m1[0])
    if f == c:
        n = 0
        daga = daga(m1)
        for i in range(0,f):
            for j in range(0,c):
                if daga[i][j] != m1[i][j]:
                    n = 1
                    return False
        if n == 0:
            return True
    else:
        return "La matriz no es cuadrada"

def identidad(num):

    f,c = len(m1),len(m1[0])
    if f == c:
        matres = [[[0,0] for i in range(num)]for j in range (num)]

        for i in range(num):
            for j in range(num):
                if i == j:
                    matres[i][j] = [1,0]
        return matres
    else:
        return "La matriz no es cuadrada"

def unitaria(ma):

    matres = multiplicacion_mat(daga(ma),ma)
    n = len(ma)
    mat_id = identidad(n)
    n = 0

    for i in range(n):
        for j in range(n):
            if matres[i][j] != mat_id[i][j]:
                n = 1
                return False
    if n == 0:
        return True

def pro_tensorial(m1,m2):

    fi1,co1 = len(ma1),len(ma1[0])
    fi2,co2 = len(ma2),len(ma2[0])
    f = fi1*fi2
    c = co1*co2

    matres = [[[0,0] for i in range(f)]for j in range (c)]

    for i in range(0,f):
        for j in range(0,c):
            matres[i][j] = com.multiplicacion(m1[i//fi2][j//co2],m2[i%fi2][j%co2])

    return matres
             

    


    
    
           
                      
    
        
