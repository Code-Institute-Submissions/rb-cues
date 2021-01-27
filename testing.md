## Contents
1. [User Stories](#user-stories)
2. [Automated](#automated)
3. [Validation](#validation)


## User Stories

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