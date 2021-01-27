[This website](https://rb-cues.herokuapp.com//) was created to let people buy pool gear.<br>
As a user you can shop for cues and accessoires.<br>
As admin you can add, update or delete items.<br>


## Contents
1. [UX](#UX)
     - [Project Goals](#project-goals)
     - [User Stories](#user-stories)
     - [Wireframes](#wireframes)
     - [Design](#design)
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

* For a user I want to be able to ... so that I can ...
    * navigatie easily between the pages ... browse throught the website.
    * register for an account ... view my personal data on a profile.
    * login/ logout of my registered account ... access my personal data on a profile.
    * receive a confirmation after registration ... verify that the registration process is completed.
    * have a profile ... store my user info and see my old orders.
    * reset my password ... recover access to my account.

    * see all products ... choose which item to buy.
    * see all products of a specific category ... compare products in one view.
    * sort the selected list of products ... easily find the cheapest product
    * search a product by name ... find a specific product

    * see a products detail ... see the price, description and a preview of the product.
    * see a products detail ... add this item to my shopping cart.
    * see the total of my shopping cart ... avoid overspending.
    
    * see all items in my shopping cart ... know I added the correct items.
    * remove items from my cart ... only add the correct items I want to purchase.
    * adjust the quantity of items in my cart ... make changes before paying.
    * enter my billing information ... checkout easier.
    * print an order confirmation ... contact the store if I have questions about the order.

* For an admin I want to be able to ... so that I can ...
    * add new products to the website ... fill my webstore.
    * edit products in the website ... change prices, descriptions and images.
    * delete products from the website ... remove items which aren't sold anymore.

### WireFrames

<details>
<summary>Home Page</summary>
<br>

![Home Page](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Homepage.png?raw=true)

</details>

<details>
<summary>Shop / Productoverview</summary>
<br>

![Shop](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Shop.png?raw=true)

</details>

<details>
<summary>Product detail</summary>
<br>

![Product Page](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Product.png?raw=true)

</details>

<details>
<summary>Profile</summary>
<br>

![Profile Page](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Profile.png?raw=true)

</details>

<details>
<summary>Shopping cart</summary>
<br>

![Shopping Cart](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Shopping_cart.png?raw=true)

</details>

<details>
<summary>Order confirmation</summary>
<br>

![Order](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Order.png?raw=true)

</details>

</details>

<details>
<summary>Add/edit Products</summary>
<br>

![Add](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Add.png?raw=true)

![Edit](https://github.com/VolkovBos/rb-cues/blob/master/wireframes/Edit.png?raw=true)

</details>


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


## Credits
### Content
I used code from [Project - Boutique Ado](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/?activate_block_id=block-v1%3ACodeInstitute%2BFSF_102%2BQ1_2020%2Btype%40sequential%2Bblock%40d3188bf68530497aa5fba55d07a9d7d7) from [Code Institue](https://github.com/Code-Institute-Org) for this project and I also used this as a guideline for the steps in the development proces.

### Acknowledgements
Thanks to [Tim (Justim)](https://github.com/justim) for some deeper explanation about Python views and decorators. Helped me with the login view decorator.

Thanks to [Robert Zunikoff](https://unsplash.com/@rzunikoff), for the main index background image

And a thanks to my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) who gave me honest, specific and good feedback.

[w3schools](https://www.w3schools.com/) and [StackOverflow](https://stackoverflow.com/) for research.