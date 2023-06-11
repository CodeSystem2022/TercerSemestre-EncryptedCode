//Roberto Perez Bertoli
package domain;

public class Persona {
	private final int idPersona;
	private static int contadorPersona;
	
	static {//bloque de inicializacion estatico
		System.out.println("Ejecucion del bloque estatico");
		++Persona.contadorPersona;
		//idPersona = 10; No es estatico un atributo por eso el error
		
	}
	{
		//Bloque de inicializacion no estatico (contexto dinamico)
		System.out.println("Ejecucion del bloque no estatico");
		this.idPersona = Persona.contadorPersona++;//incrementamos el atributo
		
	}
	//Los bloques de inicializacion se ejecutan antes del constructor
	public Persona() {
		System.out.println("Esta es la ejecucion del constructor");
		
	}
	public int getIdPersona() {
		return this.idPersona;
	}
	@Override
	public String toString() {
		return "Persona [idPersona=" + idPersona + "]";
	}
}
