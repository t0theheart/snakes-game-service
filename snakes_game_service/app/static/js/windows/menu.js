import { Connection } from "../connection.js";
import { LobbyTable } from "./lobbyTable.js";


export class Menu {
    constructor() {
        this.root = document.createElement("div");
        this.root.id = 'enter-lobby-menu';
        this.elements = {};
        this.connection = new Connection();
        this.lobby = new LobbyTable();
    };

    onclickSessionInputButton(login) {
        let _this = this;
        function handler(event) {
            let sessionId = _this.elements.input.value;
            _this.connection.connect(sessionId, login);
            _this.destroy();
        }
        return handler
    }

    create(login) {
        this.root.classList.add('menu')
        let div = document.createElement("div")
        div.id = "sessions-key-input-container"
        let input = document.createElement("input")
        input.type = "text"
        input.id = "sessions-key-input"
        let text = document.createElement("div")
        text.innerText = "Input sessions key:"
        let button = document.createElement("button")
        button.innerText = "Enter"
        button.onclick = this.onclickSessionInputButton(login);
        button.classList.add("btn");
        button.classList.add("btn-dark");
        let buttonDiv = document.createElement("div")
        button.classList.add("button-container");

        this.elements.input = input;
        this.elements.button = button;

        div.appendChild(text)
        div.appendChild(input)
        buttonDiv.appendChild(button)
        div.appendChild(buttonDiv)
        this.root.appendChild(div)
        document.body.appendChild(this.root)
    }

    destroy() {
        document.getElementById("enter-lobby-menu").remove()
    }
}