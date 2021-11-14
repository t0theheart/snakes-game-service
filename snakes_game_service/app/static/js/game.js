import { Snake } from "./snake.js";

export function createGame() {
    let canvas = document.getElementById("snakes-game")
    canvas.width = 1500
    canvas.height = 900

    let x = canvas.width/5;
    let y = canvas.height-90;

    let snake = new Snake(x, y, 30, 2, "#FF0000", 1, "#000000")

    document.addEventListener("keyup", keyUpHandler, false);

    function keyUpHandler(e) {
        console.log(e)
        if (e.key === "ArrowUp") {
            snake.moveUp()
        }
        if (e.key === "ArrowDown") {
            snake.moveDown()
        }
        if (e.key === "ArrowRight") {
            snake.moveRight()
        }
        if (e.key === "ArrowLeft") {
            snake.moveLeft()
        }
    }

    snake.create()
}