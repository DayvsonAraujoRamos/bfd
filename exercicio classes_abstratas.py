from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):  
     pass
class Cachorro(Animal):
    def falar(self):
       return "Auau"
class Gato(Animal):
    def falar(self):
       return "Miau"   
dog = Cachorro()   
cat = Gato()
print(dog.falar())
print(cat.falar())  
# ===================
rex = Animal()
# A classe não pode ser instanciada,só serve de modelo para as subclasses
# =============================
from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    @abstractmethod
    def area():
       pass
    def perimetro():
       pass
class Retangulo(FormaGeometrica):
    def __init__(self,base,altura):
      self.base = base
      self.altura = altura

    def area(self):
       return self.base *self.altura
    def perimetro(self):
       return 2 * (self.base + self.altura)
    
retangulo1 = Retangulo(6,7) 
print(f" A área do retangulo é {retangulo1.area()}")   
print(f" O perimetro do retangulo é {retangulo1.perimetro()}")
# ============================  
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    
    def mover(self):
        return "O carro está em movimento!"
    # def parar(self):
    #     return "O carro está parando"
    
fusca = Carro()
# Ocorre um erro pois é obrigatório também incrementar o metodo parar()    
print(fusca.mover())
print(fusca.parar())