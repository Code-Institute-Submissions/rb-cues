## Contents
1. [User Stories](#user-stories)
2. [Automated](#automated)
3. [Validation](#validation)


## User Stories
As a site user I want to be able to ... so that I can ...
1. register for an account ... view my personal data on a profile
    - Open each page of the website from multiple devices and multiple browsers
    - On smaller screens there is a hamburger menu on the top of the page where the user can click on. This will result in a dropdown menu with all the links displayed.
    - Open with Chrome and Firefox Developer Tools. and click on "Responsive" to check all pages
2. register for an account ... view my personal data on a profile
    - Open the My Account dropdown menu in the navbar and select 'Register'
        * The 'Register' page is rendered
    - On the 'Register' page fill in all required fields and select 'Register'
        * If the e-mails don't match you'll get an error.
        * If the passwords don't match you'll get an error.
        * If the email allready exists you'll get an error.
        * If the username allready exists you'll get an error.
        * If the password is not strong enough you'll get an error.
        * If there are no errors the 'confirm-email' page is rendered and a e-mail is sent with a verification link.
3. receive a confirmation after registration ... verify that the registration process is completed.
    - Open the e-mail and use the verification link.
        * The 'confirm-email' page is rendered.
    - Confirm email
        * The 'Login' page is rendered and you can log in.
4. see all products ... choose which item to buy.
    - From the 'Home' page click on the 'Shop Now' button.
    - From every page in the website go to sub menu and select 'All Products' in the 'All Products' dropdown menu.
        - The 'Products' page is rendered with a full overview of all available products.
5. see all products of a specific category ... compare products in one view.
    - From the 'Products' page click on a catageory of a product card.
    - From every page in the website go to sub menu and select an item in one of the dropdown menu's.
        - The 'Products' page is rendered with a full overview of all available products in the specific category.
        - If multiple categories are selected (ex. 'All Cues') a full overview of all available products in the specific categories will be shown, as well as the sected catogories.

As a logged in user I want to be able to ... so that I can ...
1. reset my password ... recover access to my account.
    - Open the My Account dropdown menu in the navbar and select 'Login'
        * The 'Login' page is rendered
    - Click on 'Forgot Password' 
        * The 'Password Reset' page is rendered.
    - Fill in your e-mail address and click on 'Reset My Password'
        * If the e-mail address is unknow you'll get an error message.
        * If the e-mail address is correct the 'Password Reset' page is re-rendered and a e-mail is sent.
    - Open the e-mail and use the reset link.
        * The 'Change Password' page is rendered.
    - Fill in your new password and click 'Change Password'
        * If the passwords don't match you'll get an error.
        * The 'Change Password' page is re-rendered.
        * You'll get a succes message in the top right corner that the password is successfully changed.
2. login/ logout of my registered account ... access my personal data on a profile.
    - Open the My Account dropdown menu in the navbar and select 'Login'
        * The 'Login' page is rendered
    - Fill in verified credentials and click on 'Login'
        * The 'Home/Index' page is rendered.
        * You'll get a succes message in the top right corner that the login is successfull.
3. have a profile ... store my user info and see my old orders.
    - Open the My Account dropdown menu in the navbar and select 'My Profile'
        * The 'Profile' page is rendered.
        * On the left you'll see a column with default delivery information.
        * On the right you'll see a column with your order history.
4. enter my billing information ... checkout easier.
    - Open the My Account dropdown menu in the navbar and select 'My Profile'
        * The 'Profile' page is rendered.
    - Fill in or change fields in the default delivery information and click on 'Update Information'
        * The 'Profile' page is re-rendered.
        * The fields are updated with the given information.
        * You'll get a succes message in the top right corner that the profile update is successfull.


As an admin/store owner I want to be able to ... so that I can ...
        
## Automated
Automated testing is an addition to the manual testing to get the most coverage of the website. The aim was not to get 100% coverage but to get the inner working tested. I used Django testing module, The Tests were written for 'Views', 'Forms', 'Urls' and 'Models' and can be found in each application specific folders. All tests can be run with the command: 'python manage.py test'

tests_models.py
tests_forms.py
tests_views.py
tests_urls.py

Due to time management issues I chose not to test the webhook functionality and do a coverage test because this is captured by user storie testing.

## Validation
To make sure there where nog syntax errors, I've used the following validators on my pages:
* [HTML validator](https://validator.w3.org/#validate_by_input)
* [CSS validator](https://jigsaw.w3.org/css-validator/)
* [PEP8](http://pep8online.com/checkresult)

And I used the Flake8 function in GitPod. I left migration and settings.py as is and also ignore warnings about model fields.