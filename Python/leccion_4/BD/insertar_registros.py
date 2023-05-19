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
                sentencia = 'INSERT INTO persona (NOMBRE, apellido, email) VALUE (%s, $s, %s)'
                entrada = input("Digite los id personas a buscar (separados por coma): ")
                valores = ('Carlos', 'Lara', 'clara@gmail.com')
                
                
                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Los registros insertados son: {registros_insertados} ')
                registros = cursor.fetchall()
                for registro in registros:
                    print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()