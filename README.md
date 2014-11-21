Advanced redirect management for Django applications. Advanced Redirects tracks all urls routed through your Django app that generate a 404 response and allows you to specify permanent or temporary redirects for them through the admin. It also tracks the referring url based on the HTTP_REFERER property in the request, along with the number of hits and the most recent hit a particular url has had from a specific referrer. You can also manually create your own redirects.

# Dependencies
    Django >= 1.7

# Installation
pypi package coming soon.  In the mean time, install from the latest tagged version

    $ pip install -e git://github.com/eressler/django-advanced-redirects.git@0.9#egg=django-advanced-redirects

# Quick Start
1. Add 'advanced_redirects' to your installed apps

        INSTALLED_APPS = (
            ...
            'advanced_redirects',
        )

2. Add the redirects middleware to the top of your middleware classes. You want the redirects middleware to be at the top so that it runs first in the request phase.

        MIDDLEWARE_CLASSES = (
            'advanced_redirects.middleware.AdvancedRedirectMiddleware',
            ...
        )

3. Run migrations to setup the database models

        $ python manage.py migrate

# Usage
In the admin, under the 'Advanced_Redirects' heading you can click on the 'Redirects' link to see the active list of redirects. Any url that generates a 404 response will automatically be added, but you can also manually add redirects. From the change list page you can enter redirect information directly and select the type of response code to use, which can be important for SEO purposes.

![Redirects Change List Page](https://raw.githubusercontent.com/eressler/django-advanced-redirects/master/docs/images/change_list.png)

If you click on any redirect url to go to its change form, you will be able to view more detailed information about the redirect url, specifically having to do with the referer of that url. This allows you to identify where dead links are coming from.

![Redirect Change Form with Referers](https://raw.githubusercontent.com/eressler/django-advanced-redirects/master/docs/images/change_form.png)

And lastly, there are two admin actions available from the drop down on the change list page which allow you to either delete all referers for selected items, or reset their hit counts to zero, which can be useful for testing.

![Admin Actions](https://raw.githubusercontent.com/eressler/django-advanced-redirects/master/docs/images/admin_actions.png)

# Settings
### DEFAULT_404_REDIRECT
_Default Value: None_

If the Advanced Redirect Middleware encounters a url that 404's without a specified redirect, it does nothing and allows the remaining middleware to handle it, which will mostly show your site's default 404 page.  However, if you would prefer to make all 404 errors redirect to a specific default url, you can specify that using the DEFAULT_404_REDIRECT setting.
    DEFAULT_404_REDIRECT = '/search/'

# TO DO:
* Finish unit tests
* Deploy to Pypi
