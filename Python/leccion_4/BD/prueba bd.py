import psycopg2

try:
    connection=psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'xxxxxx',
        database = 'test bd'
    )
    print('conexion exitosa')
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = "SELECT id_persona, nombre FROM persona"
                entrada = input("Digite los id personas a buscar (separados por coma): ")
                llaves_primarias = (tuple(entrada.split(', ')),g)
                cursor=connection.cursor()
                cursor.execute(sentencia, llaves_primarias)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
