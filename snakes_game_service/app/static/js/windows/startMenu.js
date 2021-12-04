// import { Game } from "../game.js";
// import { createLobbyContainer } from "./lobbyMenu.js";
import { Connection } from "../connection.js";
import { eventBus } from "../eventBus.js";


let connection = new Connection(eventBus)

eventBus.listen('LOBBY', function (event) {
    console.log('FROM CONSUMER!!!!!!!')
    console.log(event)
})


function removeSessionKeyContainer() {
    document.getElementById("sessions-key-input-container").remove()
}


async function onclickSessionInputButton() {
    let input = document.getElementById("sessions-key-input")
    let sessionId = input.value

    connection.send({sessionId: sessionId})
    removeSessionKeyContainer()
}


function createSessionKeyContainer() {
    let div = document.createElement("div")
    div.id = "sessions-key-input-container"

    let input = document.createElement("input")
    input.type = "text"
    input.size = 40
    input.id = "sessions-key-input"

    let text = document.createElement("div")
    text.innerText = "Input sessions key:"

    let button = document.createElement("button")
    button.innerText = "Enter"
    button.onclick = onclickSessionInputButton

    let buttonDiv = document.createElement("div")
    buttonDiv.style.marginTop = "2%"

    div.appendChild(text)
    div.appendChild(input)
    buttonDiv.appendChild(button)
    div.appendChild(buttonDiv)
    document.body.appendChild(div)
}

createSessionKeyContainer()
