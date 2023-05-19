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
              
                
                sentencia = 'UPDATE persona SET nombre= %s, apellido= %s, email= %s WHERE id_persona=%s'
                valores = ('Juan Carlos', 'Roldan', 'jcroldan@gmail.com', 1)
                
                
                
                cursor.execute(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Los registros actualizados son: {registros_actualizados} ')
                registros = cursor.fetchall()
                
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()