# Django Collins

Collins is a simple blogging application for Django, inspired by [Tumblr](http://tumblr.com/), [Projectionist](http://project.ioni.st/), &c.

Doesn't really do much yet. Still in the early stages of development.

## Prerequisites

* [Python](http://python.org/) (2.6 required for the [@post_type](https://github.com/lapilofu/django-collins/blob/master/collins/decorators.py#L4) [class decorator](http://www.python.org/dev/peps/pep-3129/). Earlier versions should work if you are not using the decorator.)
* [Django 1.3+](http://www.djangoproject.com/)
* (Optional) [django-south](http://south.aeracode.org/)

In addition, if you are working on development and want to change the stylesheets for user interface, you will need [Sass](http://sass-lang.com/) with [Compass](http://compass-style.org/).
