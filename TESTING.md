## Functionality

### Accounts & User Authentication
- [x] Registration & Login forms validation works as expected with user feedback on error
- [x] Previously existing emails will not be allowed to register again
- [x] Valid registration forms create a User model within the database
- [x] NewsletterSub accounts are successfully deleted once users have registered a full account 
- [x] Login and logout links work as expected
- [x] Views hidden behind a `@login_required` successfully direct user to the login page with a `?next` link  to redirect users after user authentication
- [x] If user inputs invalid information in login form, or navigates to the register page to set up an account, `?next` link is retained between views to redirect user
- [x] Delete account erases users from the database and any associated ratings, reviews or addresses
- [x] Orders are maintained within the system on Account deletion, with user set to NULL:

Order of deleted user in database           |
:-------------------------:|
![](docs/screenshots/test_delete.png)  |


### Landing Page

- [x] Category links on landing page lead to the correct URLs without error
- [x] When changing viewport, the hero image and category background images loaded change size appropriately
- [x] Hover, focus and active styles work on all links 
- [x] The main site heading and subheading stays within the dark section of the hero image on all common viewports, maximising visual impact and contrast 

### Navigation Bar

- [x] Navigation links lead to the correct URLs without error
- [x] Navbar links change appropriately depending on whether user is logged in or not
- [x] Hover, focus and active styles work on all links 
- [x] Subcategories appear on hover on all desktop viewports
- [x] The Cart updates accurately reflecting how many items it contains
- [x] The navbar changes from horizontal to hamburger for any viewports under 1200px
- [x] The nav menu takes up the page on mobile devices, yet the hamburger menu, logo and cart remain visible 

### Footer

- [x] Footer links lead to the correct URLs without error
- [x] Hover, focus and active styles work on all links 
- [x] As new subcategories are added, footer navigation links get updated automatically
- [x] The newsletter email input switches from empty to pre-populated and readonly once user is authenticated
- [x] Store email opens up default email app on desktop and phone
- [x] All external links open up in a new tab
- [x] Newsletter sign up successfully adds a newsletter subscription to:
	1. Anonymous users
	2. Registered users who are not currently signed up to the newsletter

### Shop

#### Sort, Search & Filter
- [x] Mobile filter menu is hidden off screen, and toggle button to show/hide filter menu works as expected
- [x] Mobile filter menu always appears above the product cards when toggled
- [x] Desktop Filter is visible on left side of the screen for viewports >= 700px
- [x] All viewports fit the filter menu and product cards successfully on the shop page without overflow issues
- [x] The search bar validation works and will request text input if empty
- [x] Search menu works and provides accurate results searching within brands, categories, subcategories, types, or product name
- [x] Dropdown filter works for each option, and does not reset existing filters applied on products shown
- [x] Dropdown links have hover styled on desktop to clearly show user what item is being selected 

#### Product Cards

- [x] Image thumbnails display for all products
- [x] Product brand logo displays and fits just below main image
- [x] Product title is displayed accurately
- [x] Clicking anywhere within the above three items will link to the product featured in the particular card
- [x] Star ratings display accurately, including 1/2, 1/3, 1/4 stars depending on the average rating
- [x] Hover, focus and active styles work on all links 
- [x] Add to cart button successfully adds 1 unit of the selected product to the cart
- [x] If the item is out of stock then the Add to cart button is disabled  

### Product Page

- [x] As in the product cards, all information is accurate to the product in the database with no missing data
- [x] Quantity select number input will be set to 0 if item is out of stock
- [x] Otherwise, quantity select has a minimum of 1 and a maximum of the total items in stock  
- [x] Product details are responsive with a layout switch at 1200px
- [x] Rating star input works as expected and confirms action with a star message
- [x] Review section shows 'no reviews yet' if none yet writted on product
- [x] 'Write a review' button disappears if user has written a review, and is replaced by 'Edit review' and 'Delete review' buttons under their own review
- [x] Edit review form works as expected, and rating field is pre-populated with user rating, if exists 
- [x] Deleting a review deletes both the review and associated rating  

### Contact Us Page

- [x] Contact form validation works as expected
- [x] Form is pre-populated with user name and email if user is logged in
- [x] Email sends from RhythmBox email to my own account with correct email subject, message content and return email:

Example Contact Us Email           |
:-------------------------:|
![](docs/screenshots/contact_us_email.png)  |


### Cart

- [x] quantity selectors on cart have a maximum value of item stock and a minmum value of 0 - which removes item from cart, as does 'Remove Item' button
- [x] If a user has previously added an item to the cart and returns later to buy it, but the quantity selected no longer exists in the store, this will display an error message and will also disable the button to proceed to checkout, to prevent errors on purchase

| Free Delivery & In Stock                    | No Free Delivery & Out of stock             |
| ------------------------------------------- | ------------------------------------------- |
| ![](docs/screenshots/cart_summary_pass.png) | ![](docs/screenshots/cart_summary_fail.png) |

### Checkout

- [x] If a user has no items in their cart and navigates to `/checkout/`, user is redirected back to `/cart/` and inform user that their cart is empty
- [x] On proceeding to the checkout screen, a Stripe payment intent is created:

Payment intent creation          |
:-------------------------:|
![](docs/screenshots/stripe_payment_intent.png)  |

- [x] Make default addrss checkbox successfully changes default address in user account
- [x] On valid checkout form input, user is successfully charged and payment succeeds:

Stripe payment succeeded         |
:-------------------------:|---------------------------
![](docs/screenshots/stripe_payment_success.png)  |

- [x] Successful checkout directs user to an order summary screen
- [x] Successful checkout creates an order in the database associated with correct user, which appears in the user's order history
- [x] Successful checkout also sends an HTML email confirmation to user:

Order Confirmation Email           |
:-------------------------:|
![](docs/screenshots/order_email.png)  |



## Testing User Stories

### New Visitors

+ to see the content and products on offer without having to register
+ to be able to add items to my cart and save them for later
	- [x] Users can see all products, reviews and ratings and add items to cart without having yet registered. Cart items will be saved in browser (once user is not in incognito mode, or clears browser sessions) for later purchase without sign up
+ to be able to easily register for the site
+ any items in my cart to remain there after I have registered for the site
	- [x] There is a focus on quick and easy registration for this site, as users are logged in as soon as they are registered.
	- [x] Validation errors that might prevent registration form from being submitted are also clear so that users can amend and submit registration form successfully
+ to quickly and easily filter and search for particular items
+ to be able to sort displayed items by price or user rating
	- [x] Filter is clear and legible on all screens and quickly navigates to category or section chosen by user.
	- [x] Design of mobile filter toggle animation received particularly good feedback from user testing, noted that it sparked joy as well as being functional
	- [x] Sorting of items is limited to the most wanted features so that it is clear and user can quickly find what they are looking for (i.e. nobody wants to search for 'lowest rated')

### Repeat Visitors

+ to easily login to my existing account
	- [x] Login form is clear and similar to registration provides clear validation if user has not submitted form correctly
+ for my previously added cart items to remain selected
	- [ ] This user story is fulfilled provided user has not been browsing in incognito, cleared browser cache or logged out of their account (this is as `session.flush()` is called as part of Django's built in logout functionality)
	- [x] for users that have closed their browser and returned to page within the same browser, this user story is fulfilled (fulfillment for *all* users is listed as a future improvement) 
+ to be able to checkout quickly using my previously saved details
	- [x] Users can not only save and edit their saved delivery details within their account page, but a cusom checkbox field is also prominent within the checkout form for users to save details for next purchase 
+ to be able to see my order history
	- [x] Order history lists all purchases made by a user in their account page
	- [x] An email receipt with full details, including delivery address for every order, is also sent to the user's email on every purchase 
+ to be able to review purchased items, and edit and delete my reviews
	- [x] User's can rate items or can rate + review items on every product page
	- [x] If user has not yet written a review then a large 'write a review' button is displayed prompting user interaction

### All users
+ to get feedback when I have completed an action on the site
	- [x] As well as form validation as listed above, many actions on the website include styled messages notifying user that their action has been successful or not. These include logging in/out, account creation/deletin, rating, reviewing, adding to cart and purchasing

Success            |  Error |  Star
:-------------------------:|:-------------------------:|:-------------------------:
![success message](docs/screenshots/messages_success.png)  |  ![error message](docs/screenshots/messages_error.png) |  ![star message](docs/screenshots/messages_star.png)

+ for the cost and fees involved in an order to be transparent and not confusing in any way
	- [x] As noted in [cart](#cart), delivery fees are clearly displayed before user proceeds to checkout
	- [x] A breakdown of costs is also displayed at checkout, on checkout confirmation and in confirmation email 
+ to get a record/confirmation of a successful purchase
	- [x] Order history lists all purchases made by a user in their account page
	- [x] An email receipt with full details, including delivery address for every order, is also sent to the user's email on every purchase 
+ for purchases to be completed securely
	- [x] Purchases are completed using the Stripe API, a well known ecommerce payment solution with a good reputation
	- [x] A webhook is implemented within the checkout app, so that the order is successfully processed in case the checkout process gets interrupted; for example - if the user closes the browser window early, or there is an interruption to their internet connection.
+ be able to contact the website owners when necessary
	- [x] The contact us page is clearly shown within the main navigation menu on all viewports and is one of the pages / functionalities that is open to all users whether they are anonymous or authenticated

### Site Owner

+ To be able to add new stock or update existing stock easily
	- [x] All models are clearly defined within the admin page
	- [x] Model elements such as slug, date added or thumbnail are automated and are made readonly within the admin to prevent incorrect input
	- [x] Stock levels can be easily adjusted with a simply quantity select  
+ users to be able to easily recover their account if they have lost their login details
	- [x] Password change procedure is the same for all users, whether authenticated or anonymous and is operated through the email with clear instructions at each stage

Password Reset Email           |
:-------------------------:|
![](docs/screenshots/password_reset_email.png)  |

+ for the website to appear clean, professional and high quality
	- [x] Professional design was a priority right from initial wireframing, and existing popular ecommerce sites such as [thomann](https://thomann.de) and [John Lewis](https://www.johnlewis.com/) were used as inspiration in this regard
	- [x] During user  testing by peers and relatives, website was designed as `professional`, `clean` and `slick`.
+ for the website to work on all viewports, so customers can shop from any device
	- [x] website has been tested extensively on multiple viewports, and any responsiveness issues have been responded to and fixed
+ for the payment system to be secure and free of errors, such as orders going through without payment or payments being taken multiple times
	- [x] No issues have been raised during user testing, and as outlined above - the Stripe API and use of webhooks provides a secure and functional payment process

## Lighthouse

- I conducted Lighthouse audits on the 4 main views (and most content filled) on the site: Home, Shop, Product Page and Cart (with three items in the cart)
- Performance scores suffered somewhat on mobile
- Future improvements that could improve performance scores for all platforms would be to serve static files using gzip compression

### Desktop

Home            |  Shop |  Product Page |  Cart
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![](docs/lighthouse/home_desktop.png)  |  ![](docs/lighthouse/shop_desktop.png) |  ![](docs/lighthouse/product_page_desktop.png) |  ![](docs/lighthouse/cart_desktop.png)
97 - 100 - 100 - 100  | 93 - 100 - 100 - 100 | 90 - 100 - 100 - 100 | 91 - 100 - 100 - 100 
[REPORT](docs/lighthouse/home_desktop.pdf)  |  [REPORT](docs/lighthouse/shop_desktop.pdf) |  [REPORT](docs/lighthouse/product_page_desktop.pdf) |  [REPORT](docs/lighthouse/cart_desktop.pdf)


### Mobile

Home            |  Shop |  Product Page |  Cart
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![](docs/lighthouse/home_mobile.png)  |  ![](docs/lighthouse/shop_mobile.png) |  ![](docs/lighthouse/product_page_mobile.png) |  ![](docs/lighthouse/cart_mobile.png)
83 - 100 - 100 - 100  | 81 - 100 - 93 - 100 | 89 - 100 - 100 - 100 | 90 - 100 - 100 - 100
[REPORT](docs/lighthouse/home_mobile.pdf)  |  [REPORT](docs/lighthouse/shop_mobile.pdf) |  [REPORT](docs/lighthouse/product_page_mobile.pdf) |  [REPORT](docs/lighthouse/cart_mobile.pdf)

## Validators

### [HTML5](https://validator.w3.org/)
- :white_check_mark: Home - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/)
- :white_check_mark: Shop - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/shop/)
- :white_check_mark: Product Details - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/shop/acoustic-drums/percussion/sonor-tt5-templeblock-set)
- :white_check_mark: Register - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/register/)
- :white_check_mark: Login - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/login/)
- :white_check_mark: Cart - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/cart/)
- :white_check_mark: Delivery - [Pass](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fprickly-app.herokuapp.com%2Fcheckout%2Fdelivery%2F#l1124c74)
- :white_check_mark: Checkout - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/checkout/)
- :white_check_mark: Checkout Success - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/checkout_success/140F-324A-637B/)
- :white_check_mark: Account Details - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/account/details/)
- :white_check_mark: Order History - [Pass](https://therhythmbox.herokuapp.com/account/orders/)
- :white_check_mark: Password Reset - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/account/password-reset/)
- :white_check_mark: Contact Us - [Pass](https://validator.w3.org/nu/?doc=https://therhythmbox.herokuapp.com/contact/)



### [CSS3](https://jigsaw.w3.org/css-validator/)
- :white_check_mark: main.css - Pass

<p>
	<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>
 	

### [JSHint](https://jshint.com/)

For testing with JSHint, I installed JSHint globally using:

		npm install -g jshint

and then within a `.jshintrc` file within my scripts folder I set the following setting:

```js
{
  "esversion": 6
}
```

**Results:**

- :white_check_mark:app.js - Pass
- :white_check_mark:quantitySelect.js - Pass
- :white_check_mark:shop.js - Pass
- :white_check_mark:stripeElements.js - Pass
- :white_check_mark:modules/dropdown.js - Pass




### [PEP8](http://pep8online.com/)
- :white_check_mark:all - Pass
- I used [[Black](https://github.com/psf/black)] formatter installed within PIP and set within VSCode as my default formatter, with the following settings:

```js
{
    "python.formatting.blackArgs": [
        "--line-length",
        "79"
    ],
    "python.formatting.provider": "black",
}
```



- Additionally, I also added all python files written by me in the [PEP8](http://pep8online.com/) validator online to ensure all files fit the standard.



## Usability
- To test the ease of navigation, this website was shared with friends and family of different ages and different levels of computer/smart device knowledge. There were no issues identified regarding the simplicity of navigating the website
- The highest praise coming from my mother, who declared "*even I can use this*". Genuinely proud of that one.
- To further expand on user testing,  multiple 'dummy' accounts were created to test the registration, log-in, membership subscription, CRUD functionality with reviews and purchasing items.

## Compatibility

| Screen size\Browser |       Safari       |       Brave    |       Chrome       |      Firefox       |
| ------------------- | :----------------: | :--: | :----------------: | :----------------: |
| Mobile              | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |
| Desktop             | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |

- Website was tested personally on an Android Google Pixel 4a 5g using Brave, Chrome and Firefox browsers
- Website was also tested personally on an Ubuntu 20.04 laptop using Brave, Chrome and Firefox browsers
- Website was tested on Safari desktop and mobile by friends using iPhone 8 and Macbook 13" 
- Website was also tested by family on Chrome OS
- Tablet testing was done extensively using Chrome and Firefox Dev tools, although no physical hardware testing could be confirmed
- Website was not made with any consideration to Internet Explorer compatibility

## Bugs

### Multiple Images

I noticed that within my media folder, the amount of images was rapidly growing and seemed to be adding new images everytime I edited a product in the django admin.

To fix, I installed [jango-cleanup](https://pypi.org/project/django-cleanup/) which deleted any unused images in the media folder, and did so successfully. 

I was still left with the issue of new images being saved and the old ones being deleted, so I edited my `save()` method to only upload a new thumbnail image if a product was either new, or the previous image had been edited

```python
    def save(self, *args, **kwargs):
        """
        Modified save method to update thumbnail only if object is
        new, or the object image has been updated
        """
        if self.pk is None:
            self.thumbnail = self.make_thumbnail(self.image)
        else:
            original = Product.objects.get(id=self.pk)
            if original.image != self.image:
                self.thumbnail = self.make_thumbnail(self.image)
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
```



### IntegrityError on loaddata

When moving my site from local SQLite development to Heroku PostgreSQL, I followed these steps:

1. Backup current SQLite database by typing in the terminal:

		./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json

1. Migrate the models to Postgres database

		python manage.py makemigrations
		python manage.py migrate

1. Then use this command to load your data from the db.json file into postgres:

		./manage.py loaddata db.json

After much research, the bug was due to me changing the AUTH_USER_MODEL later in the project, and that the `django_admin_log` table still contains a foreign key relation to the old `auth_user` table.

The solution was found in [this post](https://code.djangoproject.com/ticket/23297)

