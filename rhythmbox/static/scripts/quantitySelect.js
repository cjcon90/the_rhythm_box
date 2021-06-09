// FOR QUANTITY SELECT FUNCTIONING ON PRODUCT & CART PAGES

const addToCartForms = document.querySelectorAll(".add-to-cart-form");
const updateCartForms = document.querySelectorAll(".update-cart-form");

function quantitySelectForm(form, type) {
  form.forEach((div) => {
    const numberInput = div.querySelector(".input-number");
    const numberDecrement = div.querySelector(".input-number-decrement");
    const numberIncrement = div.querySelector(".input-number-increment");
    const stock = +numberInput.getAttribute("max");
    let min = 0;

    if (!stock) {
      numberInput.value = 0;
    } else {
      if (type === "add") {
        min = stock > 0 ? 1 : 0;
      }

      function quantitySelect(num, inc, dec) {
        dec.addEventListener("click", () => {
          if (+num.value > min) {
            num.value--;
          }
        });
        inc.addEventListener("click", () => {
          if (+num.value < stock) {
            num.value++;
          }
        });
      }

      quantitySelect(numberInput, numberIncrement, numberDecrement);
    }
  });
}

quantitySelectForm(addToCartForms, "add");
quantitySelectForm(updateCartForms, "update");
