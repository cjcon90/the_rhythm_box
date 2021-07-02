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
const submitButton = document.querySelector(".form__submit");
const loadingOverlay = document.querySelector(".loading-overlay");
const paymentForm = document.querySelector("#payment-form");

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
        fontSize: "18px",
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
    const fd = new FormData(paymentForm);
    e.preventDefault();
    card.update({ disabled: true });
    submitButton.setAttribute("disabled", "");
    loadingOverlay.classList.remove("no-display");
    loadingOverlay.classList.add("grid-center", "loading-overlay-appear");

    const csrftoken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
    const url = "/checkout/cache_checkout_data/";
    const postData = {
      csrfmiddlewaretoken: csrftoken,
      client_secret: stripeClientSecret,
    };

    const httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function () {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        stripe
          .confirmCardPayment(stripeClientSecret, {
            payment_method: {
              card,
              billing_details: {
                name: `${getTrim(fd, "first_name")} ${getTrim(
                  fd,
                  "last_name"
                )}`,
                phone: getTrim(fd, "phone_number"),
                address: {
                  line1: getTrim(fd, "street_address_1"),
                  line2: getTrim(fd, "street_address_2"),
                  city: getTrim(fd, "town_or_city"),
                  country: getTrim(fd, "country"),
                  state: getTrim(fd, "county"),
                },
              },
            },
            shipping: {
              name: `${getTrim(fd, "first_name")} ${getTrim(fd, "last_name")}`,
              phone: getTrim(fd, "phone_number"),
              address: {
                line1: getTrim(fd, "street_address_1"),
                line2: getTrim(fd, "street_address_2"),
                city: getTrim(fd, "town_or_city"),
                country: getTrim(fd, "country"),
                postal_code: getTrim(fd, "postcode"),
                state: getTrim(fd, "county"),
              },
            },
          })
          .then((result) => {
            if (result.error) {
              displayError(result, errorDiv);
              card.update({ disabled: false });
              submitButton.removeAttribute("disabled");
              loadingOverlay.classList.remove(
                "grid-center",
                "loading-overlay-appear"
              );
              loadingOverlay.classList.add("no-display");
            } else if (result.paymentIntent.status === "succeeded") {
              form.submit();
            }
          });
      }
    };
    httpRequest.open("POST", url);
    httpRequest.setRequestHeader("Content-Type", "application/json");
    httpRequest.setRequestHeader("X-CSRFToken", csrftoken);
    httpRequest.send(JSON.stringify(postData));
  });
}

function displayError(error, div) {
  // function to display any errors in stripe process
  div.textContent = ""; // initially reset div to prevent error messages stacking
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

function getTrim(form, formField) {
  // Return trimmed user input from formData
  return form.get(formField).trim();
}
