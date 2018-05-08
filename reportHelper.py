import config
import operator
from tweetHelper import getActiveTweets, getTweetsByUser, getUrls, getDomainOccurance, getWordOccurance

def generateUserReport(activeTweets):
	userReport = []
	for user,tweets in getTweetsByUser(activeTweets).iteritems():
		userTweet = "%s posted %s Tweet(s)" % (user, len(tweets))
		userReport.append(userTweet)
	return userReport

def generateLinksReport(activeTweets):
	domainReport = []
	urlsConsolidated = getUrls(activeTweets)
	domainOccurance = getDomainOccurance(urlsConsolidated)
	totalUrls = len(urlsConsolidated)
	sortedDomainList = sorted(domainOccurance.items(), key=operator.itemgetter(1), reverse=True)
	for each in sortedDomainList:
		domainInfo = "%s - %s time(s)"%(each[0], each[1])
		domainReport.append(domainInfo)
	return totalUrls, domainReport

def generateContentReport(activeTweets):
	wordReport = []
	wordList = getWordOccurance(activeTweets)
	totalWords = len(wordList)
	sortedwordList = sorted(wordList.items(), key=operator.itemgetter(1), reverse=True)
	for each in sortedwordList[:10]:
		wordInfo = "%s - %s time(s)"%(each[0], each[1])
		wordReport.append(wordInfo)
	return totalWords, wordReport

def printReport(streamBuffer):
	activeTweets = getActiveTweets(streamBuffer, config.expiryMinutes)
	
	print """
		User Report
	"""
	userReport = generateUserReport(activeTweets)
	print "\n".join(userReport)

	print """
		Links Report
	"""
	totalUrls, domainReport = generateLinksReport(activeTweets)
	print "Total Urls : %s" % (totalUrls)
	print "\n".join(domainReport)

	print """
		Content Report
	"""
	totalWords, wordReport = generateContentReport(activeTweets)
	print "Total Words : %s" % (totalWords)
	print "\n".join(wordReport)