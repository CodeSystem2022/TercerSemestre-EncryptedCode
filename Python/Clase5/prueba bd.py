import psycopg2

try:
    connection=psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'xxxxxx',
        database = 'test bd'
    )
    print('conexion exitosa')
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM persona")
except Exception as ex:
    print(ex)
