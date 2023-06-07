from capa_datos_persona.Persona import Persona
from capa_datos.conexion import Conexion
from logger_base import log
class PersonaDAO:
    '''
    DAO significa: Data Acces Object
    CRUD signfica:
        create -> insertar
        read -> seleccionar
        update -> actualizar
        delete -> eliminar
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALZIAR = 'UPDATE persona SET nombre= %s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    
    #definimos los metodos de clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls.SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
            
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount
    @classmethod
    def actualziar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALZIAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount
    
    @classmethod
    def eliminar(cls, persona):
        #Eliminar un registro
        persona1 = Persona(id_persona=13)
        personas_eliminadas = PersonaDAO.eliminar(persona1)
        log.debug(f'Personas eliminadas: {personas_eliminadas}')
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Los objetos eliminados son: {persona}')
                return cursor.rowcount
if __name__ == '__main__' :
    #Actualizar un registro
    persona1 = Persona(1, 'Juan Jose', 'Peña', 'jjpeña@gmail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')
    
    
    # insertamos un registro
    persona1 = Persona(nombre='Pedro', apellido='Romero', email='promero@gmail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')
    
     
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)