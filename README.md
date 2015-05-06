# Django Hipchat Quote of the Day

This app allows you to store your own custom set of quotes and sends them to hipchat
at pre-defined times (every day at 12pm by default).

## Installation

Clone this repo to the desired location

pip install -r requirements.txt

Add the following settings to your settings.py

1. HIPCHAT_ROOM_ID (the room where you want the quotes to appear)
2. HIPCHAT_AUTH_TOKEN (the token to authenticate with hipchat api)

add 'django_hipchat_qotd' to your INSTALLED_APPS

run python manage.py syncdb
run python manage.py installtasks

That's it. 

## Requirements

1. python requests
2. django-kronos
