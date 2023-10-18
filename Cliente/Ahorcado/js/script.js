const barrasH1 = document.getElementById("barras");
const palabras = ["agua", "teclado", "pantalla", "rojo"];
const botones = document.getElementsByClassName("button");
let palabra = "";
let barras = "";
let contador = 1;

crearPalabra();

function comprobar(letra) {
    let barrasnew = "";

    if (palabra.includes(letra)) {
        for (i in palabra) {
            if (letra == palabra[i]) {
                barrasnew += letra;
            } else {
                barrasnew += barras[i];
            }
        }
        barras = barrasnew;
        barrasH1.innerHTML = barras;
        cambioBoton("#C1E1C1", letra);
    } else {
        contador++;
        cambioBoton("#FF0000", letra);
        document.getElementById("imgAhorcado").setAttribute("src", `img/${contador}.png`)
    }

    if (!comprobarVictoria()) {
        alert("Victoria");
        disableAll();
    } else if (comprobarDerrota()) {
        alert("Derrota");
        disableAll();
    }
}

function cambioBoton(color, id) {
    const boton = document.getElementById(id);
    boton.disabled = true;
    boton.style.background = color;
}

function comprobarVictoria() {
    return barras.includes("_");
}

function comprobarDerrota() {
    return contador == 7 ? true : false;
}

function disableAll() {
    for (i in botones) {
        botones[i].disabled = true;
    }
}

function crearPalabra() {
    let col3 = document.getElementById("col3");

    palabra = palabras[Math.floor(Math.random() * 4)];

    console.log(palabra);

    for (i in palabra) {
        barras += "_";
    }
    barrasH1.innerHTML = barras;
}