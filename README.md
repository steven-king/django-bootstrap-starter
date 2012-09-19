Django Bootstrap Starter
========================

Django project template that comes with the following batteries included:

* [Django](https://www.djangoproject.com/) 1.4
* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) 2.1
* JS libraries: 
	- [Jquery 1.7.2](http://jquery.com/)
	- [Datatables 1.9.3](http://datatables.net/) (for fancy html tables, [compatible with Twitter Bootstrap](http://datatables.net/release-datatables/extras/TableTools/bootstrap.html))
	- [NVD3](http://nvd3.com/) (optional, for graphics)
	- [Bootstrap datepicker](https://github.com/Aymkdn/Datepicker-for-Bootstrap) (Aymkdn version, better than the [original bootstrap datepicker](http://www.eyecon.ro/bootstrap-datepicker/))
* Python Apps:
	- [Django Crispy Forms](https://github.com/maraujop/django-crispy-forms) (for customizing forms, Twitter Boostrap support)
	- [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) (for easy debugging)
	- [Django REST Framework](http://django-rest-framework.org/) (optional, for making a RESTful API)
	- [South](http://south.aeracode.org/) (for database migrations)

Run example App
-----------

1. Install pip package manager for python and update it to the latest version:

        sudo apt-get install python-pip
        sudo pip install --upgrade pip

* (Navigate to project folder) To install django and plugins:

		pip install -r requirements.txt 

* Probably there is an error with the package distribute(needed for djangorestframework) not being up to date:

        pip install -U distribute
        pip install -r requirements.txt	

* Set up database (example for mysql):

        sudo apt-get install mysql-server mysql-client python-mysqldb
        sudo mysql -u root -p
        CREATE DATABASE django_bootstrap_starter;	

* Create db tables ``python manage.py syncdb``
* Run: ``python manage.py runserver``

