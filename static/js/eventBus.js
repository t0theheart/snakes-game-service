

class EventBus {
    constructor() {
        this.elem = document.getElementById('event-bus')
    }

    listen(code, handler) {
        document.addEventListener(code, handler);
    }

    write(code, message) {
        let event = new Event(code, {bubbles: true});
        event.message = message
        this.elem.dispatchEvent(event);
    }
}

export const eventBus = new EventBus();