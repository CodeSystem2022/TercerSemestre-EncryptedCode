//let persona3 = new Persona ('Carla', 'Ponce'); esto no se debe hacer
class Persona{ //Clase Padre

    static contadorPersonas = 0;  //Atributo estático
    //email = 'Valor default email';     //Atributo no estático

    static get MAX_OBJ(){ // Este método simula una constante
        return 5;
    }
    constructor(nombre, apellido){ 
        this._nombre = nombre; 
        this._apellido = apellido;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersonas;
        }
        else{
            console.log('se ha superado el máximo de objetos permitidos');
        }
        
        //console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
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
        return this.idPersona+' '+this._nombre+' '+ this._apellido;
    }

    toString(){ //Regresa un string
        //se aplica el polimorfismo que significa = múltiples formas en tiempo de ejecución.
        //El método que se ejecuta depende si es una referencia de tipo padre o hija (depende del objeto).
        return this.nombreCompleto();
    }

    // metodo static, metodo que se asocia con nuestra clase 

    static saludar(){
        console.log('saludos desde este metodo static');

    }

    static saludar2(persona){
        console.log(persona.nombre+ ' ' + persona.apellido);
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

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado('Maria', 'Gimenez','Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

// Object.prototype.toString esta es la manera de acceder  a atributos  y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());


//persona1.saludar(); no es funcion, no se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);


Empleado.saludar();
Empleado.saludar2(empleado1)

//console.log(persona1.contadorObjetosPersona); - indefinido
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

console.log(persona1.email); 
console.log(empleado1.email);
//console.log(Persona.email); indefinifinido -  no puede acceder desde loa clase 
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);
let persona3 = new Persona('Carla', 'Pertosi');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10;  No se puede modificar, ni alterar
console.log(Persona.MAX_OBJ);

let persona4 = new Persona('Franco', 'Diaz');
console.log(persona4.toString());
let persona5 = new Persona('Liliana', 'Paz');
console.log(persona5.toString()); // no esta definida Liliana Paz