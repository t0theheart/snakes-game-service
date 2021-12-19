

export class LobbyTable {
    constructor(eventBus) {
        this.root = document.createElement("div");
        this.root.id = 'lobby-table'
        this.headers = ['№', 'ID', 'Status', 'Color'];
        this.elements = {};
        this.insertRowIndex = 0;
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
            let users = event.message.data.session.users;
            let user = event.message.data.user;
            let usersAmount = event.message.data.session.usersAmount;
            _this.createTable(usersAmount);
            for (let key in users) {
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
        this.insertRow(this.headers);
        this.insertRowIndex += 1;

        this.root.appendChild(this.elements.table);
    };

    createStartButton() {
        this.elements['startButton'] = document.createElement("button");
        this.elements['startButton'].innerText ='Start';
        this.elements['startButton'].onclick = (event) => {
            this.destroy();
            // this.eventBus.write('CREATE_GAME_FIELD', {});
        };
        this.root.appendChild(this.elements['startButton']);
    }

    insertUser(user) {
        let userArray = [
            this.insertRowIndex,
            user.id,
            user.status,
            user.color
        ];
        this.insertRow(userArray)
        this.insertRowIndex += 1;
    }

    removeUser(user) {
        console.log(user)
        console.log(this.elements.table)
        let rows = Array.from(this.elements.table.rows);
        let columnsAmount = this.headers.length;
        rows.forEach(row => {
            if (row.cells[1].innerText === user.id) {
                for (let i = 1; i < columnsAmount; i++) {
                    row.cells[i].innerText = '';
                }
            }
        })
        this.insertRowIndex -= 1;
    }

    insertRow(array) {
        let row = this.elements.table.rows[this.insertRowIndex];
        let cells = row.cells;
        for (let i = 0; i < cells.length; i++) {
            cells[i].innerText = array[i];
        }
    };
}