//Andrea Llavel 
package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTRO = 10;    //ES UN ATRIBUTO QUE SE LE DECLARA UN VALOR
    //metodo insert es abstracto y sin cuerpo
    void insertar();
    void listar();
    void actualizar();
    void eliminar();
}
