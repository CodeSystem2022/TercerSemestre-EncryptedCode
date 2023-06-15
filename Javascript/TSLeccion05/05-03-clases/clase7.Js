class Persona{ //Clase Padre
    constructor(nombre, apellido){ 
        this._nombre = nombre; 
        this._apellido = apellido; 
    }
  
    
    get nombre(){
        return this._nombre;
    }
    

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }

    // esta es una funcion oun metodo dentro de la persona clase, va a solicitar elnombre y apellido
    // Conesto lo que vamosa hacer es comprobar que estamos heredando
    //este metodo lo ponemos al final de la clase padre
    nombreCompleto(){
        return this._nombre + ' ' + this._apellido;
    }

    toString(){ //Regresa un string
        //se aplica el polimorfismo que significa = múltiples formas en tiempo de ejecución.
        //El método que se ejecuta depende si es una referencia de tipo padre o hija (depende del objeto).
        return this.nombreCompleto();
    }

}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre,apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = this.departamento;
    }

    //Sobreescritura - metodo ya definido en la clase padre
    //La clase hija aplica el concepto de sobreescritura
    //Modifica el comportamiento definido del metodo de la clase padre.

    nombreCompleto(){ // tiene que ser realmente igual "nombrecompleto" sino seria un nuevo metodo
    
        return super.nombreCompleto()+', '+this._departamento; 
    }
}


//Creamos objetos y los mostramos en consola:

let persona1 = new Persona("Martín", "Perez"); 
persona1.nombre = 'Juan Carlos';   
persona1.apellido = 'Rodriguez';   

let persona2 = new Persona("Carlos","Lara"); 

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');

console.log(empleado1.nombreCompleto()); 

console.log(empleado1.toString());
console.log(persona1.toString()); 