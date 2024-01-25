#!/bin/sh

cd 
source django/bin/activate
cd cdac_django
python3 manage.py test blogs
python3 manage.py test writers