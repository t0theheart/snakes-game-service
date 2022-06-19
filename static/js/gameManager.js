import {Game} from "./game.js";
import {eventBus} from "./eventBus.js";
import {connection} from "./connection.js"


export class GameManager {
    constructor() {
        this.eventBus = eventBus;
        this.connection = connection;
        this.eventBus.listen('START_GAME', this.startGameHandler());
        this.eventBus.listen('GAME_STARTED', this.gameStartedHandler());
    }

    gameStartedHandler() {
        let _this = this;
        function handler(event) {
            let settings = event.message.data.game;
            let game = new Game('snakes-game', settings.width, settings.height);

            // todo think how to destroy lobby elem
            let elem = document.getElementById('lobby-table');
            elem.parentNode.removeChild(elem);

            game.start()
            settings.players.forEach(player => {
                console.log('player', player)
                game.initPlayer(player.body, player.color)
            })
        }
        return handler;
    }

    startGameHandler() {
        let _this = this;
        function handler() {
            let data = {code: 'START_GAME', sessionId: _this.connection.sessionId};
            _this.connection.send(data);
        }
        return handler;
    }
}
