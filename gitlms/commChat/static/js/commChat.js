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
