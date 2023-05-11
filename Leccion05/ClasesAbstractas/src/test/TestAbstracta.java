//Un test para ver como funciona. Aplicamos el polimorfismo
//Funcionalidades para que el codigo sea mas generico, se usa el polimorfismo
package test;

import domain.*;

public class TestAbstracta {
    public static void main(String[] args) {
        FiguraGeometrica figura = new Rectangulo("Rectangulo");
        figura.dibujar();
    }
}

