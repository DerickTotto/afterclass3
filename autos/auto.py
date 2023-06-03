from autos.motor import Motor
#from utilidades import *

class Auto(Motor):
    
    def __init__(self, ruedas=None, puertas=None, tipo=None):
        self.ruedas = ruedas
        self.puertas = puertas
        self.tipo = tipo
    
    def fabricarAuto(self, codigoAuto, nombreAuto, codigoMotor):
        self.codigoMotor = codigoMotor
        myMotor = Motor()
        motor1 = myMotor.obtenerMotor(self.codigoMotor)

        with open('./autos/recursos/listaAutos.txt', 'a') as nuevoAuto:
            data= f'{codigoAuto}|{nombreAuto}|{self.tipo}|{self.ruedas}|{self.puertas}|{motor1[0]}|'
            nuevoAuto.write(data)
            nuevoAuto.close()
        print("Auto fabricado")
    
    def comprarAuto(self, tipo):
        self.listarAutos(tipo)
        seleccion = input("Seleccionar codigo de auto")
        print ("Haz comprado un auto!!!")
    
    def listarAutos(self, tipo):
        with open('./autos/recursos/listaAutos.txt', 'r') as Autos:
            for Autos in Autos:
                detalles = Autos.split("|")
                if tipo == detalles[2]:
                    print(Autos)
                    return detalles
            else:
                Autos.close()
                return False