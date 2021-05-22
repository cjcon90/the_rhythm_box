const hamburger = document.querySelector('.nav__hamburger')
const menu = document.querySelector('.nav-menu')
const menuList = menu.children

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    menu.classList.toggle('hidden');
    for(let i = 0; i < menuList.length; i++) {
        menuList[i].classList.toggle('nav-list-appear')
    }
})