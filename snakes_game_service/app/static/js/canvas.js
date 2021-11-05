import { SnakeSquareHead } from "./snake.js";
const canvas = document.getElementById("myCanvas");

let x = canvas.width/5;
let y = canvas.height-30;

const head = new SnakeSquareHead(x, y, 30, "#FF0000")

document.addEventListener("keyup", keyUpHandler, false);

function keyUpHandler(e) {
    console.log(e)
    if (e.key === "ArrowUp") {
        head.moveUp()
    }
    if (e.key === "ArrowDown") {
        head.moveDown()
    }
    if (e.key === "ArrowRight") {
        head.moveRight()
    }
    if (e.key === "ArrowLeft") {
        head.moveLeft()
    }
}

head.draw()
