# Sentiment analyzer

## About

This is a simple sentiment analyzer. It takes a twitter handle and outputs a bar chart visualizing the sentiments of that handles last 200 tweets.

It is my response to the Harvard CS50 course pset6.

## To set up:

1. Create twitter app: apps.twitter.com (any name/ description/ URL, blank callback URL)
2. Go to Keys and Access Tokens to find Consumer Key (API Key) and Consumer Secret (API Secret). Input these values into the terminal in the root directory:

    $ export API_KEY='API Key'
    $ export API_SECRET='API Secret'

## To install dependencies:

pip3 install --user -r requirements.txt

## To run:

$ export FLASK_APP=application.py; flask run
