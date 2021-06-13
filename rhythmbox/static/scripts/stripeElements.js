// API and secret key
const stripePublicKey = document
  .getElementById("id_stripe_public_key")
  .textContent.slice(1, -1);
const stripeClientSecret = document
  .getElementById("id_client_secret")
  .textContent.slice(1, -1);
// credit card input
const cardElement = document.getElementById("card-element");
const errorDiv = document.querySelector(".card-errors");
const submitButton = document.querySelector('.form__submit')
const loadingOverlay = document.querySelector('.loading-overlay')

if (stripePublicKey && stripeClientSecret) {
  // create card element with basic styling
  const stripe = Stripe(stripePublicKey);
  const elements = stripe.elements();
  const card = elements.create("card", {
    classes: {
      base: "form__input regular",
    },
    style: {
      base: {
        fontSize: "20px",
      },
      invalid: {
        color: "#ad0000",
      },
    },
  });

  card.mount("#card-element");

  // Display any errors in card input
  card.addEventListener("change", (e) => {
    if (e.error) {
      displayError(e, errorDiv);
    } else {
      errorDiv.innerHTML = "";
    }
  });

  // Handle form submission
  const form = document.getElementById("payment-form");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    card.update({ disabled: true });
    submitButton.setAttribute('disabled', '')
    loadingOverlay.classList.remove('no-display')
    loadingOverlay.classList.add('grid-center', 'loading-overlay-appear')
    stripe
      .confirmCardPayment(stripeClientSecret, {
        payment_method: {
          card: card,
        },
      })
      .then((result) => {
        if (result.error) {
          displayError(result, errorDiv);
          card.update({ disabled: false });
          submitButton.removeAttribute('disabled')
          loadingOverlay.classList.remove('grid-center', 'loading-overlay-appear')
          loadingOverlay.classList.add('no-display')
        } else {
          if (result.paymentIntent.status === "succeeded") {
            form.submit();
          }
        }
      });
  });

  // function to display any errors in stripe process
  function displayError(error, div) {
    div.textContent = '' // initially reset div to prevent error messages stacking
    const errorSpan = document.createElement("span");
    errorSpan.classList.add("card-errors__error");
    const i = document.createElement("i");
    i.classList.add("fas", "fa-times", "card-errors__error--icon");
    errorSpan.appendChild(i);
    const textSpan = document.createElement("span");
    textSpan.textContent = error.error.message;
    div.appendChild(errorSpan);
    div.appendChild(textSpan);
  }
}
