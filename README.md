# zappa-django-utils 0.4.1: final release!

[![PyPI](https://img.shields.io/pypi/v/zappa-django-utils.svg)](https://pypi.python.org/pypi/zappa-django-utils)
[![Slack](https://img.shields.io/badge/chat-slack-ff69b4.svg)](https://slack.zappa.io/)
[![Gun.io](https://img.shields.io/badge/made%20by-gun.io-blue.svg)](https://gun.io/)
[![Patreon](https://img.shields.io/badge/support-patreon-brightgreen.svg)](https://patreon.com/zappa)

# Final Release

Thanks to everyone who has supported this package of Zappa utilities for Django! Many of these utilities have become deprecated as new features have been added to AWS, or split into their own projects such a `django-s3-sqlite`: https://github.com/flipperpa/django-s3-sqlite

We're making one final release and will not be accepting further issues or pull requests.

# Description

Small utilities for making [Zappa](https://github.com/Miserlou/Zappa) deployments slightly easier for Django applications.

This project was inspired by Edgar Roman's [Zappa Django Guide](https://github.com/edgarroman/zappa-django-guide).

## Installation

Install via `pip`:
    
    $ pip install zappa-django-utils

Add to your installed apps:

    INSTALLED_APPS += ['zappa_django_utils']

## Usage

### Using an S3-Backed Database Engine - DEPRECATED!

Use `django-s3-sqlite` instead, as it has an updated SQLite driver compatible with current versions of Django:

https://github.com/flipperpa/django-s3-sqlite

### Creating a Postgres Database

Once you have your RDS set up, your VPC/Subnet/Security Groups set up, and your `DATABASES` setting set up, you can create the database with:

    $ zappa manage <stage> create_pg_db

Then you're ready to `python manage.py makemigrations` and `zappa update; zappa manage <stage> migrate`!

### Creating a Default Admin User 

You'll probably need a default user to manage your application with, so you can now:

    $ zappa manage <stage> create_admin_user

Or you can pass some arguments:
   
    $ zappa manage <stage> create_admin_user one two three

This will internally make this call:

```python
User.objects.create_superuser('one', 'two', 'three')
```

Now log in and immediately change the admin user's email and password.

### Creating/Dropping a Postgres Schema

You can create a [Postgres schema](https://www.postgresql.org/docs/current/static/ddl-schemas.html) with:

    $ zappa manage create_pg_schema

and drop it with:

    $ zappa manage drop_pg_schema

## License

(c) 2017, Rich Jones, MIT License
