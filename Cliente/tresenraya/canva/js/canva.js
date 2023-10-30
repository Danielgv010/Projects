onload = start;

const game = {
    board: [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    turn: true,
    numberPlays: 0,
    gameEnded: false
}

let canvas, context, width, height, turn = 2;
const coordinates = [100, 300, 500];

function start(argument) {
    canvas = document.getElementById("my-canvas")

    context = canvas.getContext("2d");

    width = canvas.width;
    height = canvas.height;

    drawBoard();


    //Añade un evento para capturar los clicks en el canvas
    canvas.addEventListener("click", function (event) { play(event) });
}

function drawBoard() {
    //Crea un rectangulo relleno color gris
    // Dos primeros parametros son las coordenadas de la esquina arriba-izquierda
    // Dos últimos parametros son el ancho y el alto del rectangulo
    context.fillStyle = "gray";
    context.fillRect(0, 0, width, height);

    //Crea nueve circulos blancos
    for (xCenter of coordinates) {
        for (yCenter of coordinates) {
            drawCircle(xCenter, yCenter, "white");
        }
    }
}

function drawCircle(xCenter, yCenter, color) {
    //Crear un circulo con los parámetros coordenadas del centro, radio, inicio y fin del arco
    context.fillStyle = color;
    context.beginPath();
    context.arc(xCenter, yCenter, 90, 0, Math.PI * 2);
    context.closePath();
    context.fill();
}

function play(event) {
    console.log("cykanahui")
    console.log(!gameStatus())
    if (!gameStatus()) {
        let x = Math.trunc((event.clientX - canvas.getBoundingClientRect().left) / 100); //Obtiene la coordenada X donde pulso el jugador en el canvas
        let y = Math.trunc((event.clientY - canvas.getBoundingClientRect().top) / 100); //Obtiene la coordenada Y donde pulso el jugador en el canvas

        if (x == 1) {
            x = 0
        } else if (x == 2 || x == 3) {
            x = 1
        } else if (x == 4 || x == 5) {
            x = 2
        }

        if (y == 1) {
            y = 0
        } else if (y == 2 || y == 3) {
            y = 1
        } else if (y == 4 || y == 5) {
            y = 2
        }

        if (game.board[y][x] == 0) {
            game.board[y][x] = turn;

            if (turn == 1) {
                turn++;
            } else {
                turn--;
            }

            drawPieces();
            game.numberPlays++;

            if (checkWin()) {
                document.getElementById("result").innerHTML = `Winner Winner Chicken Dinner! Player ${turn}`
            }

        } else {
            alert("That space is already set")
        }
    }
}

function drawPieces() {
    let color;
    game.board.forEach((row, y) => {
        row.forEach((value, x) => {
            if (value != 0) {
                if (value == 1) {
                    color = "red";
                } else if (value == 2) {
                    color = "yellow";
                }
                drawCircle(coordinates[x], coordinates[y], color);
            }
        })
    })
}

function gameStatus() {
    if (!checkWin() && game.numberPlays > 4) {
        game.board.forEach((row) => {
            row.forEach((value) => {
                if (value == 0) {
                    return false;
                } else {
                    return true;
                }
            })
        })
    } else {
        return false;
    }
}

function checkWin() {
    if (checkRows() || checkColumns() || checkDiagonal()) {
        return true;
    } else {
        return false;
    }
}

function checkRows() {
    if (game.board[0][0] == game.board[0][1] && game.board[0][1] == game.board[0][2] && game.board[0][0] != "") {
        return true;
    }
    if (game.board[1][0] == game.board[1][1] && game.board[1][1] == game.board[1][2] && game.board[1][0] != "") {
        return true;
    }
    if (game.board[2][0] == game.board[2][1] && game.board[2][1] == game.board[2][2] && game.board[2][0] != "") {
        return true;
    }
    return false;
}

function checkColumns() {
    if (game.board[0][0] == game.board[1][0] && game.board[1][0] == game.board[2][0] && game.board[0][0] != "") {
        return true;
    }
    if (game.board[0][1] == game.board[1][1] && game.board[1][1] == game.board[2][1] && game.board[0][1] != "") {
        return true;
    }
    if (game.board[0][2] == game.board[1][2] && game.board[1][2] == game.board[2][2] && game.board[0][2] != "") {
        return true;
    }
    return false;
}

function checkDiagonal() {
    if (game.board[0][0] == game.board[1][1] && game.board[1][1] == game.board[2][2] && game.board[0][0] != "") {
        return true;
    }
    if (game.board[0][2] == game.board[1][1] && game.board[1][1] == game.board[2][0] && game.board[0][2] != "") {
        return true;
    }
    return false;
}