import {eventBus} from "./eventBus.js";

export class Connection {
    constructor() {
        this.eventBus = eventBus;
        this.address = 'ws://127.0.0.1:5000/ws/';
        this.socket = null;
    };

    connect(sessionId, login) {
        this.socket = new WebSocket(this.address + this.generate_id());
        this.socket.onopen = this.onopen(sessionId, login);
        this.socket.onmessage = this.onmessage();
    };

    generate_id() {
        return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    };

    send(data) {
        this.socket.send(JSON.stringify(data));
    };

    onopen(sessionId, login) {
        function wrapper(event) {
            event.target.send(JSON.stringify({sessionId: sessionId, login: login, code: 'CONNECT_TO_SESSION'}))
        }
        return wrapper
    }

    onmessage() {
        let eventBus = this.eventBus;
        function wrapper(event) {
            let message = JSON.parse(event.data);
            eventBus.write(message.code, message);
        }
        return wrapper
    }
}