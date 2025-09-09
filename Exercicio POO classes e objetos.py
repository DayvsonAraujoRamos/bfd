class Pessoa:
 def __init__(self,nome,idade):
  self.nome = nome
  self.idade = idade
 def __str__(self):
  return f" Meu nome é {self.nome} tenho {self.idade} anos"
 def apresentar(self):
  print("Olá, meu nome é João e tenho 25 anos.")



pessoa1 = Pessoa("Dayvson",47)
pessoa2 = Pessoa( "Marta", 36)
pessoa1.apresentar()


