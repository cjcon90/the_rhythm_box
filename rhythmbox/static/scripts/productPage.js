// import { dropdownMenu } from './modules/dropdown.js'

const numberInput = document.querySelector('.input-number');
const numberDecrement = document.querySelector('.input-number-decrement');
const numberIncrement = document.querySelector('.input-number-increment');
const stock = +numberInput.getAttribute('max');

const reviewsFilterButton = document.getElementById('reviews-filter-button')
const reviewsFilterList = document.getElementById('reviews-filter-list')
const reviewsSortButton = document.getElementById('reviews-sort-button')
const reviewsSortList = document.getElementById('reviews-sort-list')

// QUANTITY SELECT ON INDIVIDUAL PRODUCT PAGE

if(!stock) {
    numberInput.value = 0;
} else {
    const min = stock > 0 ? 1 : 0;
    function quantitySelect(num, inc, dec) {
        dec.addEventListener('click', () => {
            if(+num.value > min) {num.value--}
        })
        inc.addEventListener('click', () => {
            if(+num.value < stock) {num.value++}
        })
    }
    quantitySelect(numberInput, numberIncrement, numberDecrement)
}

// REVIEW BUTTON DROPDOWNS

// dropdownMenu(reviewsFilterButton, reviewsFilterList)
// dropdownMenu(reviewsSortButton, reviewsSortList)
// TODO: delete if not using

