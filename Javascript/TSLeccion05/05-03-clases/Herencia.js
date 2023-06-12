//Clase 6. Andrea Llavel. Herencia.
//let persona3 = new Persona('Carla', 'Ponce');
//No funciona lo que es el hoisting, no se puede crear un objeto antes de haber
//definido o inicializado la clase que le permite hacer la instancia.
//No se permite antes de que este la clase creada , que permite hacer la instancia,
//no se aplica el conceto de hoisting. Persona in not defened
class Persona{      //Clase Padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
    //Luis Mayorga Carga metodo get y set
//Metodo Get
    get apellido(){
       // return this._nombre;
        return this._apellido;
    }
//Metodo Set
    set apellido(apellido){
        //this._nombre = nombre;
        this._apellido = apellido;

}
}
//Herencia Clase 6. Andrea Llavel
class Empleado extends Persona{    //Clase Hija
     constructor(nombre, apellido, departamento){
     super(nombre, apellido, departamento);    
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this.departamento = departamento;
    }
}
let persona1 = new Persona('Martin', 'Perez');
//console.log(persona1); 
//persona1.nombre = 'Juan Carlos';
//console.log(persona1.nombre);
//console.log(persona1); 
console.log(persona1.apellido);
persona1.apellido = 'Perez';
console.log(persona1.apellido);  
let persona2 = new Persona('Carlos','Lara');
//console.log(persona2); 
//console.log(persona2.nombre);
//persona2.nombre = 'Carlos';
//console.log(persona2);   
console.log(persona2.apellido);
persona2.apellido = 'Santillan';
console.log(persona2.apellido);
//Herencia . Clase 6 .Andrea Llavel
let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
//Falta llamar a super de constructor, que viene de la clase anterior y se accede
//desde el 'this' ; o retorna de un constructor derivado.
console.log(empleado1);
//get nombre no existe en la clase empleado ,este se esta heredando
console.log(empleado1._nombre);
//Podemos acceder a todo lo que nosotros queramos de clase padre: apellido,
//nombre,etc
