# def saudacao():
#     print("Olá, bem-vindo ao Python!")
# =============================
# def dobro(numero):
#     return numero * 2
# num = float(input("digite um numero "))
# print("o dobro dele é",dobro(num))
# =========================
# def soma(a, b):
#     return a + b
# resultado = soma(10,20)
# print(resultado)
# =======================
# def mensagem(nome="visitante"):
#   print(f"Olá, {nome}!")
# nome = input("Digite seu nome: ")
# if nome == "":
#     mensagem()
# else:
#     mensagem(nome)
# ========================
# def operaçoes(a,b):
#     return a+b,a-b,a*b
# n1 = float(input("digite um numero "))
# n2 = float(input("digite outro numero "))
# soma,subtraçao,multiplicaçao = operaçoes(n1,n2)
# print("A soma dos dois números é:",soma)
# print("A subtraçao dos dois números é:",subtraçao)
# print("A multiplicaçao dos dois números é:",multiplicaçao)
# ============================================================
# def media(*numeros):
#     return sum(numeros) / len(numeros)
# print(media(12, 53, 76))               
# print(media(10, 33, 11, 42, 40))   
# print(media(44, 54, 76, 54, 78, 14, 23))  
# =======================================
# def dados_pessoais(**dados):
#     for k in dados:
#         print(k, ":", dados[k])
# dados_pessoais(nome="Ana", idade=25, cidade="Recife")
# ==================================================
# def calculadora(a, b, operacao):
#     # Funções internas
#     def soma(x, y): return x + y
#     def subtracao(x, y): return x - y
#     def multiplicacao(x, y): return x * y
#     def divisao(x, y): return x / y
#     if operacao == "soma":
#         return soma(a, b)
#     elif operacao == "subtracao":
#         return subtracao(a, b)
#     elif operacao == "multiplicacao":
#         return multiplicacao(a, b)
#     elif operacao == "divisao":
#         return divisao(a, b)
#     else:
#         return "Operação inválida"
# print(calculadora(220, 22, "soma"))
# print(calculadora(220, 22, "subtracao"))
# print(calculadora(220, 22, "multiplicacao"))
# print(calculadora(220, 22, "divisao"))
# ==========================================
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)
def soma(a, b):
    return a + b
def multiplicar(a, b):
    return a * b
print(aplicar_operacao(6, 8, soma))        
print(aplicar_operacao(6, 8, multiplicar))  


