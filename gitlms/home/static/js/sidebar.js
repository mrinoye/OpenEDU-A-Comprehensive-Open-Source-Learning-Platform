function toggleSidebar() {
  let sidebar = document.getElementById("sidebar");
  let content = document.getElementById("content");

  // Toggle sidebar open/close
  sidebar.classList.toggle("open");

  // Toggle main content margin-left to shift
  content.classList.toggle("shifted");
}
