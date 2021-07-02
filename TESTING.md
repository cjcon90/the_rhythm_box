## Functionality

### Landing Page

- [x] Category links lead to the correct URLs without error
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
- [x] Product details are responsive with a layout switch at 1200px
- [x] Rating star input works as expected and confirms action with a star message
- [x] Review section shows 'no reviews yet' if none yet writted on product
- [x] 'Write a review' button disappears if user has written a review, and is replaced by 'Edit review' and 'Delete review' buttons under their own review
- [x] Edit review form works as expected, and rating field is pre-populated with user rating, if exists 
- [x] Deleting a review deletes both the review and associated rating  