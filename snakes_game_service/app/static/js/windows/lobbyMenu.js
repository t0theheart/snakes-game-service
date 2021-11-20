

export function createLobbyContainer(users) {

    function createTableHeaders(table, headers) {
        let tr = table.insertRow();
        headers.forEach(header => {
            let td = tr.insertCell();
            td.innerText = header
        })
    }

    let headers = ["Number", "Color", "Status"]
    let table = document.createElement("table")
    table.width = "40%;"
    let div = document.createElement("div")
    div.id = "lobby-container"

    createTableHeaders(table, headers)

    let counter = 0
    users.forEach(user => {
        counter += 1
        let tr = table.insertRow();
        let numberTd = tr.insertCell();
        let colorTd = tr.insertCell();
        let statusTd = tr.insertCell();

        numberTd.innerText = counter
        colorTd.innerText = user['color']
        statusTd.innerText = user['status'] || ''
    })


    document.body.appendChild(table)
}