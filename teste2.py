from abc import ABC, abstractmethod

# Interface
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass


# Classe que implementa todos os métodos
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

    def buscar(self, id):
        print(f"Buscando objeto com ID {id}.")
        return {"id": id, "objeto": "Exemplo"}


# Agora funciona normalmente
repo = RepositorioMemoria()
repo.salvar("Livro A")
print(repo.buscar(1))

