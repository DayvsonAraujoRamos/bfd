import sqlite3

conn = sqlite3.connect('escola_v2.db')
cursor = conn.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("\nTabelas no banco de dados:")
print("-" * 50)
for table in tables:
    table_name = table[0]
    print(f"\nEstrutura da tabela {table_name}:")
    print("-" * 50)
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    for column in columns:
        print(f"Coluna: {column[1]}, Tipo: {column[2]}")

conn.close()