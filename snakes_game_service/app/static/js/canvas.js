import { Snake } from "./snake.js";
const canvas = document.getElementById("myCanvas");

let x = canvas.width/5;
let y = canvas.height-90;

const snake = new Snake(x, y, 30, 2, "#FF0000", 1, "#000000")

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
