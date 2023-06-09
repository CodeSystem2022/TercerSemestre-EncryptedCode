//Andrea Llavel Issue JavaBeans semana de Scrum Master Rocio Pulitta
package domain;

import java.io.Serializable;   //Serializable: significa convertir nuestro objeto a ceros y unos

public class Persona implements Serializable {
    private String nombre;
    private String apellido;
    //Constructor vacio : esto es obligatorio
    public Persona(){
    }
    //No es obligatorio
    public Persona(String nombre, String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
        }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
                                                                                      
}
