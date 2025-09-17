aluno = {"nome": "Pedro", "idade": 18, "nota": 8.0}
print(aluno)
# ===================================
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print(produto["nome"])
print(produto["estoque"])
# =======================
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print(pessoa)
# =============================
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro["ano"]
print(carro)
# ===============================
contato = {"nome": "Ana", "email": "ana@email.com"}
if "telefone" in contato:
    print("Chave telefone encontrada:", contato["telefone"])
else:
    print("Chave telefone não encontrada")
    # ==============================
def contar_frequencia(palavras):
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] = contagem[palavra] + 1
        else:
            contagem[palavra] = 1
    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(contar_frequencia(palavras))
# ============================
d = {"a": 1, "b": 2, "c": 3}
d_invertido = {}
for chave in d:
    valor = d[chave]
    d_invertido[valor] = chave
print(d_invertido)
# ===========================
alunos = {
    "Pedro":   [6.5, 9.0, 9.5],
    "José": [7.0, 7.5, 7.0],
    "Maria": [8.0, 9.0, 10.0]
}
for aluno in alunos:
    notas = alunos[aluno]
    soma = 0
    for x in notas:
        soma = soma + x
    media = soma / len(notas)
    print(aluno, "Média =", media)
    # ===========================
dicionario1 = {"x": 1, "y": 2}
dicionario2 = {"y": 3, "z": 4}
novo = {}
for x in dicionario1:
    novo[x] = dicionario1[x]
for x in dicionario2:
    novo[x] = dicionario2[x]
print(novo)
# ========================
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
lista = []
for nome in pontuacoes:
    lista.append([nome, pontuacoes[nome]])
for x in range(len(lista)):
    for y in range(x + 1, len(lista)):
        if lista[y][1] > lista[x][1]:
            temp = lista[x]
            lista[x] = lista[y]
            lista[y] = temp
for item in lista:
    print(item[0], item[1])

