#!/bin/sh

python3 -m venv new
source new/bin/activate
pip3 install -r requirements.txt
python3 manage.py test blogs
python3 manage.py test writers