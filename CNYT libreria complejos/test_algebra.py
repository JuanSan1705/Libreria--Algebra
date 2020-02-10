import algebra as alg
import math

def test_suma_vect():
    assert alg.suma_vect([[8,3],[-1,-4],[0,-9]],[[8,-3],[2,5],[3,0]]) == [[16,0],[1,1],[3,-9]],'Error 1'

def test_inverso_aditivo():
    assert alg.inverso_aditivo([[-5,2],[3,0],[0,-1]]) == [[5,-2],[-3,0],[0,1]],'Error 2'

def test_mul_escalar_vector():
    assert alg.mul_escalar_vector([-1,1],[[-2,5],[-1,-1],[2,-9]]) == [[-3,-7],[2,0],[7,11]],'Error 3'

def test_suma_matrices():
    assert alg.suma_matrices([[[-8,-3],[-6,-4],[0,-4]],[[-1,8],[6,-10],[8,-5]],[[4,0],[8,5],[-7,-9]]],[[[-7,-2],[-4,-2],[7,7]],[[5,9],[0,3],[6,-5]],[[1,5],[-6,-6],[5,8]]]) == [[[-15,-5],[-10,-6],[7,3]],[[4,17],[6,-7],[14,-10]],[[5,5],[2,-1],[-2,-1]]],'Eror 4'

def test_inversa_matriz():
    assert alg.inversa_matriz([[[7,3],[-1,7]],[[-9,-4],[-7,-9]]]) == [[[-7,-3],[1,-7]],[[9,4],[7,9]]],'Error 5'

def test_mul_escalar_matriz():
    assert alg.mul_escalar_matriz([-2,3],[[[3,-2],[8,-4]],[[4,-10],[-2,-8]]]) == [[[0,13],[-4,32]],[[22,32],[28,10]]],'Error 6'

def test_transpuesta():
    assert alg.transpuesta([[[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]]]) == [[[5,9],[8,2]],[[-7,-5],[-3,-7]],[[-1,-4],[7,-8]]],'Error 7'

def test_conjugada():
    assert alg.conjugada([[[-6,1],[3,8]],[[2,-6],[3,0]]]) == [[[-6,-1],[3,-8]],[[2,6],[3,0]]],'Error 8'

def test_daga():
    assert alg.daga([[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]]) == [[[7,-7],[5,0]],[[3,-8],[8,6]],[[8,-4],[-10,1]]],'Error 9'

def test_multiplicacion_mat():
    assert alg.multiplicacion_mat([[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]],[[[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]]) == [[[-33,153],[120,0],[44,-22]],[[87,0],[-26,-117],[107,70]],[[0,165],[147,26],[69,-36]]],'Error 10'
    assert alg.multiplicacion_mat([[[2,1],[3,0],[1,-1]],[[0,0],[0,-2],[7,-3]],[[3,0],[0,0],[1,-2]]],[[[0,-1],[1,0]],[[0,0],[0,1]]]) == "No es posible multiplicar las matrices",'Error 10 No compatibles'

def test_accion_ma_ve():
    assert alg.accion_ma_ve([[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]],[[[1,-3]],[[4,3]],[[-3,1]]]) == [[[54,-32]],[[0,17]],[[41,30]]],'Error 11'

def test_producto_interno():
    assert alg.producto_interno([[[2,-1]],[[-8,-5]],[[-2,-6]]],[[[6,-3]],[[5,-1]],[[-6,-2]]]) == [[[4,1]]], 'Error 12'

def test_norma():
    assert alg.norma([[[4,5]],[[3,1]],[[0,-7]]]) == 10, 'Error 13'

def test_distancia():
    assert alg.distancia([[2,7],[4,1],[2,-4]],[[7,8],[2,-8],[1,4]]) == 12, 'Error 14'
    assert alg.distancia([[9,-7],[-1,-6]],[[7,-8],[5,-9]]) == math.sqrt(50), 'Error 14'

def test_hermitania():
    assert alg.hermitania([[[3,0],[2,-1],[0,-3]],[[2,1],[0,0],[1,-1]],[[0,3],[1,1],[0,0]]]) == True, 'Error 15'
    assert alg.hermitania([[[1,0],[3,-1]],[[3,1],[0,1]]]) == False, 'Error 15'

def test_unitaria():
    assert alg.unitaria([[[1/math.sqrt(2),0],[0,1/math.sqrt(2)]],[[0,1/math.sqrt(2)],[1/math.sqrt(2),0]]]) == True, 'Error 16'
    assert alg.unitaria([[[0,1],[1,0],[0,0]],[[0,0],[0,1],[1,0]],[[1,0],[0,0],[0,1]]]) == False, 'Error 16'

def test_pro_tensorial():
    assert alg.pro_tensorial([[[1,1],[0,0]],[[1,0],[0,1]]],[[[-1,2],[-2,-2],[0,2]],[[2,3],[3,1],[2,2]],[[-2,1],[1,-1],[2,1]]]) == [[[-3,1],[0,-4],[-2,2],[0,0],[0,0],[0,0]],[[-1,5],[2,4],[0,4],[0,0],[0,0],[0,0]],[[-3,-1],[2,0],[1,3],[0,0],[0,0],[0,0]],[[-1,2],[-2,-2],[0,2],[-2,-1],[2,-2],[-2,0]],[[2,3],[3,1],[2,2],[-3,2],[-1,3],[-2,2]],[[-2,1],[1,-1],[2,1],[-1,-2],[1,1],[-1,2]]],'Error 17'

def main():
    test_suma_vect()
    test_inverso_aditivo()
    test_mul_escalar_vector()
    test_suma_matrices()
    test_inversa_matriz()
    test_mul_escalar_vector()
    test_transpuesta()
    test_conjugada()
    test_daga()
    test_multiplicacion_mat()
    test_accion_ma_ve()
    test_producto_interno()
    test_norma()
    test_distancia()
    test_hermitania()
    test_unitaria()
    test_pro_tensorial()
    print("Prueba Exitosa")

main()
    
