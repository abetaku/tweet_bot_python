##Introduction

tweet_bot_python is one of simple twitter bot templetes.


##Configuration

Before using this, you need to set a few environment variables on your PC.
tweet_bot_python requires the following values for running.

TWITTER_CONSUMER_KEY = 'YOUR TWITTER CONSUMER KEY'  
TWITTER_CONSUMER_KEY_SECRET = 'TWITTER CONSUMER_KEY SECRET'  
TWITTER_ACCESS_TOKEN = 'TWITTER ACCESS TOKEN'  
TWITTER_ACCESS_TOKEN_SECRET = 'TWITTER ACCESS TOKEN SECRET'  


##Usage

```python
from tw import TW  
app = TW()  
app.tweet_post("Hello World!")  
```


