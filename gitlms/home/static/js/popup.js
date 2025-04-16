// JavaScript to trigger the sliding animation when the page loads
window.addEventListener("DOMContentLoaded", function () {
  const sidePopup = document.getElementById("side-popup");
  sidePopup.classList.remove("translate-x-full"); // Remove translate class to make it slide in
  sidePopup.classList.add("translate-x-0"); // Position it at the screen edge
});

// Close the side popup
const closeSidePopup = document.getElementById("closeSidePopup");
closeSidePopup.addEventListener("click", function () {
  const sidePopup = document.getElementById("side-popup");
  sidePopup.classList.remove("translate-x-0");
  sidePopup.classList.add("translate-x-full");
  // Add a small delay before fully hiding
  setTimeout(() => {
    sidePopup.classList.add("hidden");
  }, 1000);
});
