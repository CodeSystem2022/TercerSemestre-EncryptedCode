
package test;
import  accesodatos.*;
public class TestInterfaces {
    public static void main(String[] args) {
        IAccesoDatos datos = new ImplementacionMysql();
       // datos.listar();  //al ejecutar sucede el polimorfismo
       //imprimir(datos);
        datos = new ImplementacionOracle();
        //datos.listar();   //Dice listar desde Oracle
        //Utilizo el polimorfismo , pero se vino a la implementacion de Oracle
        imprimir(datos);
    }
    public static void imprimir(IAccesoDatos datos){
        datos.listar();   //Metodo generico,puede apuntar a Mysql o a Oracle
        
       //CON ESTO TENEMOS UN METODO GENERICO
       //APLICAMOS POLIMORFISMO , TRABAJAMOS CON COMPORTAMIENTO  
       //AL TRABAJR CON INTERFACES
       //AGREGARLE IMPLEMENTACION DEFINIDA A LOS METODOS DE LA INTERFACES, QUE QUIERAN
       //IMPLEMENTAR.COMUN PARA TRABAJAR CON DISEÑO.
       //LA BASE DE TODO LO QUE UTILIZA LOS FRAME
    }
}
