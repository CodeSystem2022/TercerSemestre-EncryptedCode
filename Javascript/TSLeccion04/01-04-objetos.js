let x = 10;

console.log(x.length);

//objeto

let persona = {
    nombre: "carlos",
    apellido:"gil",
    email:"cgil@gmail.com",
    edad:28,
    idioma:"es",
    get lang(){
        return this.idioma.toUpperCase();//toUpperCase(); para pasar el string en mayuscula
    },
    set lang(lang){
     this.idioma = lang.toUpperCase();   
    },
    //funcion o metodo
    nombreCompleto: function(){
        return this.nombre+" "+this.apellido;
    },
    //metodo get:obtener
    get nombreEdad(){
        return "el nombre es: "+this.nombre+", edad: "+this.edad;
    }
   

}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona);

console.log(persona.nombreCompleto());
//otra forma de crear objetos
let persona2 = new Object();
persona2.nombre = "juan";
persona2.direccion = "salada 14";
persona2.telefono =  "441134646";
console.log(persona2.telefono);

//accedemos como si fuera un arreglo
console.log(persona["apellido"]);

//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
 

//agregar una nueva propiedad al objeto
persona.apellido2 = "betancud";
console.log(persona);
//borrar  propiedades del objeto
delete persona.apellido2;

//cambiamos dinamicamente el valor del objeto
persona.apellido = "betancud";
console.log(persona);

//distintas formas de imprimir un objeto
// 1 concatenar
console.log(persona.nombre+" "+persona.apellido);

//2 atraves del  ciclo for in
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}
//3 LA FUNCION OBJECT.VALUES()

let personaArray = Object.values(persona);
console.log(personaArray);

//4 utilizaremos JSON.stringify : lo convierte en una cadena

let personaString = JSON.stringify(persona);
console.log(personaString)


//get obtener y set modificar
console.log("comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("comenzamos  con el metodo get y set  para idiomas");
persona.lang = "en";
console.log(persona.lang);


function Persona3(nombre, apellido, email){//constructor
    this.nombre=nombre;
    this.apellido =apellido;
    this.email=email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre =  new Persona3("leo", "lopez","lopez@gmail.com");
padre.telefono ="546434343";//propiedad esclusiba objeo padre
console.log(padre); 
//ulizamos la funcion
console.log(padre.nombreCompleto());
let madre = new Persona3("laura","contreras","contrerasQgmail.com");
console.log(madre);
console.log(madre.nombreCompleto());

//diferentes formas de crear objetos
//1
let miObjeto = new Object();
//2, recomendada y mas usada
let miObjeto2 = {};
// caso string 1
let miCadena1 = new String("hola");
//caso string 2
let miCadena2 = "hola";
//caso numero 1
let miNumero = new Number(1);
//caso numero 2
let miNumero2= 1;
//caso boolean 1
let miBoolean= new Boolean(false);
//caso boolean 2
let miBoolean2 = false;
//aray 1
let miArray = new Array();
//array 2
let miArray2 = [];
//funciones 1
let miFuncion = new function(){};
//funciones2
let miFuncion2 =function(){};


//uso prototype; se usa para agregar a propiedd a todo  metodo
Persona3.prototype.telefono ="43435435435434";
console.log(padre);
console.log(madre.telefono);
madre.telefono ="666653135434";
console.log(madre.telefono);

//uso call; para agregar funciones o propiedades que tenga otro objeto

let persona4 = {
    nombre:"juan",
    apellido:"perez",
    nombreCompleto2: function(titulo, telefono){
      return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;  
      //return this.nombre+" "+this.apellido;
    }
}
let persona5 = {
    nombre:"carlos",
    apellido:"lara"

}
console.log(persona4.nombreCompleto2("lic.","4131313131313"));
console.log(persona4.nombreCompleto2.call(persona5,"ing.","211002544252"));

//metodo apply
let arreglo=["ing","000111221.."];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));

