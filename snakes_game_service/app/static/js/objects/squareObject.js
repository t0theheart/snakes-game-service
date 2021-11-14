const canvas = document.getElementById("snakes-game");
const ctx = canvas.getContext("2d");


export class SquareObject {
    constructor(x, y, sideLength, color, borderWidth, borderColor) {
        this.x = x;
        this.y = y;
        this.sideLength = sideLength;
        this.color = color;
        this.borderWidth = borderWidth;
        this.borderColor = borderColor;
    }

    draw() {
        ctx.beginPath();
        ctx.rect(
            this.x + this.borderWidth,
            this.y + this.borderWidth,
            this.sideLength - this.borderWidth * 2,
            this.sideLength - this.borderWidth * 2
        );
        ctx.fillStyle = this.color;
        ctx.strokeStyle = this.borderColor;
        ctx.lineWidth = this.borderWidth;
        ctx.fill();
        ctx.stroke();
        ctx.closePath();
    }

    clear() {
        ctx.clearRect(
            this.x - this.borderWidth,
            this.y - this.borderWidth,
            this.sideLength + this.borderWidth * 2,
            this.sideLength + this.borderWidth * 2
        );
    }
}
