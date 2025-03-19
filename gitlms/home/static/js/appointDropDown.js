function toggleDropdown(button) {
  let dropdown = button.nextElementSibling; // Select the dropdown menu inside the same div
  let allDropdowns = document.querySelectorAll(".dropdown-menu");

  // Close other open dropdowns
  allDropdowns.forEach((menu) => {
    if (menu !== dropdown) {
      menu.classList.add("hidden");
    }
  });

  // Toggle visibility of the selected dropdown
  dropdown.classList.toggle("hidden");
}

// Close dropdown when clicking outside
document.addEventListener("click", function (event) {
  let dropdowns = document.querySelectorAll(".dropdown-menu");
  let buttons = document.querySelectorAll("button");

  if (![...dropdowns, ...buttons].some((el) => el.contains(event.target))) {
    dropdowns.forEach((dropdown) => dropdown.classList.add("hidden"));
  }
});
