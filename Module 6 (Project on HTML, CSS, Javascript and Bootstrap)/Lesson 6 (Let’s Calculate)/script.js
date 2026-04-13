const historyElement = document.getElementById("history");
const outputElement = document.getElementById("output");

let currentInput = "";
let historyInput = "";

function updateDisplay() {
    outputElement.innerText = currentInput || "0";
    historyElement.innerText = historyInput;
}

document.getElementById("keyboard").addEventListener("click", (e) => {
    const target = e.target;
    if (target.tagName !== "BUTTON") return;

    const value = target.innerText;
    const id = target.id;

    if (target.classList.contains("number")) {
        handleNumber(value);
    } else if (target.classList.contains("operator")) {
        handleOperator(id, value);
    }

    updateDisplay();
});

function handleNumber(num) {
    if (currentInput === "0") {
        currentInput = num;
    } else {
        currentInput += num;
    }
}

function handleOperator(id, label) {
    switch (id) {
        case "clear":
            currentInput = "";
            historyInput = "";
            break;

        case "backspace":
            currentInput = currentInput.slice(0, -1);
            break;

        case "=":
            if (currentInput !== "") {
                try {
                    // Combine history and current input, then evaluate
                    let expression = (historyInput + currentInput).replace(/×/g, "*").replace(/÷/g, "/");
                    let result = eval(expression);

                    historyInput = "";
                    currentInput = result.toString();
                } catch (err) {
                    currentInput = "Error";
                }
            }
            break;

        default:
            if (currentInput !== "") {
                historyInput += currentInput + " " + label + " ";
                currentInput = "";
            } else if (historyInput !== "") {
                // Change the last operator if user clicks a different one
                historyInput = historyInput.slice(0, -3) + " " + label + " ";
            }
            break;
    }
}