from autos.motor import Motor
from autos.auto import Auto

def creaMotor():
    newMotor = Motor("Gasolina","2.0","255Hp","320Nm")
    print(newMotor.fabricarMotor("focus-a10", "Ecoboost"))

def ComprarMotor():
    getMotor = Motor()
    print(getMotor.obtenerMotor("focus-a10"))

#creaMotor()
#ComprarMotor()

def fabricarAuto():
    newAuto = Auto("4","5","Hatchback")
    newAuto.fabricarAuto("ford-f1", "Focus", "focus-a10")

fabricarAuto()