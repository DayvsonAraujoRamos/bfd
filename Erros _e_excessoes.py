# def num():
#     try:
#         numero = int(input("digite um número "))
#         print(f"voce digitou: {numero}")
#     except ValueError:
#         print("O número informado deve ser inteiro")
# num()
# =====================================
# try:
#     n1 = int(input("digite um numero "))
#     n2 = int(input("digite outro numero "))
#     print(f"o valor da multiplicaçao é:,{n1 * n2}")
# except ValueError:
#     print("digite um numero inteiro")
# ===========================================
# try:
#     num = int(input("digite um numero "))
# except ValueError:
#     print("digite um numero inteiro")
# else:
#     print("numero digitado com sucesso")
# =========================
# try:
#     arquivo = open("dados.txt","r")
#     print(arquivo.read())
# except FileNotFoundError:
#     print("arquivo nao encontrado")
# finally:
#     print("encerrando programa")
# =================================
# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError("divisao por zero nao permitida!")
#     return a / b 
# =======================================      
# class IdadeInvalidaError(Exception):
#     pass
# def cadastrar_idade(idade):
#     if idade < 0:
#         raise IdadeInvalidaError("Idade não pode ser negativa!")
#     print(f"Idade cadastrada: {idade}")
#     =========================================
# try:
#     a = float(input("Digite o primeiro número: "))
#     b = float(input("Digite o segundo número: "))
#     print(f"o resultado é: {a / b}")
# except ValueError:
#     print("Digite apenas números válidos!")
# except ZeroDivisionError:
#     print( "Não é possível dividir por zero!")
#     ===================================
# try:
#     n = int(input("digite um número inteiro: "))
# except ValueError:
#     print("valor inválido!")
# else:
#     if n % 2 == 0:
#         print("o número digitado é par.")
#     else:
#         print("o número digitado é ímpar.")
# finally:
#     print("fim do programa")
# ================================
# class SaldoInsuficienteError(Exception):
#     pass
# def sacar(saldo,valor):
#     if valor > saldo:
#         raise SaldoInsuficienteError("seu saldo é insuficiente")
#     return saldo - valor
# try:
#     novo_saldo = sacar(200,220)
#     print(f"saque realizado,seu novo saldo é: {novo_saldo}")
# except SaldoInsuficienteError as s:
#     print(s)
