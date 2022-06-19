import { Snake } from "./objects/snake.js";


export class Game {
    constructor(canvasId, width, height) {
        this.canvas = document.getElementById(canvasId)
        this.width = width
        this.height = height
        this.player = null
    }

    initGameField() {
        this.canvas.width = this.width
        this.canvas.height = this.height
    }

    initPlayer(body, bodyColor) {
        this.player = new Snake(body, 30, 2, bodyColor, 1, "#000000")

        function keyUpHandler(snake) {
            function f(e) {
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
            return f
        }

        document.addEventListener("keyup", keyUpHandler(this.player), false)
        this.player.create()
    }

    start() {
        this.initGameField()
    }
}