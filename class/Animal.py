class Animal:

    nome = None
    lugar = None


    def __init__(self, nome, lugar):
        self.nome =nome
        self.lugar = lugar
    

    def getterNome(self):
        return self.nome
    
    def getterLugar(self):
        return self.lugar
    
    def setNome(nome):
        nome = nome

    def setLugar(lugar):
        lugar = lugar
    
    def hello(self):
        print(f"Animal {self.nome}, vive na {self.lugar}")

a1 = Animal("cachorro", "terra")

a1.hello()   

class Cachorro(Animal):

    def falar(self):
        print(f"Cachorro {self.nome} diz: Au Au!" )


b1 = Cachorro("hoy","casa")

b1.falar()

class Gato(Animal):

    def hello(self):
        print(f"{self.nome} diz: Miau, Miau")

c1 = Gato("Red", "Casa")
c1.hello()