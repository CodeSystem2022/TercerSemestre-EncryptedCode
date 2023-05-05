
 dominio del paquete ;

 clase  pública Empleado {
    protegido  String  nombre ;
     doble  sueldo protegido ;

    public  Empleado ( String  nombre , doble  sueldo ){
        esto _ nombre = nombre ;
        esto _ sueldo = sueldo ;
    }
    //Metodo para la sobreescritura
    public  String  obtenerDetalles (){
        devuelve "Nombre:" + esto . nombre + ", Sueldo:" + este . salario _
    }

    public  String  getNombre () {
        volver  nombre ;
    }

    public  void  setNombre ( String  nombre ) {
        esto _ nombre = nombre ;
    }

    public  double  getSueldo () {
        volver  sueldo ;
    }

    public  void  setSueldo ( doble  sueldo ) {
        esto _ sueldo = sueldo ;
    }

}


 26 cambios: 26 adiciones y 0 eliminaciones26 
InstanciaDe/src/dominio/Gerente.java
@@ -0,0 +1,26 @@

 dominio del paquete ;


public  class  Gerente   extiende  Empleado {
     Cuerda  privada departamento ;

    public  Gerente ( String  nombre , doble  sueldo , String  departamento ){
        súper ( nombre , sueldo );
        esto _ departamento = departamento ;
    }
    //Sobreescribimos el metodo
  @ anular 
  public  String  obtenerDetalles (){
     volver  súper . obtenerDetalles ()+ ", Departamento: " + este . departamento ;
  }

    public  String  getDepartamento () {
        volver  departamento ;
    }

    public  void  setDepartamento ( String  departamento ) {
        esto _ departamento = departamento ;
    }

}
 34 cambios: 34 adiciones y 0 eliminaciones34 
InstanceOf/src/test/TestInstanceOf.java
@@ -0,0 +1,34 @@

 prueba de paquete ;

//Trabajo de Andrea LLavel_05/05/2023
importar  dominio .*;


public  class  TestInstanceOf {       //InstanceOf: significa instancia de cierto tipo
    public  static  void  main ( String [] args ) {
        Empleado  empleado1 = nuevo  Empleado ( "Juan" , 10000 );
        determinarTipo ( empleado1 );       //Si ejecuto aca, me manda al error ClassCastException
        empleado1 = nuevo  Gerente ( "José" , 5000 , "Sistemas" );
       // determinarTipo(empleado1); //Esta apuntando tipo Gerente
    }

    public  static  void  determinarTipo ( Empleado  empleado ){
        if ( empleado  instanceof  Gerente ){        //Esta comprobacion es falsa, por eso no nos muestra nada.
            //los mas genericos serian la clase empleado y la clase object
            sistema _ fuera _ println ( "Es de tipo Gerente" );
            Gerente  gerente = ( Gerente ) empleado ;       //Creamos un objeto Gerente y utilizando lo que es la variable empleado la convertimos a Gerente
            //((Gerente) empleado).getDepartamento(); //Formato asignado por el IDE
            sistema _ fuera _ println ( "gerente = " + gerente . getDepartamento ());

    }
       else  if ( empleado  instancia de  Empleado ){
            sistema _ fuera _ println ( "Es de tipo empleado" );
           // Gerente gerente = (Gerente)empleado;
            //System.out.println("gerente "+gerente.getDepartamento());
        }
       else  if ( empleado  instancia de  Objeto ){
            sistema _ fuera _ println ( "Es de tipo Objeto" );
}
}
}
 33 cambios: 33 adiciones y 0 eliminaciones33 
Sobreescritura/src/domain/Empleado.java
@@ -0,0 +1,33 @@
 dominio del paquete ;

 clase  pública Empleado {
    protegido  String  nombre ;
     doble  sueldo protegido ;

    public  Empleado ( String  nombre , doble  sueldo ){
        esto _ nombre = nombre ;
        esto _ sueldo = sueldo ;
    }
    //Metodo para la sobreescritura
    public  String  obtenerDetalles (){
        devuelve  "Nombre:" + esto . nombre + ",Sueldo:" doble  sueldo1 = este . salario _
    }

    public  String  getNombre () {
        volver  nombre ;
    }

    public  void  setNombre ( String  nombre ) {
        esto _ nombre = nombre ;
    }

    public  double  getSueldo () {
        volver  sueldo ;
    }

    public  void  setSueldo ( doble  sueldo ) {
        esto _ sueldo = sueldo ;
    }

}

 12 cambios: 12 adiciones y 0 eliminaciones12 
Sobreescritura/src/dominio/Gerente.java
@@ -0,0 +1,12 @@

 dominio del paquete ;

public  class  Gerente  extiende  Empleado {
     Cuerda  privada departamento ;

    public  Gerente ( String  nombre , doble  sueldo , String  departamento ){
        súper ( nombre , sueldo );
        esto _ departamento = departamento ;
    }

}
 12 cambios: 12 adiciones y 0 eliminaciones12 
Sobreescritura/src/test/TestSobreescritura.java
@@ -0,0 +1,12 @@

 prueba de paquete ;

 dominio de importación . Gerente ;


public  class  TestSobreescritura {
    public  static  void  main ( String [] args ) {
        Gerente  gerente1 = nuevo  Gerente ( "José" , 5000.0 , "Sistemas" );
        sistema _ fuera _ println ( "gerente1= " + gerente1 . obtenerDetalles ());
    }
}
 35 cambios: 35 adiciones y 0 eliminaciones35 
Sobreescritura1/src/dominio/Empleado.java
@@ -0,0 +1,35 @@

 dominio del paquete ;

 clase  pública Empleado {
    protegido  String  nombre ;
     doble  sueldo protegido ;

    public  Empleado ( String  nombre , doble  sueldo ){
        esto _ nombre = nombre ;
        esto _ sueldo = sueldo ;
    }
    //Metodo para la sobreescritura
    public  String  obtenerDetalles (){
        devuelve "Nombre:" + esto . nombre + ", Sueldo:" + este . salario _
    }

    public  String  getNombre () {
        volver  nombre ;
    }

    public  void  setNombre ( String  nombre ) {
        esto _ nombre = nombre ;
    }

    public  double  getSueldo () {
        volver  sueldo ;
    }

    public  void  setSueldo ( doble  sueldo ) {
        esto _ sueldo = sueldo ;
    }

}


 17 cambios: 17 adiciones y 0 eliminaciones17 
Sobreescritura1/src/dominio/Gerente.java
@@ -0,0 +1,17 @@

 dominio del paquete ;


public  class  Gerente   extiende  Empleado {
     Cuerda  privada departamento ;

    public  Gerente ( String  nombre , doble  sueldo , String  departamento ){
        súper ( nombre , sueldo );
        esto _ departamento = departamento ;
    }
    //Sobreescribimos el metodo
  @ anular 
  public  String  obtenerDetalles (){
     volver  súper . obtenerDetalles ()+ ", Departamento: " + este . departamento ;
  }
}
 21 cambios: 21 adiciones y 0 eliminaciones21 
Sobreescritura1/src/test/TestSobreescritura1.java
@@ -0,0 +1,21 @@

 prueba de paquete ;

importar  dominio .*;


public  class  TestSobreescritura1 {
    public  static  void  main ( String [] args ) {
        Empleado  empleado1 = nuevo  Empleado ( "Juan" , 10000 );
        imprimir ( empleado1 );
       // System.out.println("empleado1= "+empleado1.obtenerDetalles());
        empleado1 = nuevo  Gerente ( "José" , 5000 , "Sistemas" );
        imprimir ( empleado1 );
        //Sistema.out.println("gerente1=" + gerente1.obtenerDetalles());
    }

    public  static  void  imprimir ( Empleado  empleado ){
        Cadena  detalles = empleado . obtener detalles ();
        sistema _ fuera _ println ( "detalles= " + detalles );
    }
}
