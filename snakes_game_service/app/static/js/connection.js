

export class Connection {
    constructor() {
        this.socket = null
        this.address = 'ws://127.0.0.1:5000/ws/'
    }

    generate_id() {
        return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15)
    }

    send(data) {
        this.socket.send(data)
    }

    init(sessionId) {
        this.socket = new WebSocket(this.address + this.generate_id());
        this.socket.onopen = function(event) {
            event.target.send(sessionId)
        };
    }
}