
import time
class Auto():
    color = ""
    marca = ""
    modelo =""
    llantas = 0
    velocidad = 0
    #ENCAPSULAMIENTO DE ATRIBUTOS
    __conductor = ""

    def __init__(self, color, marca, modelo, llantas, velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.llantas = llantas
        self.velocidad = velocidad

    # ENCAPSULAMIENTO LOS METODOS GET A SET
    def setConductor(self,conductor):
        self.__conductor = conductor
    def getConductor(self):
        return self.__conductor

    def caracteristicas(self):
        print("Color: ", self.color)
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Llantas: ", self.llantas)
        print("Velocidad: ", self.velocidad)
        # ENCAPSULAMIENTO DE ATRIBUTOS
        print("Conductor", self.getConductor())
    def aceleracion(self, aceleracion):
        for i in range(0, aceleracion, 2):
            print("Mi automil esta acelerando", i, "KM/s")
        time.sleep(0.1)

    def frenado(self, aceleracion,frenado):
        for i in range(aceleracion,frenado,-2):
            print("Mi automil esta frenando a ", i, "KM/s")
        time.sleep(0.1)

    def detenido(self):
            print("Mi automil se detuvo")