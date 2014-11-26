scheduler_tweet
===============

Django App for schedule tweet. You create a new configuration (app key, app secret, oauh token and oauth token secret) . After this you should create a new tweet using this config. Define a date ... Voilá. Wait and you will seed your tweet.

Install
========

I assume that you have installed: git, python, postgresql, virtualenv and virtualenvwrapper.

First create a virtualenv for the project.

	$ mkvirtualenv schedule_twitter
	$ workon schedule_twitter

After, git clone project:

	$ git clone https://github.com/aoqfonseca/scheduler_tweet.git

Go to dir where you cloned:

	$ make setup

With this, you ready to run and contrib. 

For run:

	$ make run

In local, this django app use a sqlite db. You can chance to use local postgresql. 