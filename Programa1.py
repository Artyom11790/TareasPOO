class persona:
    #atributos
    def __init__(self,nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI


    def mostrar(self):
        print(f'{self.nombre}\n{self.edad} años\n{self.DNI}')
    
    def EsMayorDeEdad(self):
        if self.edad > 18:
            return True
        else:
            return False


persona1=persona("Arturo coronado",19,"23233456F")
persona1.mostrar()
print(persona1.EsMayorDeEdad())