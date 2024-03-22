# 1. importar 
import src.LogicTTY.disparar_logica as juegoTTY_logic
import unittest


# 2. Construir clase de pruebas
# Esta clase sirve para crear un tablero para estas pruebas
class Tablero:
    def __init__(self,tablero):
        self.tablero=tablero


# 2.1. Construir clase de pruebas
class JuegoTTYTests ( unittest.TestCase ):
# 3. Crear metodos de prueba

    #prueba N1 (normal) para disparar a un objetivo
    def test_disparar_01(self):

        #entregar coordenadas
        x = 1
        y = 4

        #definir las variables de salida
        expected = True

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])
         

        #pasar coordenadas a la funcion
        resultado = juegoTTY_logic.Disparar(x,y,tablero).shoot()

        #verificar
        self.assertEqual(resultado, expected, "El resultado no es el esperado")

    #prueba N2 (normal) para disparar a un objetivo
    def test_disparar_02(self):

        #entregar coordenadas
        x = 1
        y = 5

        #definir las variables de salida
        expected = False

        #crear el tablero


        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])

        #pasar coordenadas a la funcion
        resultado = juegoTTY_logic.Disparar(x,y,tablero).shoot()
        

        #verificar
        self.assertEqual(resultado, expected, "El resultado no es el esperado")

    #prueba N3 (normal) para disparar a un objetivo
    def test_disparar_03(self):

        #entregar coordenadas
        x = 3
        y = 5

        #definir las variables de salida
        expected = False

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])
        
        #pasar coordenadas a la funcion
        resultado = juegoTTY_logic.Disparar(x,y,tablero).shoot()

        #verificar
        self.assertEqual(resultado, expected, "El resultado no es el esperado")  

    #prueba N4 (excepcion) para disparar a un objetivo
    def test_disparar_excepcion_negativos_04(self):

        #entregar coordenadas
        x = 2
        y = -2

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])


        #verificar si salto la excepcion
        with self.assertRaises(juegoTTY_logic.CoordenadasNegativas):

            #probar el disparo
            juegoTTY_logic.Disparar(x,y,tablero).shoot()
    
    #prueba N5 (excepcion) para disparar a un objetivo
    def test_disparar_excepcion_fuera_de_rango_05(self):

        #entregar coordenadas
        x = 4
        y = 7

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])

        #verificar si salto la excepcion
        with self.assertRaises(juegoTTY_logic.CoordenadasFueraRangoError):

            #probar el disparo
            juegoTTY_logic.Disparar(x,y,tablero).shoot()

    #prueba N6 (excepcion) para disparar a un objetivo
    def test_disparar_excepcion_valor_incorrecto_06(self):

        #entregar coordenadas
        x = 3
        y = "6"

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])

        #verificar si salto la excepcion
        with self.assertRaises(juegoTTY_logic.CoordenadasValorIncorrecto):

            #probar el disparo
            juegoTTY_logic.Disparar(x,y,tablero).shoot()
    
    #prueba N7 (excepcion) para disparar a un objetivo
    def test_disparar_excepcion_valor_incorrecto_07(self):

        #entregar coordenadas
        x = "3"
        y = 5

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])
        
        #verificar si salto la excepcion
        with self.assertRaises(juegoTTY_logic.CoordenadasValorIncorrecto):

            #probar el disparo
            juegoTTY_logic.Disparar(x,y,tablero).shoot()

    #prueba N8 (caso excepcional) para disparar a un objetivo
    def test_disparar_caso_disparo_mismas_coordenadas_08(self):

        #entregar coordenadas
        x = 2
        y = 2

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])
        
        #crear el objeto del disparo
        obj=juegoTTY_logic.Disparar(x,y,tablero)

        #definir las salidas 
        expected_result=False #no hubo hit porque ya antes habia disparado ahi

        #probar el disparo
        obj.shoot()
        resultado=obj.shoot()

        #verificar si salto la excepcion
        self.assertEqual(resultado,expected_result)

    #prueba N9 (caso excepcional) para disparar a un objetivo
    def test_disparar_caso_disparo_mismas_coordenadas_09(self):

        #entregar coordenadas
        x = 4
        y = 4

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])
        
        #crear el objeto del disparo
        obj=juegoTTY_logic.Disparar(x,y,tablero)

        #definir las salidas 
        expected_result=True #no hubo hit porque ya antes habia disparado ahi

        #probar el disparo
        obj.shoot()
        resultado=obj.shoot()

        #verificar si salto la excepcion
        self.assertEqual(resultado,expected_result)

    #prueba N10 (caso excepcional) para disparar a un objetivo
    #se tomaran los valores enteros y se deshecharan los decimales
        
    def test_disparar_caso_disparo_float_10(self):

        #entregar coordenadas
        x = 3.1
        y = 6.2

        #crear el tablero
        tablero=Tablero(tablero=[["O","O","O","X","O","O"],
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","O","O","O"]
                                 ["O","O","O","X","O","O"]])
        #crear el objeto del disparo
        obj=juegoTTY_logic.Disparar(x,y,tablero)

        #definir las salidas 
        expected_result=False

        #probar el disparo
        
        resultado=obj.shoot()

        #verificar si salto la excepcion
        self.assertEqual(resultado,expected_result)
        

if __name__ == '__main__':
    unittest.main()
