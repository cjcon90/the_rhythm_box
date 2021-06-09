import { dropdownMenu } from "./modules/dropdown.js";

// MAIN SHOPPING PAGE SORT & FILTER

const productSortButton = document.getElementById("product-sort-button");
const productSortList = document.getElementById("product-sort-list");
const filtersMenuButton = document.querySelector(".filters__button");
const filtersMenu = document.querySelector(".filters__menu");

filtersMenuButton.addEventListener("click", () => {
  filtersMenu.classList.toggle("closed");
});

dropdownMenu(productSortButton, productSortList);
