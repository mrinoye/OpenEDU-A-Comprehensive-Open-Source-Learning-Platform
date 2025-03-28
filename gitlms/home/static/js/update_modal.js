// Get all buttons with the class 'openUpdateModalBtn' (generic button for any entity)
const openUpdateModalBtns =
  document.getElementsByClassName("openUpdateModalBtn");

// Get the update modal, close button, and form
const update_modal = document.getElementById("update_modal");
const closeUpdateModalBtn = document.getElementById("closeUpdateModalBtn");
const updateForm = update_modal.querySelector("form"); // Get the form element

// Add event listener to each "Update" button
for (let button of openUpdateModalBtns) {
  button.addEventListener("click", (event) => {
    event.stopPropagation(); // Prevent event propagation to parent elements

    // Get the type of entity (department, course, or any other entity) and ID from data attributes
    const entityType = button.getAttribute("data-type"); // e.g., "department", "course", etc.
    const entityId = button.getAttribute("data-id"); // The ID of the entity

    // Find the corresponding input fields for the modal based on entity type
    const entityIdField = document.getElementById(`${entityType}_id_field`);
    const entityNameField = document.getElementById(`${entityType}_name_field`);
    const entityDescriptionField = document.getElementById(
      `${entityType}_description_field`
    );

    // Clear existing values and set new ones for the modal
    if (entityIdField) {
      entityIdField.value = entityId;
    }
    if (entityNameField) {
      entityNameField.value = ""; // Clear or set default value if necessary
    }
    if (entityDescriptionField) {
      entityDescriptionField.value = ""; // Clear or set default value if necessary
    }

    // Dynamically update the form action URL with the department ID
    if (updateForm) {
      // Ensure department.id is appended as the last part of the action URL
      const formAction =
        updateForm.action.split("/").slice(0, -1).join("/") + `/${entityId}`;
      updateForm.action = formAction;
    }

    // Show the modal
    update_modal.classList.remove("hidden");
  });
}

// Close modal when the close button is clicked
if (closeUpdateModalBtn) {
  closeUpdateModalBtn.addEventListener("click", () => {
    update_modal.classList.add("hidden");
  });
}

// Close modal when clicking outside the modal
window.addEventListener("click", (e) => {
  if (e.target === update_modal) {
    update_modal.classList.add("hidden");
  }
});
