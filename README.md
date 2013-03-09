
##Introduction

tweet_bot_python is one of simple twitter bot templetes.

****

##Configuration

Before using this, you need to set a few environment variables on your PC.
tweet_bot_python requires the following values for running.

TWITTER¥_CONSUMER¥_KEY=__'YOUR TWITTER CONSUMER KEY'__
TWITTER¥_CONSUMER¥_KEY¥_SECRET=__'TWITTER CONSUMER_KEY SECRET'__
TWITTER¥_ACCESS¥_TOKEN=__'TWITTER ACCESS TOKEN'__
TWITTER¥_ACCESS¥_TOKEN¥_SECRET=__'TWITTER ACCESS TOKEN SECRET'__

****

##Usage

from tw import TW
app = TW()
app.tweet_post("Hello World!")


