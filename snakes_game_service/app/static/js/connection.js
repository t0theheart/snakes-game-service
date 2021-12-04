

export class Connection {
    constructor(eventBus) {
        this.eventBus = eventBus;
        this.address = 'ws://127.0.0.1:5000/ws/';
        this.socket = new WebSocket(this.address + this.generate_id());
        this.socket.onmessage = this.onmessage();
    };

    generate_id() {
        return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    };

    send(data) {
        this.socket.send(JSON.stringify(data));
    };

    onmessage() {
        let eventBus = this.eventBus;
        function wrapper(event) {
            let message = JSON.parse(event.data);
            if (message.code === 'LOBBY') {
                eventBus.write('LOBBY', message)
            }
        }
        return wrapper
    }
}