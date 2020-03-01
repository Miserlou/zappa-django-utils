import os
import sys
from setuptools import setup
from io import open

# New PyPI handles markdown! Yay!
with open('README.md') as f:
    README = f.read()

# Set external files
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), 'test_requirements.txt')) as f:
    test_required = f.read().splitlines()

setup(
    name='zappa-django-utils',
    version='0.4.1',
    packages=['zappa_django_utils'],
    install_requires=required,
    tests_require=test_required,
    test_suite='nose.collector',
    include_package_data=True,
    license='MIT License',
    description='Helpers for Django Zappa deployments',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/Miserlou/zappa-django-utils',
    author='Rich Jones',
    author_email='rich@openwatch.net',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
