// import { Game } from "../game.js";
import { LobbyTable } from "./lobbyTable.js";
import { Connection } from "../connection.js";
import { eventBus } from "../eventBus.js";


let connection = new Connection(eventBus)
let lobbyTable = new LobbyTable(eventBus)


function removeSessionKeyContainer() {
    document.getElementById("sessions-key-input-container").remove()
}


async function onclickSessionInputButton() {
    let input = document.getElementById("sessions-key-input");
    let sessionId = input.value;
    connection.connect(sessionId);
    removeSessionKeyContainer()
}


function createSessionKeyContainer() {
    let menuDiv = document.createElement("div")
    menuDiv.id = "menu"

    let div = document.createElement("div")
    div.id = "sessions-key-input-container"

    let input = document.createElement("input")
    input.type = "text"
    input.id = "sessions-key-input"

    let text = document.createElement("div")
    text.innerText = "Input sessions key:"

    let button = document.createElement("button")
    button.innerText = "Enter"
    button.onclick = onclickSessionInputButton
    button.classList.add("btn");
    button.classList.add("btn-dark");

    let buttonDiv = document.createElement("div")
    buttonDiv.id = "enter-button-container"

    div.appendChild(text)
    div.appendChild(input)
    buttonDiv.appendChild(button)
    div.appendChild(buttonDiv)
    menuDiv.appendChild(div)
    document.body.appendChild(menuDiv)
}

createSessionKeyContainer()
