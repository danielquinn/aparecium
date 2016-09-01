# Aparecium

A quick &amp; dirty way to read my friend's private RSS feed


## What This Does

I have a friend who keeps a private blog on WordPress, and I'd like to keep
tabs on it.  However, its privateness means that I can't just put the RSS URL
into my feed reader (Thunderbird) because it barfs at the login screen on
every poll.

This script lets me run a tiny webserver locally that when queried, does some
mechanize-gymnastics to log into Wordpress and fetch the feed I want.


## How to Use It

It's a typical Flask project:

* Run `pip install -r requirements.txt`
* Copy `config.example.json` to `config.json` and edit it to include the
  URL(s) of the blog(s) you want to read, and the username/password you'll
  have to use for each.
* Run `python aparecium.py`


## Colophon

This script reveals that which was initially hidden, so I named it for the
spell from the Harry Potter series with the same name.

