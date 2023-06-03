// Manejo de excepciones
package test;
import static aritmetica.Aritmetica.division;
import excepciones.OperacionExcepcion;

public class TestExcepciones {
   
    public static void main(String[] args) {
        int resultado = 0;
        try{
            resultado = division(10, 0);
        } catch(OperacionExcepcion e){
            System.out.println("Ocurrio un error de tipo OperacionExcepcion");
            System.out.println(e.getMessage());
        } catch(Exception e){
            System.out.println("Ocurrio un error");
            e.printStackTrace(System.out);  //Se lo conoce como Pila de Excepciones
            System.out.println(e.getMessage());
        }
        finally{
            System.out.println("Se reviso la division entre cero");
        }
        System.out.println("La variable resultado tiene como valor: "+resultado);
    }
} //las clases son excepciones que ocurren en tiempo de ejecucion
