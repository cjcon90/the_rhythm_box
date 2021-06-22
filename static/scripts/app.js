// HAMBURGER MENU

const hamburger = document.querySelector(".nav__hamburger");
const menu = document.querySelector(".nav-menu");
const menuList = document.querySelectorAll(
  "li.nav-menu__list--category"
);

// Toggle hamburger menu and add animation to menu items
hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("open");
  menu.classList.toggle("nav-hidden");
  for (let i = 0; i < menuList.length; i++) {
    menuList[i].classList.toggle("nav-list-appear");
  }
});

// Hover dropdown functionality for desktop navbar
for(let item of menuList) {
  item.forEach(e => {
    e.addEventListener('mouseover', () => {
      makeVisible(e)
      e.addEventListener('mouseover', () => {
        makeVisible(e)
      })
    })
  })
}

function makeVisible(element) {
  element.setAttribute("style", "display: inline-block;");
}