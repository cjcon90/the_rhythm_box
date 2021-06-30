# The RhythmBox - E-Commerce Web App for Professional Drums, Cymbals and Drumming Equipment

Code Institute - Final Milestone Project (4) - Full Stack Frameworks With Django

The RhythmBox is a multi-page e-commerce web application, selling professional drum and percussion equipment.

The application focuses on high quality products from the top and most recogniseable brands in each category: acoustic drums, electronic drums, cymbals and drum hardware & accessories.

**This project contains real products from existing brands, the images of which have all been sourced from [Thomann.de](https://www.thomann.de), a major European music equipment retailer, where all of the actual products can be found.**

This project is hosted on Heroku => [Live Site](https://therhythmbox.herokuapp.com/)

Purchases can be made with the Stripe test credit card:
* **credit card:** 4242 4242 4242 4242
* **expiration date:** Any future date
* **CVC:** Any 3-digit number
* **ZIP:** Any 5-digit number

![Preview Image](https://res.cloudinary.com/cjcon90/image/upload/v1624905692/codeinstitute/the_rhythm_box/preview_image.png)

## Table of Contents

## User Experience

### User Stories

* As a new visitor, I would like:
	+ to see the content and products on offer without having to register
	+ to be able to easily register for the site
	+ to be able to add items to my cart and save them for later
	+ any items in my cart to remain there I have registered for the site
	+ to quickly and easily filter and search for particular items
	+ to be able to sort displayed items by price or user rating
* As a repear visitor, I would like:
	+ to easily login to my existing account
	+ for my previously added cart items to remain selected
	+ to be able to checkout quickly using my previously saved details
	+ to be able to see my order history
	+ to be able to review purchased items, and edit and delete my eviews
* All users would like:
	+ to get feedback when I have completed an action on the site
	+ for the cost and fees involved in an order to be transparent and not confusing in any way
	+ to get a record/confirmation of a successful purchase
	+ for purchases to be completed securely
	+ be able to contact the website owners when necessary

### Wireframes

Desktop and mobile wireframes were designed in Figma, with tablet and mid-sized screens following design cues from both.

[Original Figma Wireframes](https://www.figma.com/file/hg0KWE38FLTnIb9HUORQij/RhythmBox?node-id=0%3A1)

[PDF Wireframes](docs/wireframes.pdf)

#### Changes from wireframes

While the designs of the final website followed the original Figma designs extremely closely, there are a few small changes.

1. Some minor features were left out for the purposes of achieving a minimal viable product, as the core functionality and user stories were met without them. These included:
	+ Sorting and filtering reviews on products and rating product reviews on 'helpfulness'
		- not deemed necessary at this stage as there will be very few reviews on the website
	+ Navigation breadcrumbs on the desktop version of the site
		- although links are structured in a way that this feature could be added in without massive changes 
	+ Saving and storing payment information
		- as currenly, people are only expected to use a test Stripe card
2. The filtering system was changed to single-select list rather than a multi-select, collapsible list as shown in the wireframes. This would have added layers of complexity unnecessary at this stage
3. A star rating system, separate from reviews, was introduced to the product page as people interacting with and testing the site are far more likely to leave a star rating than write a review.



## Information Architecture

As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment.

### Data Models

A full list of data models used on the site are found below.

Unless otherwise stated, the default validation settings of `blank=False, null=False` are assumed.

#### User Model

For this app I created a custom User Model following [this guide in the Django documentation](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#specifying-a-custom-user-model) and [this tutorial by CodingWithMitch](https://www.youtube.com/watch?v=eCeRC7E8Z7Y).

This made is easy to add custom user fields, and have login based on email as opposed to an unneccessary username being used within model

#### Accounts App

##### `Account` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Email | email | EmailField | max_length=60, unique=True |
| First Name | first_name | CharField | max_length=30 |
| Last Name | last_name | CharField | max_length=30 |
| Newsletter | newsletter | BooleanField | default=True |
| Date Joined | date_joined | DateTimeField | auto_now_add=True |
| Last Login   | last_login | DateTimeField | auto_now_add=True |
| Is Admin | is_admin | BooleanField | default=False |
| Is Active    | is_active        | BooleanField   | default=False              |
| Is Staff     | is_staff         | BooleanField   | default=False              |
| Is Superuser | is_superuser     | BooleanField   | default=False              |

A custom user manager is defined as per [the Django documentation](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model)

##### `Address` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| User | user | OneToOneField 'Account' | on_delete=models.CASCADE |
| Street Address 1 | street_address_1 | CharField | max_length=80 |
| Street Address 2 | street_address_2 | CharField            | max_length=80, null=True, blank=True |
| Town or City     | town_or_city | CharField | max_length=40 |
| County | county | CharField | max_length=40 |
| Postcode         | postcode         | CharField            | max_length=20                        |
| Country          | country          | CountryField         | default="IE"                         |
| Phone Number | phone_number | CharField | max_length=20 |

##### `NewsletterSub` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Email             | email             | EmailField     | max_length=60, unique=True |
| Subscription Date | subscription_date | DateTimeField  | auto_now_add=True          |

#### Products App

##### `Category` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Title    | title            | Charfield      | max_length=255                  |
| Slug     | slug             | Charfield      | max_length=255,<br />blank=True |
| Ordering | order            | IntegerField   | default=0                       |

##### `Subcategory` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Parent   | parent           | OneToOneField 'Category' | on_delete=models.CASCADE        |
| Title    | title            | Charfield                | max_length=255                  |
| Slug     | slug             | Charfield                | max_length=255,<br />blank=True |
| Ordering | order            | IntegerField             | default=0                       |

##### `Type` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Parent   | parent           | OneToOneField 'Subcategory' | on_delete=models.CASCADE        |
| Title    | title            | Charfield                   | max_length=255                  |
| Slug     | slug             | Charfield                   | max_length=255,<br />blank=True |
| Ordering | order            | IntegerField                | default=0                       |

##### `Brand` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Name     | name             | Charfield      | max_length=255                  |
| Slug     | slug             | Charfield      | max_length=255,<br />blank=True |
| Logo     | logo             | ImageField     | upload_to="brands/"             |

##### `Product` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Category    | category         | OneToOneField 'Category'    | on_delete=models.CASCADE                                  |
| Subcategory | subcategory      | OneToOneField 'Subcategory' | on_delete=models.CASCADE                                  |
| Type        | type             | OneToOneField 'Type'        | null=True,<br />blank=True,<br />on_delete=models.CASCADE |
| Title       | title            | Charfield                   | max_length=255                                            |
| Slug        | slug             | Charfield                   | max_length=255,<br />blank=True                           |
| Brand       | brand            | OneToOneField 'Brand'       | null=True,<br />blank=True,<br />on_delete=models.CASCADE |
| Description | description      | TextField                   | blank=True, null=True                                     |
| Price       | price            | DecimalField                | max_digits=7,<br />decimal_places=2                       |
| Stock       | stock            | IntegerField                | default=15                                                |
| Date Added  | date_added       | DateTimeField               | auto_now_add=True                                         |
| Image       | image            | ImageField                  | upload_to="/products/",<br />blank=True, null=True        |
| Thumbnail   | thumbnail        | ImageField                  | upload_to="/products/thumbnails/", blank=True, null=True  |


##### `Rating` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| User ID | user_id | OneToOneField 'Account' | on_delete=models.CASCADE |
| Product | product | OneToOneField 'Product' | on_delete=models.CASCADE |
| Rating | rating | IntegerField | choices=Stars.choices |
| Date Added | date_added | DateTimeField | auto_now_add=True |


##### `Review` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Rating | rating | OneToOneField 'Rating' | on_delete=models.CASCADE |
| Headline | headline | CharField | max_length=50 |
| Content | content | TextField | max_length=500 |
| Date Added | date_added | DateTimeField | auto_now_add=True |


`Order` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Order Number | order_number | CharField | max_length=32,<br />editable=False,<br />unique=True |
| User | user | ForeignKey 'Account' | on_delete=models.SET_NULL,<br />null=True, <br />blank=True,<br />related_name='orders' |
| First Name | first_name | CharField | max_length=50 |
| Last Name | last_name | CharField | max_length=50 |
| Street Address 1 | street_address_1 | CharField | max_length=80 |
| Street Address 2 | street_address_2 | CharField | max_length=80,<br />null=True, blank=True |
| Town or City | town_or_city | CharField | max_length=40 |
| County | county | CharField | max_length=40 |
| Postcode | postcode | CharField | max_length=20 |
| Country | country | CountryField | default="IE" |
| Phone Number | phone_number | CharField | max_length=20 |
| Date | date | DateTimeField | auto_now_add=True |
| Delivery Cost | delivery_cost | DecimalField | max_digits=8,<br />decimal_places=2, default=0 |
| Order Total | order_total | DecimalField | max_digits=12, <br />ecimal_places=2, default=0 |
| Grand Total | grand_total | DecimalField | max_digits=12,<br />decimal_places=2, default=0 |
| Original Cart | original_cart | TextField |  |
| Stripe PID | stripe_pid | CharField | max_length=254 |

`OrderLineItem` model

| **Name**        | **Database Key** | **Field Type**       | **Type Validation**                                       |
| --------------- | ---------------- | -------------------- | --------------------------------------------------------- |
| Order           | order            | ForeignKey 'Order'   | on_delete=models.CASCADE,<br />related_name='lineitems'   |
| Product         | product          | ForeignKey 'Product' | on_delete=models.CASCADE                                  |
| Quantity        | quantity         | IntegerField         | default=0                                                 |
| Line Item Total | lineitem_total   | DecimalField         | max_digits=12,<br />decimal_places=2,<br />editable=False |