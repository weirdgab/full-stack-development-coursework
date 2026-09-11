import psycopg2

conn.psycopg2.connect(database='postgres', user='postgres',
                      password='senha123', host='127.0.0.1', post='5432')
print('Conexão com o Banco de Dados aberta com sucesso!')

cur.execute("""Delete from public."AGENDA" where "id"=1""")
conn.commit()

cont = cur.rowcount()
print(cont, "Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!")

conn.close()
