class Persona: 
    def __init__(self,nombre,edad,nube):
        self.__nombre=nombre
        self.__edad=edad
    
    #metodos set

    def set_edad(self,edad):   
       self.__edad=edad
    
  
    def set_nombre(self,nombre):
         self.__nombre = nombre

    #metodos get
    def get_nombre(self):
       return self.__nombre
       
    def get_edad(self):
     return self.__edad
    
    def es_mayor_de_edad(self):
       if self.__edad>18:
          return True
       
       else:
          return False
    
    def mostrar_persona(self):
       print(f'{self.nombre}\n{self.edad}')

    def es_mayor_que(self):
       if self.__edad>10:
          return True
       else:
          return False


per1=Persona("grecia",10)
per2=Persona("jaime",15)

#per1.mostrar_persona()
#per2.mostrar_persona()



print(per1.get_nombre())
edad1 = per1.set_edad(17)
print(per1.get_edad())
print(per1.es_mayor_de_edad())

print(per1.es_mayor_que())

print(per2.get_nombre())
per2.set_edad(19)
print(per2.get_edad())
print(per2.es_mayor_de_edad())




