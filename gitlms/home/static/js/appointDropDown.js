let selectedUserId = null; // To store the selected user's ID

// Function to show the appoint modal
function showAppointModal(role, userId) {
  selectedUserId = userId; // Store the selected user's ID
  document.getElementById("appointModal").classList.remove("hidden");
  document.getElementById("roleSelect").value = "assign";

  // Fetch departments based on role selection
  fetchDepartments();
}

// Function to close the appoint modal
function closeAppointModal() {
  document.getElementById("appointModal").classList.add("hidden");
}

// Function to fetch departments from the server
function fetchDepartments() {
  fetch("/get_departments/")
    .then((response) => response.json())
    .then((data) => {
      const departmentSelect = document.getElementById("departmentSelect");
      departmentSelect.innerHTML =
        '<option value="">Select Department</option>'; // Reset options
      data.forEach((department) => {
        const option = document.createElement("option");
        option.value = department.id;
        option.textContent = department.name;
        departmentSelect.appendChild(option);
      });
    });
}

// Event listener for department selection
document
  .getElementById("departmentSelect")
  .addEventListener("change", function () {
    const departmentId = this.value;
    if (
      departmentId &&
      document.getElementById("roleSelect").value === "moderator"
    ) {
      // Fetch courses when department is selected
      fetchCourses(departmentId);
    } else {
      // Disable and reset the course dropdown when department is not selected
      document.getElementById("courseSelect").innerHTML =
        '<option value="">Select Course</option>';
      document.getElementById("courseSelect").disabled = true;
    }
  });

// Function to fetch courses for the selected department
function fetchCourses(departmentId) {
  fetch(`/get_courses_by_department/${departmentId}/`)
    .then((response) => response.json())
    .then((data) => {
      const courseSelect = document.getElementById("courseSelect");
      courseSelect.innerHTML = '<option value="">Select Course</option>'; // Reset options
      data.forEach((course) => {
        const option = document.createElement("option");
        option.value = course.id;
        option.textContent = `${course.course_code} - ${course.course_name}`;
        courseSelect.appendChild(option);
      });
      courseSelect.disabled = false; // Enable course selection
    })
    .catch((error) => console.error("Error fetching courses:", error));
}

// Function to handle role change
function roleChanged() {
  const role = document.getElementById("roleSelect").value;
  const departmentSelect = document.getElementById("departmentSelect");
  const courseSelect = document.getElementById("courseSelect");

  // Hide or show the department and course selects based on role
  if (role === "user") {
    departmentSelect.classList.add("hidden");
    courseSelect.classList.add("hidden");
    departmentSelect.disabled = true;
    courseSelect.disabled = true;
  } else if (role === "admin") {
    departmentSelect.classList.remove("hidden");
    courseSelect.classList.add("hidden");
    departmentSelect.disabled = false;
    courseSelect.disabled = true;
  } else if (role === "moderator") {
    departmentSelect.classList.remove("hidden");
    courseSelect.classList.remove("hidden");
    departmentSelect.disabled = false;
    courseSelect.disabled = true;
  }
}

// Function to save the assignment
function saveAssignment() {
  const role = document.getElementById("roleSelect").value;
  const departmentId = document.getElementById("departmentSelect").value;
  const courseId = document.getElementById("courseSelect").value;

  // Logic to save the role assignment (send data to the server via AJAX)
  const data = {
    user_id: selectedUserId,
    appoint_role: role, // Send the role being assigned
    department_id: departmentId,
    course_id: courseId,
  };

  // Send only department_id or course_id based on the selected role
  if (role === "admin") {
    // Only send department_id for Admin
    delete data.course_id;
  } else if (role === "moderator") {
    // Only send course_id for Moderator
    delete data.department_id;
  }

  // Send data to the server for processing
  fetch("/appoint_user/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      window.location.href = "/appoint";

      closeAppointModal();
    })
    .catch((error) => console.error("Error assigning role:", error));
}
