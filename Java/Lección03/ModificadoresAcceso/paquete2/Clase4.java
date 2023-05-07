package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributo privado";
    
    private Clase4(){
        System.out.println("Constructor privado");
    }
    
    //Creamos un constructor public
    public Clase4(String argumento){//Aqui se puede llamar al constructor vacio
        this();
        System.out.println("Constructor publico");
    }
    
    //Método private
    private void metodoPrivado(){
        System.out.println("Método privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
}
