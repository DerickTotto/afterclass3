class Motor:
    
    def __init__(self, tipoCombustible=None, cilindrada=None, potencia=None, torque=None):
        self.tipoCombustible = tipoCombustible
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.torque = torque

    def fabricarMotor(self, codigoMotor, nombreMotor):
        with open('./autos/recursos/listaMotores.txt', 'a') as nuevoMotor:
            data= f'{codigoMotor}|{nombreMotor}|{self.tipoCombustible}|{self.cilindrada}|{self.potencia}|{self.torque}|'
            nuevoMotor.write(data)
            nuevoMotor.close()
        return("Motor fabricado")

    def obtenerMotor(self, codigoMotor=None):
        with open('./autos/recursos/listaMotores.txt', 'r') as Motores:
            for Motor in Motores:
                detalles = Motor.split("|")
                if codigoMotor == detalles[0]:
                    Motores.close()
                    return detalles
            else:
                Motores.close()
                return False