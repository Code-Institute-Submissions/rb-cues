## Contents
1. [User Stories](#user-stories)
2. [Automated](#automated)
3. [Validation](#validation)


## User Stories
As a site user I want to be able to ... so that I can ...
1. register for an account ... view my personal data on a profile
    - Open each page of the website from multiple devices and multiple browsers
    - Open with Chrome and Firefox Developer Tools. and click on "Responsive" to check all pages

2. register for an account ... view my personal data on a profile
    - Open the My Account dropdown menu in the navbar and select 'Register'
        * The 'Sign Up' page is rendered
    - On the 'Sign Up' page fill in all required fields and select 'Sign Up'
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
        * The 'Sign In' page is rendered and you can log in.
        
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