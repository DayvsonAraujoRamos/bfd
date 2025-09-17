# Classe base
class Animal:
    def __init__(self, nome, idade):
        self._nome = nome       # protegido
        self.__idade = idade    # privado

    # Encapsulamento com getters/setters
    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade inválida!")

    def fazer_som(self):
        print(f"{self._nome} faz um som.")

# Classe filha
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)  # herança
        self.raca = raca

    # Polimorfismo: sobrescrevendo método
    def fazer_som(self):
        print(f"{self._nome} está latindo!")

# Testando
dog = Cachorro("Rex", 3, "Labrador")
dog.fazer_som()                         # Polimorfismo
print(f"Idade: {dog.get_idade()}")      # Encapsulamento
dog.set_idade(5)
print(f"Nova idade: {dog.get_idade()}") # Encapsulamento



