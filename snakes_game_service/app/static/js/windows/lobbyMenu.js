

export function createLobbyContainer(number) {
    let headers = ["Number", "Player", "Color", "Status"]
    let div = document.createElement("div")
    div.id = "lobby-container"

    let table = document.createElement("table")
    table.width = "40%;"

    let tr = table.insertRow();

    headers.forEach(header => {
        let td = tr.insertCell();
        td.innerText = header
    })

    document.body.appendChild(table)

    // for (let i = 0; i < number; i++) {
    //
    // }
}