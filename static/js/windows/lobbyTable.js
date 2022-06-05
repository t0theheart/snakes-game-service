import {eventBus} from "../eventBus.js";

export class LobbyTable {
    constructor() {
        this.root = document.createElement("div");
        this.root.id = 'lobby-table'
        this.headers = ['№', 'Login', 'Status', 'Color'];
        this.elements = {};
        this.eventBus = eventBus;
        this.eventBus.listen('ENTER_LOBBY', this.enterLobbyHandler());
        this.eventBus.listen('PLAYER_ENTER_LOBBY', this.playerEnterLobbyHandler());
        this.eventBus.listen('PLAYER_LEAVE_LOBBY', this.playerLeaveLobbyHandler());
    };

    destroy() {
        let elem = document.getElementById(this.root.id);
        elem.parentNode.removeChild(elem);
    }

    playerEnterLobbyHandler() {
        let _this = this;
        function handler(event) {
            let user = event.message.data.user;
            _this.insertUser(user)
        }
        return handler;
    }

    playerLeaveLobbyHandler() {
        let _this = this;
        function handler(event) {
            let user = event.message.data.user;
            _this.removeUser(user)
        }
        return handler;
    }

    enterLobbyHandler() {
        let _this = this;
        function handler(event) {
            let users = event.message.data.users;
            let user = event.message.data.user;
            let usersAmount = users.length;
            _this.createTable(usersAmount);
            for (let key in users) {
                if (users[key] !== null)
                    _this.insertUser(users[key]);
            }
            if (user.status === 'HOST') {
                _this.createStartButton();
            }
            document.body.appendChild(_this.root);
        }
        return handler;
    };

    createTable(rowsAmount) {
        this.elements.table = document.createElement("table");
        this.elements.table.classList.add("table");
        this.elements.table.classList.add("table-bordered");
        this.elements.table.classList.add("border-dark");
        let columnsAmount = this.headers.length;
        rowsAmount += 1;
        for (let i = 0; i < rowsAmount; i++) {
            let tr = this.elements.table.insertRow();
            for (let j = 0; j < columnsAmount; j++) {
                let cell = tr.insertCell();
                if (j === 0) {
                    cell.innerText = i + '';
                }
            }
        }
        this.insertRow(0, this.headers);

        this.root.appendChild(this.elements.table);
    };

    createStartButton() {
        this.elements['startButton'] = document.createElement("button");
        this.elements['startButton'].innerText ='Start';
        this.elements['startButton'].classList.add("btn");
        this.elements['startButton'].classList.add("btn-dark");
        this.elements['startButton'].onclick = (event) => {
            this.eventBus.write('START_GAME', {});
        };
        this.root.appendChild(this.elements['startButton']);
    }

    insertUser(user) {
        let index = user.slot + 1;
        let userArray = [
            index,
            user.login,
            user.status,
            user.color
        ];
        this.insertRow(index, userArray);
    }

    removeUser(user) {
        let index = user.slot + 1;
        let row = this.elements.table.rows[index];
        let columnsAmount = this.headers.length;
        for (let i = 1; i < columnsAmount; i++) {
            row.cells[i].innerText = '';
        }
    }

    insertRow(index, array) {
        let row = this.elements.table.rows[index];
        let cells = row.cells;
        for (let i = 0; i < cells.length; i++) {
            cells[i].innerText = array[i];
        }
    };
}