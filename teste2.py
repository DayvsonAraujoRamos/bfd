class Comodo:
    def __init__(self, nome):
        self.nome = nome
        print(f"Cômodo '{self.nome}' criado.")

    def __del__(self):
        print(f"Cômodo '{self.nome}' destruído.")

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]
        print("Casa construída.")

    def __del__(self):
        print("Casa destruída.")

# Teste
casa = Casa()
del casa

