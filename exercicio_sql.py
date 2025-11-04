import sqlite3

# Importe o módulo sqlite3  e faça a conexão com o banco de dados escola_v2.db
conn = sqlite3.connect('escola_v2.db')
cursor = conn.cursor()

print("\n1. Faça a query para pegar toda a tabela alunos e imprima na tela.")
print("-" * 50)
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

print("\n2. Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas. No fim imprima na tela a lista desses alunos e suas médias.")
print("-" * 50)
query_medias = """
SELECT 
    nome,
    (nota1 + nota2) / 2 as media
FROM Aluno
ORDER BY media DESC
LIMIT 10
"""
cursor.execute(query_medias)
top_medias = cursor.fetchall()
for nome, media in top_medias:
    print(f"Aluno: {nome} - Média: {media:.2f}")

print("\n3. Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.")
print("-" * 50)
query_join = """
SELECT 
    x.*,
    y.nome as nome_turma,
    y.ano
FROM Aluno x
LEFT JOIN Turma y ON x.turma_id = y.id
"""
cursor.execute(query_join)
alunos_turmas = cursor.fetchall()
for registro in alunos_turmas:
    print(registro)

print("\n4. Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.")
print("-" * 50)
query_turma2 = """
SELECT 
    x.*,
    y.nome as nome_turma,
    y.ano
FROM Aluno x
LEFT JOIN Turma y ON x.turma_id = y.id
WHERE x.turma_id = 2
"""
cursor.execute(query_turma2)
alunos_turma2 = cursor.fetchall()
for registro in alunos_turma2:
    print(registro)

conn.close()
