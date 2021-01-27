[This website](https://rb-cues.herokuapp.com//) was created to let people buy pool gear.<br>
As a user you can shop for cues and accessoires.<br>
As admin you can add, update or delete items.<br>


## Contents
1. [UX](#UX)
     - [User Stories](#user-stories)
     - [Wireframes](#wireframes)
2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Apps-Api](#apps-api)
    - [Framework](#framework)
    - [Resources](#resources)
4. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
5. [Deployment](#deployment)
    - [GitPod](#gitpod)
6. [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

## UX

### User Stories

<details>
<summary>As a site user I want to be able to ... so that I can ...</summary>

1. navigatie easily between the pages ... browse through the website
2. register for an account ... view my personal data on a profile
3. receive a confirmation after registration ... verify that the registration process is completed.
4. see all products ... choose which item to buy.
5. see all products of a specific category ... compare products in one view.
6. sort the selected list of products ... easily find the cheapest product.
7. search a product by name ... find a specific product.
8. see a products detail ... see the price, description and a preview of the product.
9. see a products detail ... add this item to my shopping cart.
10. see the total of my shopping cart ... avoid overspending.
11. see all items in my shopping cart ... know I added the correct items.
12. remove items from my cart ... only add the correct items I want to purchase.
13. adjust the quantity of items in my cart ... make changes before paying.
14. print an order confirmation ... contact the store if I have questions about the order.
</details>
<details>
<summary>As a logged in user I want to be able to ... so that I can ...</summary>

1. login/ logout of my registered account ... access my personal data on a profile.
2. have a profile ... store my user info and see my old orders.
3. reset my password ... recover access to my account.
4. enter my billing information ... checkout easier.
</details>
<details>
<summary>As an admin/store owner I want to be able to ... so that I can ...</summary>

1. add new products to the website ... fill my webstore.
2. edit products in the website ... change prices, descriptions and images.
3. delete products from the website ... remove items which aren't sold anymore.
</details>

### WireFrames

<details>
<summary>Home Page</summary>
<br>

![Home Page](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Homepage.png?raw=true)

</details>

<details>
<summary>Shop / Productoverview</summary>
<br>

![Shop](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Shop.png?raw=true)

</details>

<details>
<summary>Product detail</summary>
<br>

![Product Page](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Product.png?raw=true)

</details>

<details>
<summary>Profile</summary>
<br>

![Profile Page](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Profile.png?raw=true)

</details>

<details>
<summary>Shopping cart</summary>
<br>

![Shopping Cart](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Shopping_cart.png?raw=true)

</details>

<details>
<summary>Order confirmation</summary>
<br>

![Order](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Order.png?raw=true)

</details>

</details>

<details>
<summary>Add/edit Products</summary>
<br>

![Add](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Add.png?raw=true)

![Edit](https://github.com/VolkovBos/rb-cues/blob/master/media/wireframes/Edit.png?raw=true)

</details>

 <div align="right">

[Back to Top &#8593;](#contents)
</div>

## Features
### Existing Features
#### Top Navbar
Changes Dymamicaly depending on the login status of the user. 
- If the user is not logged in it shows the basic menu with 'Register/Login' and shopping cart.
- If the user is logged in it shows the basic menu with 'My Profile/Logout' and shopping cart.
- If the user is logged in and a superuser it shows the basic menu with 'Admin Section/Add Product/ My Profile/Logout' and shopping cart.

The 4 submenu items are links to the shop. They are clickable and lead to:
All Products
- By Price; shows all products in the shop sorted by price low to high.
- By Category; shows all products in the shop sorted by category A to Z.
- All Products; shows all products in the shop.

Cues
- Billiards; shows all products in the shop filtered by category 'Billiards'.
- Pool; shows all products in the shop filtered by category 'Pool'.
- Snooker; shows all products in the shop filtered by category 'Snooker'.
- All Cues; shows all products in the shop filtered by category 'Billiards', 'Pool' or 'Snooker'.

Accessories
- Maintenance; shows all products in the shop filtered by category 'Maintenance'.
- Gloves; shows all products in the shop filtered by category 'Gloves'.
- Tips; shows all products in the shop filtered by category 'Tips'.
- All Accessories; shows all products in the shop filtered by category 'Maintenance', 'Gloves' or 'Tips'.

New/Deals
- New; shows all products in the shop filtered by 'New'.
- Deals; shows all products in the shop filtered by 'Deal'.
- All; shows all products in the shop filtered by 'New' or 'Deal'.

Search Bar 
The search bar will look for a matching word or words in either the name or description of the products.

Back to top button
Throughout the site in the right bottom of the page you have the option to go back to the top of the page.

#### General Shop
Sort By Selector: Here you can sort the products by:
- Price; (low-high) or (high-low).
- Name; (A-Z) or (Z-A).
- Category; (A-Z) or (Z-A).

Product cards
The Product cards are clickable and will take you to the details product page. If the product does not have an image a 'No Image' image will take its place. The admin is able to see edit or delete on the product cards from your shop as on the product details page.

Quantity selector
lets you add more items to your order.

Add to Cart Message
When you add an item to the cart, a message will appear letting you know it was successful, and give the user a quick way to checkout with a checkout button.

#### Shopping cart
Price
A breakdown of all the charges are on the right, so you know how much you will be charged.

Adjust Cart
The user can adjust or delete from the cart if they have made a mistake.

Secure Payment method
Using Stripe is a secure way to place your orders

Checkout
Once the order has been submitted and Stripe receives payment, you will see the order with an option to print this.

#### Profile (logged in users)
Profile Page
A full profile page with all default billing info and order history.

Order history
A order history log where you can find all of your orders.

### Features Left to Implement
- A contact page.
- Ability to maintain stock on all products.

 <div align="right">

[Back to Top &#8593;](#contents)
</div>

## Technologies Used
I have used the following technologys for this project:

### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5), Semantic markup language as the shell of the site
* [CSS3](https://en.wikipedia.org/wiki/CSS), Cascading Style Sheets as the design of the site
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [jQuery](https://jquery.com/), for DOM manipulation
* [Python](https://www.python.org), for the backend
    - [Django](https://www.djangoproject.com/), for my framework
    - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/), to render forms

### Apps-Api
* [Heroku](https://heroku.com), to deploy my app
* [Gitpod](https://gitpod.io), for development
* [Github](https://github.com), for version control
* [Balsamiq](https://balsamiq.com/wireframes/desktop/), for creating the wireframes
* PIP, to download tools
* [Stripe](https://stripe.com/) for online payment
* [Postgres SQL](https://www.postgresql.org/), for my database

### Framework
* [Bootstrap](https://getbootstrap.com/), for CSS and HTML framework
* [Font Awesome](https://fontawesome.com/), for icons
* [Google Fonts](https://fonts.google.com/), to choose and combine my fonts

### Resources
* [Unsplash](https://unsplash.com/), for images

 <div align="right">

[Back to Top &#8593;](#contents)
</div>

## Testing
Testing and Validation information and be found at [Testing.md](https://github.com/VolkovBos/rb-cues/blob/master/testing.md)


## Deployment
This project was created using Github.<br>
From there I used Gitpod.io to write my code.<br>
Then I used commits to git followed by pushes to my GitHub repository.<br>
Later on I've deployed this project to Heroku and used automated pushes to make sure my pushes to GitHub were also made to Heroku.<br>
For deployment on Heroku I've used the following steps:
* Using the terminal command pip freeze > requirements.txt I have created a requirements.txt file.
* Using the terminal command echo web: python app.py > Procfile I have created a procfile.
* I've used git add, git commit and git push to push the requirements and Procfile to GitHub.
* I've created a new app on the Heroku website by using the "new" button on my dashboard.
* I gave the app a name of rb-cues and set the region to Europe.
* From the Heroku dashboard I've clicked "Deploy" > "Deployment method" and selected GitHub.
* Confirm the linking of the heroku app to the correct GitHub repository.
* In the heroku dashboard I've clicked "Settings" > "Reveal Config Vars".
* I've added the config vars for my DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS.
* In the heroku dashboard I've clicked "Deploy".
* In the "Manual Deployment" section of this page I've made sure the master branch is selected and I've clicked "Deploy Branch".
* The site was now successfully deployed.


### Gitpod
To run this project in GitPod:
1) Use the Gitpod button on the GitHub repository
2) pip install -r requirements.txt
    - Install all python apps necessary for this site
3) python manage.py migrate
    - Create database based on the models
4) python manage.py loaddata categories
    - Load category fixture data (categories need to be loaded before products)
5) python manage.py loaddata products
     - Load products fixture data
6) python manage.py createsuperuser
    - Fill in a username, email and a password
7) python manage.py runserver
    - Run the site

 <div align="right">

[Back to Top &#8593;](#contents)
</div>

## Credits
### Content
I used code from [Project - Boutique Ado](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/?activate_block_id=block-v1%3ACodeInstitute%2BFSF_102%2BQ1_2020%2Btype%40sequential%2Bblock%40d3188bf68530497aa5fba55d07a9d7d7) from [Code Institue](https://github.com/Code-Institute-Org) for this project and I also used this as a guideline for the steps in the development proces.

### Acknowledgements
Thanks to [Tim (Justim)](https://github.com/justim) for some deeper explanation about Python views and decorators. Helped me with the login view decorator.

Thanks to [Robert Zunikoff](https://unsplash.com/@rzunikoff), for the main index background image

And a thanks to my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) who gave me honest, specific and good feedback.

[w3schools](https://www.w3schools.com/) and [StackOverflow](https://stackoverflow.com/) for research.

 <div align="right">

[Back to Top &#8593;](#contents)
</div>