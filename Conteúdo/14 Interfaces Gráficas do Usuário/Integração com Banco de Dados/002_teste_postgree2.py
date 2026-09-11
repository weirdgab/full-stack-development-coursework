import psycopg2

nomeDaTabela = 'tabelaExemplo'
cursor.execute(" insert into %s values (%%s, %%s)" % nomeDaTabela, [10, 20])
