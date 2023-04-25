import mysql.connector
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='dbyoutube'
)


cursor=connection.cursor()


"""Create
nome_produto="lindt"
valor=5
command=f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}",{valor})'
cursor.execute(command)
connection.commit()
"""

#Read
get_command= f'SELECT * FROM vendas'
cursor.execute(get_command)
result=cursor.fetchall()
print(result)


"""
cursor=connection.cursor()
command=''   #aspas simples sempre nas queries
cursor.execute(command)    #isso aqui é obrigatorio em todos os metodos de crud
connection.commit()    #isso é usado APENAS em métodos que alteram o db. O get não tem isso
consulta=cursor.fetchall()     #para ler o banco de dados
"""


cursor.close()
connection.close()