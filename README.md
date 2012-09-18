Django Bootstrap Starter
========================

Django project template that comes with the following batteries included:

* [Django](https://www.djangoproject.com/) 1.4
* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) 2.1
* JS libraries: 
	- [Jquery 1.7.2](http://jquery.com/)
	- [Datatables 1.9.3](http://datatables.net/) (for fancy html tables, [compatible with Twitter Bootstrap](http://datatables.net/release-datatables/extras/TableTools/bootstrap.html))
	- [NVD3](http://nvd3.com/) (for graphics)
	- [Bootstrap datepicker](https://github.com/Aymkdn/Datepicker-for-Bootstrap) (Aymkdn version, better than the [original bootstrap datepicker](http://www.eyecon.ro/bootstrap-datepicker/))
* Python Apps:
	- [Django Crispy Forms](https://github.com/maraujop/django-crispy-forms) (for customizing forms, Twitter Boostrap support)
	- [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) (for easy debugging)
	- [Django REST Framework](http://django-rest-framework.org/) (optional, for making a RESTful API)

Run example App
-----------

* Install pip: sudo apt-get install pip
* Install mysql interface to python: python-mysqldb
* Install Django: sudo pip install django
* (Navigate to project folder) Download python plugins and libraries: ``pip install -r requirements.txt`` 
* Create database for project (example mysql):
```sudo mysql -u root -p
CREATE DATABASE django_bootstrap_starter
```
* Create db tables``python manage.py syncdb``
* Run! ``python manage.py runserver``