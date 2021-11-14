import { createGame } from "./game.js";


function removeSessionKeyContainer() {
    document.getElementById("session-key-input-container").remove();
}


async function onclickSessionInputButton() {
    let input = document.getElementById("session-key-input")
    let value = input.value
    let response = await fetch('/sessions?key=' + value);

    if (response.ok) {
        removeSessionKeyContainer()
        createGame()
    }
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
