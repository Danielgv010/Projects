const persona = {
    nombre: "Federico",
    apellidos: "García Lorca",
    edad: 55,
    nacionalidad: "española",
    datosCompletos: function (){
        console.log(`${this.nombre} - ${this.apellidos} - ${this.edad}`);
    }
}

console.log(persona.nombre);

persona.apodo = "El Fede"

console.log(persona.nombre);

persona.datosCompletos();


const persona1 = {}
persona1.nombre = "Jose";
persona1.apellidos = "García";


const persona2 = new Object();
persona2.nombre = "Jose";
persona2.apellidos = "García";


for (let atributo in persona){
    console.log(persona[atributo])
}

console.log("--")

delete persona.apodo;

for (let atributo in persona){
    console.log(persona[atributo])
}

const myObj = {
    name: "John",
    age: 30,
    cars: [
        {name:"Ford",models:["Fiesta","Focus","Mustang"]},
        {name:"BMW",models:["320","X3","X5"]},
        {name:"Fiat",models:["500","Panda"]}
    ]
}

for ( let modelo of myObj.cars[0].models ){
    console.log(modelo)
}

function verElemento(esto){
    console.log(esto)
}