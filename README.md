django-bootstrap-starter
========================

Django project template using Bootstrap, Django Crispy Forms and other predefined tools

* [Django](https://www.djangoproject.com/) 1.4
* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) 2.1
* JS libraries included: 
	- [Jquery 1.7.2](http://jquery.com/)
	- [Datatables 1.9.3](http://datatables.net/) (for fancy html tables, [compatible with Twitter Bootstrap](http://datatables.net/release-datatables/extras/TableTools/bootstrap.html))
	- [NVD3](http://nvd3.com/) (for graphics)
	- [Bootstrap datepicker](https://github.com/Aymkdn/Datepicker-for-Bootstrap) (Aymkdn version, better than the [original bootstrap datepicker](http://www.eyecon.ro/bootstrap-datepicker/))
* Python Apps included:
	- [Django Crispy Forms](https://github.com/maraujop/django-crispy-forms) (for customizing forms, Twitter Boostrap support)
	- [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) (for easy debugging)
	- [Django REST Framework](http://django-rest-framework.org/) (optional, for make a RESTful API)

Instalation
-----------

* Download python plugins and libraries: ``pip install -r requirements.txt`` 
* Create database for project:
``sudo mysql -u root -p

CREATE DATABASE django_bootstrap_starter

python manage.py syncdb``
* 
