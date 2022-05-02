#! /usr/bin/env bash

sleep 10;
python livuar/manage.py makemigrations

sleep 10;
python livuar/manage.py migrate

sleep 10;
python livuar/manage.py runserver 0.0.0.0:8000