# contact-collector

Simple Django framework for collecting contact data.


## Installation

* Requirements

  * git
  * Python 3.5
  * virtualenv

* Steps (for Linux)

  * install Python
  * clone repository

    ```
    git clone https://github.com/fracpete/contact-collector.git
    ```

  * change into `contact-collector` directory
  * set up virtual environment

    ```
    virtualenv -p /usr/bin/python3.5 venv
    ```

  * install Django and required dependencies

    ```
    ./venv/bin/pip install Django
    ./venv/bin/pip install django_excel
    ./venv/bin/pip install pyexcel-xls
    ```

  * setup database

    ```
    ./venv/bin/python contactcollector/manage.py makemigrations
    ./venv/bin/python contactcollector/manage.py migrate
    ```

  * create superuser

    ```
    ./venv/bin/python contactcollector/manage.py createsuperuser
    ```

Optional:

  * open webbrowser at http://localhost:8000/admin/
  * add additional users with **staff** flag set (gives access to the admin interface)


## Usage

* change into project directory
* start up local webserver

  ```
  ./venv/bin/python contactcollector/manage.py  runserver
  ```

* open webbrowser at http://localhost:8000/admin/
* log in

