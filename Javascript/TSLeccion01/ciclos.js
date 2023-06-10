//Andrea Llavel
//while significa mientras
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;     
}
console.log("Fin del ciclo while");      

//do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;         
}  while(conteo < 3);
  console.log("Fin de ciclo do while");

  //for
  for( let contando = 0; contando < 3; contando++){
    console.log(contando);
  }
  console.log("Fin del ciclo for");

  //Palabra Reservada Break
  for(let contando = 0; contando < 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);
        break;
    }
  }
  console.log("Termina el ciclo al encontrar el primer numero par");

  //Palabra Reservada Continue y Etiquetas Labels
  inicio:
  for(let contando = 0; contando < 10; contando++){
    if(contando % 2 !== 0){
        break inicio;   //ir a la siguiente interacion   
    }
    console.log(contando);
  }
  console.log("Termina el ciclo ");

  
//Etiquetas Labels no estan recomendadas, pero conocerlas y saber el funcionamiento 
//para cambiar el programa para encontrar otras soluciones.
