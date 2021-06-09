// FOR QUANTITY SELECT FUNCTIONING ON PRODUCT & CART PAGES

const inputDiv = document.querySelectorAll('.number-select')

inputDiv.forEach(div => {
  const numberInput = div.querySelector(".input-number");
  const numberDecrement = div.querySelector(".input-number-decrement");
  const numberIncrement = div.querySelector(".input-number-increment");
  const stock = +numberInput.getAttribute("max");

  if (!stock) {
    numberInput.value = 0;
  } else {
    const min = stock > 0 ? 1 : 0;

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

})

