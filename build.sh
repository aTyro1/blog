#!/bin/sh

pip freeze > requirements.txt
python3 -m venv new
source new/bin/activate
pip install -r requirements.txt
python3 manage.py test blogs
python3 manage.py test writers