import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='postgresDB',
    user='admin',
    password='admin123'
)

cursor = conn.cursor()

# Atualizar dados na tabela
cursor.execute("""
UPDATE public."AGENDA"
SET nome = 'teste atualizado'
WHERE id = 1;
""")

conn.commit()

# Ler os dados atualizados
cursor.execute("""
SELECT id, nome, telefone FROM public."AGENDA";
""")
rows = cursor.fetchall()
for row in rows:
    print(f'ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}')

# Fechar a conexão
cursor.close()
conn.close()
