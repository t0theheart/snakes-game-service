import { Game } from "../game.js";
import { createLobbyContainer } from "./lobbyMenu.js";


function removeSessionKeyContainer() {
    document.getElementById("session-key-input-container").remove()
}


async function onclickSessionInputButton() {
    let input = document.getElementById("session-key-input")
    let session = input.value

    async function enterToSession(session) {
        let response = await fetch('/sessions/' + session + '/users', {
            method: 'POST',
            headers: {'Content-Type': 'application/json;charset=utf-8'},
            body: {}
        });

        if (response.ok) {
            return true
        }

    }

    async function getSessionUsers(session) {
        let response = await fetch('/sessions/' + session + '/users');

        if (response.ok) {
            return (await response.json()).users
        }
    }

    let isEntered = enterToSession(session)

    if (isEntered) {
        let users = await getSessionUsers(session)
        removeSessionKeyContainer()
        createLobbyContainer(users)
    }


    // if (response.ok) {
    //     removeSessionKeyContainer()
    //     let sessionData = await response.json()
    //     let gameData = sessionData.game
    //     createLobbyContainer()
    //     // let game = new Game("snakes-game", gameData.width, gameData.height)
    //     // game.start()
    // }
}


function createSessionKeyContainer() {
    let div = document.createElement("div")
    div.id = "session-key-input-container"

    let input = document.createElement("input")
    input.type = "text"
    input.size = 40
    input.id = "session-key-input"

    let text = document.createElement("div")
    text.innerText = "Input session key:"

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
