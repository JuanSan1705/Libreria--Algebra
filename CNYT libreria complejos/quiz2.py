

def Multiplicar_Matrices(b,a):
    
    resul = [[(b[0][0]*a[0][0]+b[0][1]*a[1][0]),(b[0][0]*a[0][1]+b[0][1]*a[1][1])],[(b[1][0]*a[0][0]+b[1][1]*a[1][0]),(b[1][0]*a[0][1]+b[1][1]*a[1][1])]]

    return resul

def main():

    B = [[1,0],[0,1]]
    A = [[1,1],[1,0]]
    k = 0
    while B[0][0] <= 1000:

        B = Multiplicar_Matrices(B, A)

        k = k + 1



    print(k)

main()
