import sqlite3

# Conecta ao banco em modo somente-leitura para segurança
conn = sqlite3.connect('file:escola_v2.db?mode=ro', uri=True)
cursor = conn.cursor()

def get_table_name() -> str:
    """Retorna o nome correto da tabela de alunos (Aluno ou alunos)."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('Aluno', 'alunos')")
    result = cursor.fetchone()
    return result[0] if result else ""

# Faça a query para pegar toda a tabela alunos e imprima na tela.
print("\n1. Todos os alunos da tabela:")
print("-" * 50)

table_name = get_table_name()
if not table_name:
    print("Erro: Tabela 'Aluno' ou 'alunos' não encontrada no banco.")
else:
    cursor.execute(f"SELECT * FROM {table_name}")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)

# Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas.
print("\n2. Top 10 médias dos alunos:")
print("-" * 50)

try:
    query_medias = f"""
    SELECT 
        nome,
        nota1,
        nota2,
        (nota1 + nota2) / 2 as media
    FROM {table_name}
    ORDER BY media DESC
    LIMIT 10
    """
    cursor.execute(query_medias)
    top_medias = cursor.fetchall()
    for nome, n1, n2, media in top_medias:
        print(f"Aluno: {nome}")
        print(f"  Nota 1: {n1:.1f}")
        print(f"  Nota 2: {n2:.1f}")
        print(f"  Média:  {media:.1f}")
        print("-" * 30)
except sqlite3.OperationalError as e:
    print("Erro ao calcular médias:", e)

# # Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
# print("\n3. Left Join entre Aluno e Turma:")
# print("-" * 50)
# query_join = """
# SELECT 
#     x.*,
#     y.nome as nome_turma,
#     y.ano
# FROM Aluno x
# LEFT JOIN Turma y ON x.turma_id = y.id
# """
# cursor.execute(query_join)
# alunos_turmas = cursor.fetchall()
# for registro in alunos_turmas:
#     print(registro)

# # Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.
# print("\n4. Alunos da turma 2:")
# print("-" * 50)
# query_turma2 = """
# SELECT 
#     x.*,
#     y.nome as nome_turma,
#     y.ano
# FROM Aluno x
# LEFT JOIN Turma y ON x.turma_id = y.id
# WHERE x.turma_id = 2
# """
# cursor.execute(query_turma2)
# alunos_turma2 = cursor.fetchall()
# for registro in alunos_turma2:
#     print(registro)

# conn.close()