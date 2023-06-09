package test;

public class Test_argumentos_variables {
	public static void main(String[] args) {
		imprimir_numeros(5,3,6,7,89);
		imprimir_numeros(6,3,4,21,5);
		varios_parametros("Roberto", 5,56,7,8,34,23);
	}
	private static void varios_parametros(String nombre, int ...numeros) {
		System.out.println("Nombre: "+nombre);
		imprimir_numeros(numeros);
	}
	private static void imprimir_numeros(int ...numeros) {
		for(int i = 0; i < numeros.length; i++) {
			System.out.println("Elementos: "+numeros[i]);
		}
	}
}
