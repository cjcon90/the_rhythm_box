function dropdownMenu(button, menu) {
    button.addEventListener('click', () => {
        menu.classList.toggle('show')
    })
}

export {dropdownMenu}