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
    
    def oi(self):
        print(f"Animal {self.nome}, vive na {self.lugar}")

a1 = Animal("cachorro", "terra")

a1.oi()    
