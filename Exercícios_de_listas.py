livros = ["O principe","A batalha do apocalipse",'A arte da guerra' ]
print("Lista dos livros:", livros)
=======================
print("O primeiro livro é:", livros[0])
print("O último livro é:", livros[-1])
========================
livros.append("Vidas secas")
livros.append("Dom Casmurro")
print(livros)
============================
livros.insert(1,"Duna")
print(livros)
=========================
if "Silêncio  dos inocentes" in livros:
      livros.remove("Silêncio dos  inocentes")
else: 
      print("Livro não encontrado")
=====================
num = [1, 2, 3, 2, 4, 2, 5]
print("O número 2 aparece",num.count(2), "vezes")
=============================
for livro in livros:
      print(f"O livro {livro} é interessante")
===============================
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print(idade)
================================
valores = [10, 20, 30, 40]
soma = 0
for x in valores:
    soma += x
    print("A soma dos valores é",soma)
===============================
notas = []
for x in range(2):
    notas_aluno = []
    print(f"\nDigite as 3 notas do aluno {x+1}:")
    for y in range(3):
        nota = float(input(f"Nota {y+1}: "))
        notas_aluno.append(nota)
    notas.append(notas_aluno)
print("\nNotas:", notas)
for x in range(len(notas)):
    soma = 0
    for nota in notas[x]:
        soma += nota
    media = soma / len(notas[x])
    print("Média do aluno", x+1, ":", media)
===================================
tabuleiro = [["[ ]"] * 8 for _ in range(8)]
pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[0] = pecas
tabuleiro[1] = ["pea"] * 8
tabuleiro[6] = ["pea"] * 8
tabuleiro[7] = pecas
print("\nTabuleiro de Xadrez:")
for linha in tabuleiro:
    print(*linha)



