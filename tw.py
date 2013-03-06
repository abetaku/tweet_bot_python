# coding: utf-8

import tweepy
from twkeys import TwKeys

class Tw:

	def __init__(self):
		keys = TwKeys()
		c_key, c_secret, a_token, a_token_secret = keys.get()

		self.auth = tweepy.OAuthHandler(c_key, c_secret)
		self.auth.set_access_token(a_token, a_token_secret)
	
	def tweet_post(self, tweet):		
		api = tweepy.API(self.auth)
		api.update_status(tweet)


if __name__ == '__main__':
	app = Tw()
	app.tweet_post("Hello World!")


