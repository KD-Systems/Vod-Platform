const menu = document.querySelector("#menu");
const dropDown = document.querySelector("#drop-down");
const sidebar = document.querySelector(".sidebar");
const drop_down = document.querySelector(".dropdown-content-background");

menu.addEventListener("click", function () {
    sidebar.classList.toggle("show-sidebar");
});
dropDown.addEventListener("click", function () {
    drop_down.classList.toggle("show-dropdown");
});
