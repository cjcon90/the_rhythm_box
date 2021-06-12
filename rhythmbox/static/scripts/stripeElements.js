const stripe_public_key = document.getElementById('id_stripe_public_key').textContent;
const stripe_client_secret = document.getElementById('id_client_secret').textContent;
const cardElement = document.getElementById('card-element')
console.log(cardElement)

console.log(stripe_public_key, stripe_client_secret)

const stripe = Stripe(stripe_public_key);
const elements = stripe.elements();
const card = elements.create('card', {
    classes: {
        base: 'form__input regular',
    },
    style: {
        base: {
            fontSize: '1.5rem',
        }
    }
  });

console.log(card)

card.mount('#card-element');
