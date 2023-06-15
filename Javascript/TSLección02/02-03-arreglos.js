// leccion subida por Roberto Perez

//let autos = new Array('Ferrari', 'Renault', 'BMW');
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

//recorremocs los elementos de un arreglo

console.log(autos[0]);

for(let i=0; i < autos.length;i++){
console.log(i+ ' : '+autos[i]);
};

// Modificamos los elementos del arreglo
autos[1] = 'Citroen';
// Agregamos nuevos elementos al arreglo

autos.push('Audi');// el elemento se agrega al final
console.log(autos);

//Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Plymouth';
console.log(autos);

//Como preguntar si es un arreglo
console.log(Array.isArray(autos));//Devuelve booleano