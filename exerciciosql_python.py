import sqlite3

# Conectar ao banco de dados (apenas leitura)
conn = sqlite3.connect('escola_v2.db', uri=True)
cursor = conn.cursor()

# 1. Query para pegar toda a tabela alunos
print("\n1. Todos os alunos da tabela:")
print("-" * 50)
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

# 2. Média entre nota1 e nota2, ordenada em ordem decrescente (top 10)
print("\n2. Top 10 médias dos alunos:")
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

# 3. Left Join entre Aluno e Turma
print("\n3. Left Join entre Aluno e Turma:")
print("-" * 50)
query_join = """
SELECT 
    a.*,
    t.nome as nome_turma,
    t.ano
FROM Aluno a
LEFT JOIN Turma t ON a.id_turma = t.id
"""
cursor.execute(query_join)
alunos_turmas = cursor.fetchall()
for registro in alunos_turmas:
    print(registro)

# 4. Alunos da turma 2
print("\n4. Alunos da turma 2:")
print("-" * 50)
query_turma2 = """
SELECT 
    a.*,
    t.nome as nome_turma,
    t.ano
FROM Aluno a
LEFT JOIN Turma t ON a.id_turma = t.id
WHERE a.id_turma = 2
"""
cursor.execute(query_turma2)
alunos_turma2 = cursor.fetchall()
for registro in alunos_turma2:
    print(registro)

conn.close()
