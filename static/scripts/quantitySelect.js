// FOR QUANTITY SELECT FUNCTIONING ON PRODUCT & CART PAGES

const addToCartForms = document.querySelectorAll(".add-to-cart-form");
const updateCartForms = document.querySelectorAll(".update-cart-form");

function quantitySelectForm(forms, type) {
  forms.forEach((form) => {
    // identify input field, increment, decrement & max value (based on current stock)
    const numberInput = form.querySelector(".input-number");
    const numberDecrement = form.querySelector(".input-number-decrement");
    const numberIncrement = form.querySelector(".input-number-increment");
    const stock = +numberInput.getAttribute("max");
    let min = 0;

    if (!stock) {
      numberInput.value = 0;
    } else {
      // if adding to cart (and there are products currently in stock), then set minimum value to 1
      if (type === "add") {
        min = stock > 0 ? 1 : 0;
      }

      // increment & decrement number functionality

      numberDecrement.addEventListener("click", () => {
        if (+numberInput.value > min) {
          numberInput.value--;
        }
      });
      numberIncrement.addEventListener("click", () => {
        if (+numberInput.value < stock) {
          numberInput.value++;
        }
      });
    }
  });
}

quantitySelectForm(addToCartForms, "add");
quantitySelectForm(updateCartForms, "update");
