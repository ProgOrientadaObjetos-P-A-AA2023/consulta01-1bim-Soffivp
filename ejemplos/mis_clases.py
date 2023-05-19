"""

"""
from _ast import expr


# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Persona():
    # nombre: "nom"
    # edad: 1
    # cedula: "00000"

    def __init__(self, nom, edad, ced):
        self.nombre = nom
        self.edad = edad
        self.cedula = ced

    def calcularNacimiento(self):
        anios = self.edad-2023
        print(anios , "es su año de nacimiento")


p1 = Persona('Sofia', 24 ,'1105210775')
p2 = Persona('Salome', 32 ,'59632322')

print("Tu nombre es: ",p1.nombre, ", tu edad es: ",p1.edad, "tu cedula es:",p1.cedula)
anios = p1.calcularNacimiento()

print("Tu nombre es: ",p2.nombre, ", tu edad es: ",p2.edad, "tu cedula es:",p2.cedula)
anios = p2.calcularNacimiento()


# clase 02
class Mascota():

        def __init__(self, nombre, raza,edad,cedula):
            self.nombre = nombre
            self.raza = raza
            self.edad = edad
            self.cedulapropietario = cedula


m1 = Mascota('Cenizo','gato',1,'651235400')
m2 = Mascota('Drupi','perro',5,'866464632')

print("La mascota: ", m1.nombre, "es un ",m1.raza, " y tiene ", m1.edad, "años")
print("La mascota: ", m2.nombre, "es un ",m2.raza, " y tiene ", m2.edad, "años")







