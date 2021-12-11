

export class LobbyTable {
    constructor(eventBus) {
        this.eventBus = eventBus;
        this.headers = ['№', 'ID', 'Status', 'Color'];
        this.table = null;
        this.insertRowIndex = 0;
        this.eventBus.listen('ENTER_LOBBY', this.enterLobbyHandler());
        this.eventBus.listen('NEW_PLAYER_ENTER_LOBBY', this.newPlayerEnterLobby());
    };

    newPlayerEnterLobby() {
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
            let data = event.message.data;
            let usersAmount = data.usersAmount;
            _this.createTable(usersAmount);
            data.users.forEach(user => {
                _this.insertUser(user);
            })
        }
        return handler;
    };

    createTable(rowsAmount) {
        this.table = document.createElement("table");
        document.body.appendChild(this.table);
        let columnsAmount = this.headers.length;
        rowsAmount += 1;
        for (let i = 0; i < rowsAmount; i++) {
            let tr = this.table.insertRow();
            for (let j = 0; j < columnsAmount; j++) {
                let cell = tr.insertCell();
                if (j === 0) {
                    cell.innerText = i + '';
                }
            }
        }
        this.insertRow(this.headers);
        this.insertRowIndex += 1;
    };

    insertUser(user) {
        let userArray = [
            this.insertRowIndex,
            user.userId,
            user.status,
            user.color
        ]
        this.insertRow(userArray)
        this.insertRowIndex += 1;
    }

    insertRow(array) {
        let row = this.table.rows[this.insertRowIndex];
        let cells = row.cells;
        for (let i = 0; i < cells.length; i++) {
            cells[i].innerText = array[i];
        }
    };
}