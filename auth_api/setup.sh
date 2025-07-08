#!/bin/bash

python manage.py migrate
python manage.py init_types
python manage.py runserver 127.0.0.1:8000