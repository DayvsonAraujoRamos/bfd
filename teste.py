# # Classe base
# class Animal:
#     def __init__(self, nome, idade):
#         self._nome = nome       # protegido
#         self.__idade = idade    # privado

#     # Encapsulamento com getters/setters
#     def get_idade(self):
#         return self.__idade

#     def set_idade(self, idade):
#         if idade >= 0:
#             self.__idade = idade
#         else:
#             print("Idade inválida!")

#     def fazer_som(self):
#         print(f"{self._nome} faz um som.")

# # Classe filha
# class Cachorro(Animal):
#     def __init__(self, nome, idade, raca):
#         super().__init__(nome, idade)  # herança
#         self.raca = raca

#     # Polimorfismo: sobrescrevendo método
#     def fazer_som(self):
#         print(f"{self._nome} está latindo!")

# # Testando
# dog = Cachorro("Rex", 3, "Labrador")
# dog.fazer_som()                         # Polimorfismo
# print(f"Idade: {dog.get_idade()}")      # Encapsulamento
# dog.set_idade(5)
# print(f"Nova idade: {dog.get_idade()}") # Encapsulamento

alunos = [
    {"nome": "ana", "nota": 8.5},
    {"nome": "bruno", "nota": 6.0},
    {"nome": "carla", "nota": 7.2},
    {"nome": "diego", "nota": 5.8},
    {"nome": "maria", "nota": 9.0}
]

# 1) Filtrar só os aprovados
aprovados = list(filter(lambda a: a["nota"] >= 7, alunos))

# 2) Transformar nomes em maiúsculas
aprovados_formatados = list(map(
    lambda a: {"nome": a["nome"].upper(), "nota": a["nota"]}, aprovados
))

# 3) Criar mensagens personalizadas
mensagens = list(map(
    lambda a: f"{a['nome']} FOI APROVADO COM NOTA {a['nota']}",
    aprovados_formatados
))

print("Mensagens finais:")
for msg in mensagens:
    print(msg)



