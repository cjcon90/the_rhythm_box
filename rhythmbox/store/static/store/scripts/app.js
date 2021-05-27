const hamburger = document.querySelector('.nav__hamburger')
const menu = document.querySelector('.nav-menu')
const menuList = document.querySelectorAll('li.nav-menu__list--category, li.nav-menu__list--subcategory')
const productSortButton = document.getElementById('product-sort-button')
const productSortList = document.getElementById('product-sort-list')
const filtersMenuButton = document.querySelector('.filters__button')
const filtersMenu = document.querySelector('.filters__menu')

// Add animation to nav menu items in mobile view
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    menu.classList.toggle('hidden');
    for(let i = 0; i < menuList.length; i++) {
        menuList[i].classList.toggle('nav-list-appear')
    }
})

filtersMenuButton.addEventListener('click', () => {
    filtersMenu.classList.toggle('closed')
})

// function for dropdown menus
function dropdown(button, menu) {
    button.addEventListener('click', () => {
        menu.classList.toggle('show')
    })
}

dropdown(productSortButton, productSortList)