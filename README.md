CharterWebsite
==============

Princeton Charter Club's Grand Old Website

### How to run the server:

Type this into ther terminal:

    python manage.py runserver

Then navigate to the URL it gives you, and you should be accessing the site!


Run these commands when you first download the repo:
---

- This sets up a directory to store executables of files unique to this project. This way, if this project requires Django 1.7, but your computer actually has Django 1.8 installed, turning on the virtual env (using "source ..." below) will force your computer to use Django 1.7.

        virtualenv venv

- Turn on the virtual environment:

        source venv/bin/activate

This changes the location of all of the dependencies to be ./venv/bin/activate instead of /usr/local/bin. All of the executable files needed to run this website are in that folder already, and this allows all of us to test the website with the same installed version of software.

If you don't run this command, you will likely be missing a bunch of software. Sorry :(

- Install the required packages:

        pip install django-toolbelt

- Install the CAS authentication:

        cd django-cas
        python setup.py install
        cd ..

This installs the authentication package needed for Django onto your system.

- Install [Postgres](http://postgresapp.com/)!

This way, when we start making calls to the database and you try to test the changes locally on your computer, you'll still be able to.

Open 'psql' and run:

        CREATE ROLE admin LOGIN PASSWORD 'kernighan';
        CREATE DATABASE chartermembers;

This creates a role that can login to the database `chartermembers`. You will
use this below. See the [video](https://docs.google.com/a/princeton.edu/file/d/0B6HetodYPhDwX3NtTlVQc19YQ2s/edit).

- Setup the database according to Django's specifications.

        python manage.py migrate
        python manage.py syncdb

It will ask you to create an admin. Use the login credentials in
`charterclub/local_settings.py`. Say yes, and use the following:

        Username: admin
        Password: kernighan

- Run it and see if everything works!

        python manage.py runserver

Then navigate to http://127.0.0.1:8000/, and if you see a success page, then you're good!

- Once you're done developing, exit your virtual environment with:

        deactivate

Yay! Questions?


Pushers
---

Are you a pusher (to Heroku)? If so follow these instructions!

- Add heroku.com as the `heroku` remote to your git:

        heroku git:remote -a charterclub
        git remote -v

You should see both `origin` and `heroku` as a remote after you type that second line.

- Set up a `release` branch that tracks whatever you have pushed onto Heroku. All pushes will be done from this branch, as it includes the commit that deletes `local_settings.py` and removes the `@login_required` decorators.

        git checkout -b release heroku/master

You've now set up your release branch!

When there are changes on `master` that you want to release to the public, do the following:

- Update your `master` branch with the most recent changes. Whatever is on your local copy of `master` is what will be pushed.

        git checkout master
        git pull -r

- Pull changes from `heroku/master` so that you have the changes from the last person who pushed:

        git checkout release
        git pull -r

- Merge in the new changes from your local copy of `master`.

        git merge master
        git log

You should see all of the new commits plus a "merge" commit in your `release` branch.

- Push to heroku!

        git push heroku master


Git Help
---
See "git protocols" doc in the wiki for more information.

Congrats! You've cloned the repo. Here's what you want to do if you want to submit a change:

- Edit your files.
- Add all files to the staging area. If you don't add files to the staging area, git won't recognize them, and won't share them with everyone else.

        git add .

- Commit your changes. Bundle all of your changes into one "commit," which is tagged with a commit message and sent to the remote repo.

        git commit -m "[1-word description] Commit Message Here"

- Update with what everyone else is doing! You want to stay updated with all of the changes everyone else does, so run:

        git pull --rebase

"pull" simply fetches all changes; "rebase" adds your changes onto the changes that have been fetched.

- If you're done testing (and **ONLY** if you're don't testing), share your changes with everyone else.

        git push

If you don't test your code, and what you push breaks everyone else's copy of the code, **SHAME ON YOU**!

