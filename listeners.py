import tweepy
import datetime as dTime


class TweetStreamListener(tweepy.StreamListener):
	def __init__(self, streamBuffer):
		#Buffer to store the incoming stream with added timestamp
		self.streamBuffer = streamBuffer
		tweepy.StreamListener.__init__(self)

	def on_status(self, status):
		#Invoked on arrival of a new tweet
		tweet = status._json
		if not self.isRetweet(tweet):
			timeStamp = dTime.datetime.now()
			urls = tweet["entities"]["urls"]
			expandedUrls = self.getExpandedUrls(urls)
			dataDict = { "user": tweet["user"]["screen_name"], "urls": expandedUrls, "tweet": tweet["text"], "timeStamp": timeStamp }
			self.streamBuffer.append(dataDict)
		else:
			pass

	def isRetweet(self, tweet):
		#For checking if the tweet is retweeted or new
		if tweet['retweeted'] and tweet['text'].startswith('RT @'):
			return True
		else:
			return False

	def getExpandedUrls(self, urls):
		#For extracting expanded urls from stream
		expandedUrls = []
		for url in urls:
			expandedUrl = url["expanded_url"]
			expandedUrls.append(expandedUrl)
		return list(set(expandedUrls))
