nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
altura = input("ingrese su altura: ")
peso = input("ingrese su peso: ")
infoPersonal = (nombre, edad, altura, peso)
tup = tuple(infoPersonal)
print(infoPersonal)



experiencia_lab=[]
Experiencialab = input("ESCRIBE SI TIENES EXPERIENCIA LABORAL 1.si 2.no: ")
if Experiencialab == 2:
    print("NO TIENES EXPERIENCIA LABORAL")
else:
    experienciala=(input("Cual es tu experiencia labora: "))
    experiencia_lab.append(experienciala)
experienciatot=tuple(experiencia_lab)
print(f'tu experiencia laboral es: {experienciatot}')