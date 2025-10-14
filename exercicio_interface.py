from abc import ABC,abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self,valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self,valor):
        print("Foi processado o pagamento no valor de", valor, "reais")

class Boleto(Pagamento):
    def processar(self,valor):
        print("O boleto foi pago no valor de", valor, "reais")

cartao = CartaoCredito()      
boleto =Boleto()

cartao.processar(650)
boleto.processar(720)
# ================================
from abc import ABC,abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar():
        pass
class Desligavel(ABC):
    @abstractmethod
    def desligar():
        pass

class Computador(Ligavel,Desligavel):
    def ligar(self):
        print("Computador ligado")
    def desligar(self):
        print("Computador desligado")

pc = Computador()

pc.ligar()
pc.desligar()
# =======================================

from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir():
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar():
        pass

class Relatorio(Imprimivel,Exportavel):
    def imprimir(self):
        print("O relatorio foi impresso")
    def exportar(self):
        print("O relatorio foi exportado com sucesso")

Rel = Relatorio()
Rel.imprimir()
Rel.exportar()
# =======================================

from abc import ABC,abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self,objeto):
        pass
    @abstractmethod
    def buscar(self,id):
        pass

class RepositorioMentoria(Repositorio):
    def salvar (self,objeto):
        self.objeto = objeto
        print(f"Objeto '{objeto}' salvo.")
    def buscar(self,id):
        self.id = id
        print(f"Objeto '{id}' encontrado.")    
# Se não incrementar o metodo buscar() vai dar erro, pois RepositorioMemoria()
# herda de uma classe abstrata, portanto tem que incrementar os dois metodos.

repositorio = RepositorioMentoria()   
repositorio.salvar("caixa")  
repositorio.buscar(1)        


        