import os

class TwKeys:
	def __init__(self):
		self.consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
		self.consumer_secret = os.getenv("TWITTER_CONSUMER_KEY_SECRET")
		self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
		self.access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

	def get(self):
		return self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret

