// HAMBURGER MENU

const hamburger = document.querySelector('.nav__hamburger')
const menu = document.querySelector('.nav-menu')
const menuList = document.querySelectorAll('li.nav-menu__list--category, li.nav-menu__list--subcategory')

// Add animation to nav menu items in mobile view
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    menu.classList.toggle('hidden');
    for(let i = 0; i < menuList.length; i++) {
        menuList[i].classList.toggle('nav-list-appear')
    }
})