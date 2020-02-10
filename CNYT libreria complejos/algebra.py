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
    print(res)
    ma = math.sqrt(res)
    return ma

def distancia(v,w):
    res = norma(suma_vect(v,inverso_aditivo(w)))
    return res

def hermitania(m1):

    f,c = len(m1),len(m1[0])
    if f == c:
        daga = daga(m1)
        for i in range(0,f):
            for j in range(0,c):
                if daga[i][j] != m1[i][j]:
                    return False
                    break
         
                    

    else:
        return "La matriz no es cuadrada"

def identidad(n):
     
def unitaria(m1):

    f,c = len(m1),len(m1[0])

def pro_tensorial(m1,m2):

    fi1,co1 = len(ma1),len(ma1[0])
    fi2,co2 = len(ma2),len(ma2[0])

    matres = [[[0,0] for i in range(fi1*fi2)]for j in range (co1*co2)]

    for i in range(0,):
        for j in range(0,)

    


    
    

#v = [[[4,5]],[[3,1]],[[0,-7]]]
#print(norma(v))

#A = [[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]]
#V = [[[1,-3]],[[4,3]],[[-3,1]]]
#res = accion_ma_ve(A,V)
#print(res)

#A = [[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]]                   
#B = [[[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]]
#res = multiplicacion_matrices(A,B)
#print(res)
                      
                      
    
        
