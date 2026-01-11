 


// const form = document.querySelector("form");
// const button = document.querySelector(".generate-btn");
// const spinner = document.querySelector(".spinner");
// const themeBtn = document.getElementById("themeToggle");

// if (form) {
//     form.addEventListener("submit", () => {
//         button.innerText = "⏳ Generating…";
//         button.disabled = true;
//         spinner.style.display = "block";
//     });
// }

// // Dark / Light mode
// if (localStorage.theme === "light") {
//     document.body.classList.add("light");
//     themeBtn.textContent = "☀️";
// }

// themeBtn.addEventListener("click", () => {
//     document.body.classList.toggle("light");
//     const light = document.body.classList.contains("light");
//     localStorage.theme = light ? "light" : "dark";
//     themeBtn.textContent = light ? "☀️" : "🌙";
// });

// // Section toggle
// function toggleSection(btn) {
//     const body = btn.nextElementSibling;
//     body.style.display = body.style.display === "block" ? "none" : "block";
// }




const form = document.querySelector("form");
const button = document.querySelector(".generate-btn");
const spinner = document.querySelector(".spinner");
const themeBtn = document.getElementById("themeToggle");

if (form) {
    form.addEventListener("submit", () => {
        button.innerText = "⏳ Generating…";
        button.disabled = true;
        spinner.style.display = "block";
    });
}

// Dark / Light mode
if (localStorage.theme === "light") {
    document.body.classList.add("light");
    themeBtn.textContent = "☀️";
}

themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("light");
    const light = document.body.classList.contains("light");
    localStorage.theme = light ? "light" : "dark";
    themeBtn.textContent = light ? "☀️" : "🌙";
});

// Section toggle
function toggleSection(btn) {
    const body = btn.nextElementSibling;
    body.style.display = body.style.display === "block" ? "none" : "block";
}
let steps = [
    "📄 Reading PDF…",
    "🧹 Cleaning text…",
    "🧠 Summarizing content…",
    "🧾 Formatting review…"
];

let stepIndex = 0;

if (form) {
    form.addEventListener("submit", () => {
        spinner.style.display = "block";

        setInterval(() => {
            if (stepIndex < steps.length) {
                spinner.innerText = steps[stepIndex];
                stepIndex++;
            }
        }, 2000);
    });
} 
function toggleChat() {
    const body = document.getElementById("chatBody");
    body.style.display = body.style.display === "block" ? "none" : "block";
}

function sendMessage() {
    const input = document.getElementById("chatInput");
    const message = input.value.trim();
    if (!message) return;

    addMessage("You", message);

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message})
    })
    .then(res => res.json())
    .then(data => addMessage("AI", data.reply));

    input.value = "";
}

function addMessage(sender, text) {
    const box = document.getElementById("chatBox");
    const msg = document.createElement("div");
    msg.className = sender === "You" ? "msg user" : "msg ai";
    msg.innerHTML = `<strong>${sender}:</strong><br>${text}`;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}

function clearChat() {
    document.getElementById("chatBox").innerHTML = "";
}
