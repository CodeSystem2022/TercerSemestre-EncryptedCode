Let persona3 = new Persona ('Carla', 'Ponce');
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido() {
        return this._apellido;
  }

    set apellido(nuevoApellido) {
        this._apellido = nuevoApellido;
  }

}


class Empleado extends Persona{
    constructor(departamento){
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }
    set departamento(){
        this._departamento = departamento;
    }
}
    Let persona1 = new Persona ('Martin', 'Perez');
    console.log(persona1.nombre);
    console.log(persona.apellido); 
    persona1.nombre = 'Juan Carlos';
    persona1.apellido = 'Perez';
    console.log(persona1.nombre);
    //console.log(persona1);
    Let persona2 = new Persona ('Carlos', 'Lara');
    console.log(persona2.nombre); Carlos
    persona2.nombre= 'María Laura';
    console.log(persona2);
    //console.log(persona2);


Let empleado1 = new Empleado('María', 'Gimenez', 'Sistemas')
console.log(empleado1);
console.log(empleado.nombre);
