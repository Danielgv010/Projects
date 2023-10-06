function crearTabla() {
    body = document.getElementsByTagName("body")[0];
    tabla = document.createElement("table");

    let row = document.getElementById("filas").value;
    let column = document.getElementById("columnas").value;
    let border = document.getElementById("borde").checked;
    let color = document.getElementById("color").value;

    console.log(row);
    console.log(column);
    console.log(border);
    console.log(color);

    for (let i = 0; i < row; i++) {
        console.log("It: "+i)
        const fila = document.createElement("tr");
        for (let j = 0; j < column; j++) {
            const columna = document.createElement("td");
            columna.innerHTML = String(i)+String(j);
            fila.appendChild(columna);
        }
        tabla.appendChild(fila);
    }
    
    if (border) {
        tabla.setAttribute("border",1);
        tabla.setAttribute("style","border-color:"+color+";border-collapse:collapse;");
    } else {
        tabla.setAttribute("border",0);
    }

    body.appendChild(tabla);
}