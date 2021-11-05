const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");


export class SquareObject {
    constructor(x, y, sideLength, color) {
        this.x = x;
        this.y = y;
        this.sideLength = sideLength;
        this.color = color;
    }

    draw() {
        ctx.beginPath();
        ctx.rect(this.x, this.y, this.sideLength, this.sideLength);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }

    clear() {
        ctx.clearRect(this.x, this.y, this.sideLength, this.sideLength);
    }
}
