import nltk
import tweepy
import time
import config
from listeners import TweetStreamListener
from reportHelper import printReport

def nltkConfigure():
	#Download nltk packages if not present already
	print "Checking and downloading required nltk packages "
	punktDownload =	nltk.download('punkt', quiet=True)
	taggerDownload =	nltk.download('averaged_perceptron_tagger', quiet=True)
	return punktDownload and taggerDownload


def main():
	#Authenticating with twitter api
	auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)
	api = tweepy.API(auth)

	keyword = raw_input("Please enter the keyword to track : ")

	#streamBuffer to buffer the incoming tweets from twitter api
	streamBuffer = []
	tweetStreamListener = TweetStreamListener(streamBuffer)
	tweetStream = tweepy.Stream(auth = api.auth, listener = tweetStreamListener)
	tweetStream.filter(track=[keyword], async=True)

	print "Please Wait while generating report..."

	try:
		while True:
			time.sleep(config.monitorInterval * 60)
			printReport(streamBuffer)

	except KeyboardInterrupt:
		print "Exiting Program. Closing Stream"
		tweetStream.disconnect()

if __name__ == '__main__':
	if nltkConfigure():
		print "nltk packages downloaded"
		main()
	else:
		print "Couldnt download required nltk packages"
