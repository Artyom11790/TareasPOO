class Microsof:
    def __init__(self,ganancias,sofware,NumEmp):
        self.__ganancias=ganancias
        self.sofware=sofware 
        self.NumEmp=NumEmp
    def presentar(self):
        print(f' Ganancias: {self.__ganancias}\n Software: {self.sofware}\n Numero de empleados: {self.NumEmp}')
    def getGanancias(self):
       print(self.__ganancias)

    def despidos(self):
       if Empresa1.__ganancias<1000000000:
         k=input("¿Deseas despedir personal?: ")
         if k== "si":
            s = int(input("¿cuantos empleados deseas despedir?:"))
            self.NumEmp=self.NumEmp-s
            print(f'Numero de Empleados actuales: {self.NumEmp}')
        


class xbox(Microsof):
    def __init__(self, juegos, hardware,ganancias,software,NumEmp):
        super().__init__(ganancias,software,NumEmp)
        self.juegos=juegos
        self.hardware=hardware
        self.__ganancias=ganancias
    def presentar(self):
        print(f'Juego mas importante: {self.juegos}\n Hardaware: {self.hardware},\n Ganancias {self.__ganancias},\nStreaming: {self.sofware}\n Numero de empleados: {self.NumEmp}')
    def getGanancias(self): 
        print(self.__ganancias)
   
    def despidos(self):
       if division.__ganancias<1000000000:
         k=input("¿Deseas despedir personal?: ")
         if k== "si":
            s = int(input("¿cuantos empleados deseas despedir?:"))
            self.NumEmp=self.NumEmp-s
            print(f'Numero de Empleados actuales: {self.NumEmp}')
        

class linkekln(Microsof):
    def __init__(self, usuarios,ganancias,NumEmp):
        super().__init__(self,ganancias, NumEmp)
        self.usuarios=usuarios
        self.__ganancias=ganancias
    def presentar(self):
        print(f'\n Ganancias: {self.__ganancias},\n Numero de empleados: {self.NumEmp}\n Numero de usuarios: {self.usuarios}')
    def getGanancias(self): 
        print(self.__ganancias)

    def despidos(self):
       if division2.__ganancias<1000000000:
         k=input("¿Deseas despedir personal?: ")
         if k== "si":
            s = int(input("¿cuantos empleados deseas despedir?:"))
            self.NumEmp=self.NumEmp-s
            print(f'Numero de Empleados actuales: {self.NumEmp}')
   

elegir=int(input("Datos financieros:\n 1)-Microsoft\n 2)-Xbox \n 3)-Linkedln\n"))



print("******************************************************************************************\n")
if elegir==1:
 print("ESTADO DE MICROSOFT")
 Empresa1=Microsof(10000,"windows 11",15000)
 Empresa1.presentar()
 Empresa1.despidos()
 print("******************************************************************************************\n")

elif elegir==2:
 print("ESTADO DE LA DIVISION XBOX")
 division = xbox("Halo","Xbox series",1000,"xcloud",10000)
 division.presentar()
 division.despidos()
 print("******************************************************************************************\n")
 
elif elegir==3:
   print("ESTADO DE LA DIVISION LINKEDLN")
   division2 = linkekln(1374838,100,1000)
   division2.presentar()
   division2.despidos()
   print("******************************************************************************************\n")
else:
   print("seleccionaste una opcion incorrecta")

