import { Snake } from "./snake.js";
const canvas = document.getElementById("myCanvas");

let x = canvas.width/5;
let y = canvas.height-90;

// const head = new SnakeSquareHead(x, y, 30, "#FF0000", 1, "#000000")
const snake = new Snake(x, y, 30, 2, "#FF0000", 1, "#000000")

// document.addEventListener("keyup", keyUpHandler, false);
//
// function keyUpHandler(e) {
//     console.log(e)
//     if (e.key === "ArrowUp") {
//         head.moveUp()
//     }
//     if (e.key === "ArrowDown") {
//         head.moveDown()
//     }
//     if (e.key === "ArrowRight") {
//         head.moveRight()
//     }
//     if (e.key === "ArrowLeft") {
//         head.moveLeft()
//     }
// }

snake.create()
