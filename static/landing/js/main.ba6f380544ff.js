
// show/hide nav menu
const menu = document.querySelector(".nav-links");
const menuOpenBtn = document.querySelector("#open-menu-btn");
const menuCloseBtn = document.querySelector("#close-menu-btn");

menuOpenBtn.addEventListener("click", () => {
    menu.style.display = "flex";
    menuCloseBtn.style.display = "inline-block";
    menuOpenBtn.style.display = "none";
});

menuCloseBtn.addEventListener("click", () => {
    menu.style.display = "none";
    menuCloseBtn.style.display = "none";
    menuOpenBtn.style.display = "inline-block";
});