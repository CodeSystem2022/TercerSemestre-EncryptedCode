
package test;

//Trabajo de Andrea LLavel_05/05/2023
import domain.*;


public class TestInstanceOf {      //InstanceOf: significa instancia de cierto tipo
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);
        determinarTipo(empleado1);       //Si ejecuto aca, me manda a el error ClassCastException
        empleado1 =new Gerente("Jose", 5000, "Sistemas");
       // determinarTipo(empleado1);    //Esta apuntando tipo Gerente
    }
    
    public static void determinarTipo(Empleado empleado){
        if(empleado instanceof Gerente){       //Esta comprobacion es falsa, por eso no nos muestra nada.
            //los mas genericos serian la clase empleado y la clase object
            System.out.println("Es de tipo Gerente");
            Gerente gerente = (Gerente)empleado;       //Creamos un objeto Gerente y utilizando loque es la variable empleado la convertimos a Gerente
            //((Gerente) empleado).getDepartamento();    //Formato asignado por el IDE
            System.out.println("gerente = "+gerente.getDepartamento());
            
    }
       else if(empleado instanceof Empleado){
            System.out.println("Es de tipo Empleado");
           // Gerente gerente = (Gerente)empleado;
            //System.out.println("gerente "+gerente.getDepartamento());
        }
       else if(empleado instanceof Object){
            System.out.println("Es de tipo Object");
}
}
}