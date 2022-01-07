import { Menu } from "./menu.js";


export class Login {
    constructor() {
        this.root = document.createElement("div");
        this.root.id = 'login';
        this.elements = {};
        this.login = null;
        this.menu = new Menu();
    };

    onclickLogin() {
        let _this = this;
        function handler(event) {
            let login = _this.elements.input.value;
            _this.destroy();
            _this.menu.create(login);
        }
        return handler
    }

    create() {
        this.root.classList.add('menu')
        let input = document.createElement("input")
        input.type = "text"
        let text = document.createElement("div")
        text.innerText = "Enter your login:"
        let button = document.createElement("button")
        button.innerText = "Login"
        button.onclick = this.onclickLogin();
        button.classList.add("btn");
        button.classList.add("btn-dark");
        let buttonDiv = document.createElement("div")
        button.classList.add("button-container");
        this.elements.button = button;
        this.elements.input = input;
        buttonDiv.appendChild(button)
        this.root.appendChild(text)
        this.root.appendChild(input)
        this.root.appendChild(buttonDiv)

        document.body.appendChild(this.root)
    }

    destroy() {
        document.getElementById("login").remove()
    }

}
