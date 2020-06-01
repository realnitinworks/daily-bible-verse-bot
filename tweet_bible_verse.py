# import modules
import os
from datetime import date

import tweepy
import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# define constants
BIBLE_VERSE_URL = "https://www.biblegateway.com/"
LOG_FMT = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
LOG_FILE = "bible_verse_bot.log"
CONSUMER_KEY = os.environ['cs_key']
CONSUMER_SECRET = os.environ['cs_secret']
ACCESS_TOKEN = os.environ['acc_token']
ACCESS_SECRET = os.environ['acc_secret']
TODAY = date.today()

# set up a logger
logging.basicConfig(
    level=logging.DEBUG,
    format=LOG_FMT,
    datefmt="%H:%M:%S",
    filename=LOG_FILE,
    filemode='a'
)


def twitter_authenticate():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)


def get_bible_verse():
    response = requests.get(BIBLE_VERSE_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    verse = soup.select(".votd-box > p")[0].text
    verse_url = urljoin(BIBLE_VERSE_URL, soup.select(".votd-box > a")[0]['href'])
    return f'"{verse}" - {verse_url}'


def _already_posted(tweet):
    with open(LOG_FILE) as f:
        return any(
            f"{TODAY} {tweet}" in line
            for line in f
        )


def tweet_bible_verse(api, tweet):
    if _already_posted(tweet):
        logging.warning(f"Skip posting to twitter: {tweet} - already posted")
        return None

    try:
        api.update_status(tweet)
        logging.info(f"Successfully posted to Twitter: {TODAY} {tweet}")
    except Exception as e:
        logging.error(f"Error posting to twitter: {e}")


def main():
    api = twitter_authenticate()
    tweet = get_bible_verse()
    tweet_bible_verse(api, tweet)


if __name__ == '__main__':
    main()

