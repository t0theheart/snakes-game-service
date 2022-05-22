import {Game} from "./game.js";
import {eventBus} from "./eventBus.js";
import {connection} from "./connection.js";


export class GameManager {
    constructor() {
        this.eventBus = eventBus;
        this.connection = connection;
        // this.eventBus.listen('CREATE_GAME', this.createGameHandler());
        this.eventBus.listen('START_GAME', this.startGameHandler());
    }

    // createGameHandler() {
    //     let _this = this;
    //     function handler(event) {
    //         let settings = event.message.data.game;
    //         console.log(settings)
    //     }
    //     return handler;
    // }

    startGameHandler() {
        let _this = this;
        function handler() {
            let data = {code: 'START_GAME', sessionId: _this.connection.sessionId};
            _this.connection.send(data);
        }
        return handler;
    }
}
