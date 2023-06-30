//Andrea Llavel.Cuando instale Mysql, cree una base de datos que se me pisaban los datos de estudiantes ;con nuestro proyecto integrador final.
//Entonces cambie los datos estudiantes, por "encrypted". Y tambien los datos de como se creaba la tabla, ysu postrior trabajo porque no me permitia realizarlo
package UTN.conexion;


import java.sql.Connection;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection(){
        Connection conexion = null;
        //Variables para conectarnos a la base de datos
        var baseDatos = "encrypted";
        var url = "jdbc:mysql://localhost:3306/"+baseDatos;
        var usuario= "root";
        var password = "admin";
        //cargamos la clase del driver de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException | SQLException e){
            System.out.println("Ocurrio un error en la conexion: "+e.getMessage());
        }//Fin catch
        return conexion;
    }//Fin Metodo connection
}
