

export class LobbyTable {
    constructor(eventBus) {
        this.root = document.createElement("div");
        this.root.id = 'lobby-table'
        this.headers = ['№', 'ID', 'Status', 'Color'];
        this.elements = {};
        this.insertRowIndex = 0;
        this.eventBus = eventBus;
        this.eventBus.listen('ENTER_LOBBY', this.enterLobbyHandler());
        this.eventBus.listen('NEW_PLAYER_ENTER_LOBBY', this.newPlayerEnterLobbyHandler());
    };

    destroy() {
        let elem = document.getElementById(this.root.id);
        elem.parentNode.removeChild(elem);
    }

    newPlayerEnterLobbyHandler() {
        let _this = this;
        function handler(event) {
            let user = event.message.data;
            _this.insertUser(user)
        }
        return handler;
    }

    enterLobbyHandler() {
        let _this = this;
        function handler(event) {
            let session = event.message.session;
            let user = event.message.user;
            let usersAmount = session.usersAmount;
            _this.createTable(usersAmount);
            session.users.forEach(user => {
                _this.insertUser(user);
            })
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
        ]
        this.insertRow(userArray)
        this.insertRowIndex += 1;
    }

    insertRow(array) {
        let row = this.elements.table.rows[this.insertRowIndex];
        let cells = row.cells;
        for (let i = 0; i < cells.length; i++) {
            cells[i].innerText = array[i];
        }
    };
}