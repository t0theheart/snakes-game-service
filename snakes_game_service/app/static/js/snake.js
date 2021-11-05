import { SquareObject } from "./squareObject.js";


export class Snake {
    constructor(x, y, bodySize, bodyLength, bodyColor, borderWidth, borderColor) {
        this.bodySize = bodySize
        this.bodyLength = bodyLength
        this.bodyColor = bodyColor
        this.borderWidth = borderWidth
        this.borderColor = borderColor
        this.body = []
        this.head = null
        this.headX = x
        this.headY = y
        this.createHead()
        this.createStartBody()
    }

    createHead () {
        let head = new SquareObject(this.headX, this.headY, this.bodySize, this.bodyColor, this.borderWidth, this.borderColor)
        this.body.push(head)
    }

    createStartBody () {
        for (let i = this.bodyLength; i > 0; i--) {
            let lastElementY = this.body[this.body.length-1].y + this.bodySize
            let lastElementX = this.body[this.body.length-1].x
            let bodyElement = new SquareObject(lastElementX, lastElementY, this.bodySize, this.bodyColor, this.borderWidth, this.borderColor)
            this.body.push(bodyElement)
        }
    }

    create() {
        this.body.forEach(bodyElement => {
            bodyElement.draw()
        })
    }
}


// export class SnakeSquareHead extends SquareObject {
//     moveUp () {
//         this.clear()
//         this.y = this.y - this.sideLength
//         this.draw()
//     }
//
//     moveDown() {
//         this.clear()
//         this.y = this.y + this.sideLength
//         this.draw()
//     }
//
//     moveRight() {
//         this.clear()
//         this.x = this.x + this.sideLength
//         this.draw()
//     }
//
//     moveLeft() {
//         this.clear()
//         this.x = this.x - this.sideLength
//         this.draw()
//     }
// }