import tldextract
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
import datetime


def getTweetsByUser(activeTweets):
	tweetsByUser = defaultdict(list)
	for tweet in activeTweets:
		tweetsByUser[tweet["user"]].append(tweet)
	return tweetsByUser

def getUrls(activeTweets):
	urls = []
	for tweet in activeTweets:
		urls = urls + tweet["urls"]
	return urls
	
def getDomainOccurance(urls):
	domainsOccurance = defaultdict(int)
	for url in urls:
		domainName = tldextract.extract(url).registered_domain
		domainsOccurance[domainName] = domainsOccurance[domainName] +1
	return domainsOccurance

def getWordOccurance(activeTweets):
	wordOccurance = defaultdict(int)
	for tweet in activeTweets:
		tokenizedWords = tweet["tweet"].split()
		taggedPartOfSpeech = nltk.pos_tag(tokenizedWords)
		for tags in taggedPartOfSpeech:
			#Remove common words and non alphabetical strings
			if tags[1].startswith('N') and tags[0].isalpha():
				wordOccurance[tags[0]] = wordOccurance[tags[0]] + 1	
	return wordOccurance
	
def getActiveTweets(streamBuffer, expiryMinutes):
	activeTweets = []
	expiryTime = datetime.datetime.now() - datetime.timedelta(minutes = expiryMinutes)
	for eachTweet in streamBuffer:
		if eachTweet["timeStamp"] > expiryTime:
			activeTweets.append(eachTweet)
		else:
			pass
	return activeTweets

