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
                sentencia = 'DELETE FROM persona WHERE id_persona=%s'
                entrada = input('Digite el numero de registro a eliminar: ')
                valores = (entrada,)
                
                
                cursor.execute(sentencia, valores)
                registros_eliminados = cursor.rowcount
                print(f'Los registros eliminados son: {registros_eliminados} ')
                registros = cursor.fetchall()