# daily-bible-verse-bot
A twitter bot that posts the daily Bible verse to Twitter. It scrapes the daily Bible verse from [BibleGateway.com](https://www.biblegateway.com/)
and then use the tweepy API to post the verse as status to Twitter.

I have deployed this on Heroku and added a scheduler to run the app daily.

An example tweet posted on my Twitter is [here](https://twitter.com/nitin_cherian/status/1177425212327026688)


# Setting up to run the app

>$ git clone https://github.com/realnitinworks/daily-bible-verse-bot.git

>$ mv .env_example .env

>$ # Key in your twitter credentials into the environment variables in .env 

>$ pipenv install

>$ pipenv shell

