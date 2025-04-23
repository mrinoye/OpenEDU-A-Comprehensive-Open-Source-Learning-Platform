function scrollChatToBottom() {
  const chat = document.getElementById("chat-messages");
  if (chat) {
    console.log(chat.scrollHeight);
    chat.scrollTop = chat.scrollHeight;
  }
}

// Scroll on page load
window.addEventListener("load", scrollChatToBottom);

// Optional: scroll after new message is sent
function sendMessage(event) {
  event.preventDefault();
  // your logic to send message
  setTimeout(scrollChatToBottom, 100); // wait for DOM update
}

// Toggle options menu for sender
function toggleOptions(id) {
  const menu = document.getElementById(id);
  menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// Prevent form submission and handle sending message with attachment
function sendMessage(event) {
  event.preventDefault();
  const messageInput = event.target.querySelector('input[type="text"]');
  const message = messageInput.value;

  console.log("Message:", message);

  // Reset the input fields
  messageInput.value = "";
}
