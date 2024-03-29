import { SquareObject } from "./squareObject.js";


export class Snake {
    constructor(body, bodySize, bodyLength, bodyColor, borderWidth, borderColor) {
        this.bodySize = bodySize
        this.bodyLength = bodyLength
        this.bodyColor = bodyColor
        this.borderWidth = borderWidth
        this.borderColor = borderColor
        this.body = []
        this.createStartBody(body)

        this.moveMap = {
            up: {x: 0, y: -this.bodySize},
            down: {x: 0, y: this.bodySize},
            right: {x: this.bodySize, y: 0},
            left: {x: -this.bodySize, y: 0}
        }
    }

    createStartBody(body) {
        console.log('head', body[0])
        let head = new SquareObject(body[0][0], body[0][1], this.bodySize, this.bodyColor, this.borderWidth, this.borderColor)
        this.body.push(head)
        for (let i = 1; i < body.length; i++) {
            console.log('i', body[i])
            let bodyElement = new SquareObject(body[i][0], body[i][1], this.bodySize, this.bodyColor, this.borderWidth, this.borderColor)
            this.body.push(bodyElement)
        }
    }

    create() {
        this.body.forEach(bodyElement => {bodyElement.draw()})
    }

    getLastBodyElement() {
        return this.body[this.body.length-1]
    }

    getFirstBodyElement() {
        return this.body[0]
    }

    moveLastBodyElementToFirstBodyElement() {
        let lastBodyElement = this.body.pop()
        this.body.unshift(lastBodyElement)
    }

    moveUp () {
        let move = this.moveMap["up"]
        this.move(move.x, move.y)
    }

    moveDown() {
        let move = this.moveMap["down"]
        this.move(move.x, move.y)
    }

    moveRight() {
        let move = this.moveMap["right"]
        this.move(move.x, move.y)
    }

    moveLeft() {
        let move = this.moveMap["left"]
        this.move(move.x, move.y)
    }

    move(x, y) {
        let lastBodyElement = this.getLastBodyElement()
        let firstBodyElement = this.getFirstBodyElement()
        lastBodyElement.clear()
        lastBodyElement.x = firstBodyElement.x
        lastBodyElement.y = firstBodyElement.y
        lastBodyElement.x = lastBodyElement.x + x
        lastBodyElement.y = lastBodyElement.y + y
        lastBodyElement.draw()
        this.moveLastBodyElementToFirstBodyElement()
    }
}