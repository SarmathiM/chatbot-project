function sendMessage() {
  let input = document.getElementById("user-input");
  let message = input.value;

  if (message.trim() === "") return;

  let chatBox = document.getElementById("chat-box");

  chatBox.innerHTML += `<div class="user"><span>${message}</span></div>`;

  fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: message }),
  })
    .then((res) => res.json())
    .then((data) => {
      chatBox.innerHTML += `<div class="bot"><span>${data.response}</span></div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    });

  input.value = "";
}

function handleKey(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}

function clearChat() {
  document.getElementById("chat-box").innerHTML = "";
}

function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}