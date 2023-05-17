let x = 10;

console.log(x.length);

//objeto

let persona = {
    nombre: "carlos",
    apellido:"gil",
    email:"cgil@gmail.com",
    edad:30,
    //funcion o metodo
    nombreCompleto: function(){
        return this.nombre+" "+this.apellido;
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
