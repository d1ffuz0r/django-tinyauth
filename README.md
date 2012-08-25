django-tinyauth
===============

fast login to django admin interface

Support
=======
Django1.4


Installation
============
Install app. Works only with enabled a debug state.

```
$ git clone git://github.com/d1ffuz0r/django-tinyauth.git
$ cd django-tinyauth
$ [sudo] python setup.py install
```

Add app to INSTALLED_APPS at settings.py file

```
    ...
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_tinyauth' # <---
)
```

Set DEBUG = True

```
DEBUG = True
```

See your admin login page

![example](https://dl.dropbox.com/u/11201125/Screen%20Shot%202012-08-21%20at%2012.25.04%20AM.png)

Authors
=======
* Code: Roman Gladkov
* Name: Boxxy
