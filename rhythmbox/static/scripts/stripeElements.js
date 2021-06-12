const stripePublicKey = document.getElementById(
  "id_stripe_public_key"
).textContent;
const stripeClientSecret =
  document.getElementById("id_client_secret").textContent;
const cardElement = document.getElementById("card-element");
const errorDiv = document.querySelector(".card-errors");

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const card = elements.create("card", {
  classes: {
    base: "form__input regular",
  },
  style: {
    base: {
      fontSize: "1.5rem",
    },
    invalid: {
      color: "#ad0000",
    },
  },
});

console.log(card);

card.mount("#card-element");

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
  stripe
    .confirmCardPayment(stripeClientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: "Mr Test Name",
        },
      },
    })
    .then((result) => {
      if (result.error) {
        displayError(result, errorDiv);
        card.update({ disabled: false });
      } else {
        if (result.paymentIntent.status === "succeeded") {
          form.submit();
        }
      }
    });
});

// display any errors in stripe process
function displayError(error, div) {
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
