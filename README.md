<br />
<p align="center">
  <a href="https://github.com/cranjis-mcbasketball/mother-coconuts-german-automotive-marketplace">
    <img src="https://imgur.com/tNFdroW.png" alt="Logo" width="70" height="70">
  </a>

  <h3 align="center">Mother Coconuts' German Automotive Marketplace</h3>

  <p align="center">
  A Django RESTful API built for <a href="https://github.com/cranjis-mcbasketball/mother-coconuts-german-automotive-marketplace">Audi, VW, and Porsche Owners</a> 
    <a href="https://github.com/cranjis-mcbasketball/mother-coconuts-german-automotive-marketplace"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    View Demo (coming soon)
    ·
    <a href="https://github.com/cranjis-mcbasketball/mother-coconuts-german-automotive-marketplace/issues">Report Bug</a>
    ·
    <a href="https://github.com/cranjis-mcbasketball/mother-coconuts-german-automotive-marketplace/issues">Request Feature</a>
  </p>
</p>

### Install

Creating and activating virtual environment

    create venv: python -m venv ./path/to/new/virtual/environment
    activate venv: <venv>\Scripts\Activate.ps1

Installing requirements and making migrations

    python -m pip install --upgrade pip
    pip install -r requirements.txt
    cd bazaar
    python ../manage.py makemigrations
    python ../manage.py migrate
    python ../manage.py runserver

Once connected to the server...

To create a new admin account, run command: > python manage.py createsuperuser

To sign in to admin account in browser:
navigate to http://127.0.0.1:8000/admin
