

export class LobbyTable {
    constructor(eventBus) {
        this.eventBus = eventBus;
        this.headers = ['№', 'ID', 'Color', 'Status'];
        this.table = null;

        this.eventBus.listen('ENTER_LOBBY', this.enterLobbyHandler());
    };

    enterLobbyHandler() {
        let _this = this;

        function handler(event) {
            let data = event.message.data;
            let usersAmount = data.usersAmount;
            _this.createTable(usersAmount);
        }

        return handler;
    };

    createTable(rowsAmount) {
        this.table = document.createElement("table");
        document.body.appendChild(this.table);

        let columnsAmount = this.headers.length;
        rowsAmount += 1; // for header

        for (let i = 0; i < rowsAmount; i++) {
            let tr = this.table.insertRow();
            for (let j = 0; j < columnsAmount; j++) {
                tr.insertCell();
            }
        }

        this.insertRow(0, this.headers);
    };

    insertRow(index, data) {
        let row = this.table.rows[index];
        let cells = row.cells;
        for (let i = 0; i < cells.length; i++) {
            cells[i].innerText = data[i];
        }
    };
}