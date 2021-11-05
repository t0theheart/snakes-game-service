import { SquareObject } from "./squareObject.js";


export class SnakeSquareHead extends SquareObject {
    moveUp () {
        this.clear()
        this.y = this.y - this.sideLength
        this.draw()
    }

    moveDown() {
        this.clear()
        this.y = this.y + this.sideLength
        this.draw()
    }

    moveRight() {
        this.clear()
        this.x = this.x + this.sideLength
        this.draw()
    }

    moveLeft() {
        this.clear()
        this.x = this.x - this.sideLength
        this.draw()
    }
}