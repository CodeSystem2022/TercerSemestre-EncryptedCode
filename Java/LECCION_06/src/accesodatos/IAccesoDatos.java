package accesodatos;

public interface IAccesoDatos {
	int MAX_REGISTRO = 10;
	
	//METODO INSERTAR ES ABSTRACTO Y SIN CUERPO
	
	void insertar();
	void listar();
	void actualizar();
	void eliminar();
}
