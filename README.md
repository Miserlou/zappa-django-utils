# zappa-django-utils

Small utilities for making [Zappa](https://github.com/Miserlou/Zappa) deployments slightly easier for Django applications.

## Installation

Install via `pip`:
    
    $ pip install zappa-django-utils

Add to your installed apps:

    INSTALLED_APPS += ('zappa_django_utils',)

## Usage

### Creating a Postgres Database

Once you have your RDS set up, your VPC/Subnet/Security Groups set up, and your `DATABASES` setting set up, you can create the database with:

    $ zappa manage create_pg_db

Then you're ready to `python manage.py makemigrations` and `zappa update; zappa manage migrate`!

### Creating a default admin user 

You'll probably need a default user to manage your application with, so you can now:

    $ zappa manage create_admin_user

Now log in with the information that gets returned and immediately change the admin user's email and password.


## License

(c) 2017, Rich Jones, MIT License
