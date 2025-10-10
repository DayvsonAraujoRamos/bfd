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
        print("O relatorio foi expotado com sucesso")

Rel = Relatorio()
Rel.imprimir()
Rel.exportar()