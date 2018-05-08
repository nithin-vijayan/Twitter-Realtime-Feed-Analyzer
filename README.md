# Twitter-Realtime-Feed-Analyzer
To analyse realtime twitter feeds to generate reports based on tweets

# Setup:

All the required packages are defined in requirements.txt

1. Clone the repository to you local system ```git clone git@github.com:nithin-vijayan/Twitter-Realtime-Feed-Analyzer.git```

2. run  ```pip install -r requirements.txt```  for installing all the required packages

nltk packages for text parsing will be downloaded seperately during program execution. Program might take a while for first execution when downloading these packages

3. Signup in twitter for dev account and create an app to obtain the auth token, auth secret , api token and api secret and define these in config.py file

```
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

4. (Optional) Change the interval for report generating and analyzing window if required values are 1 min and 5 min by default
```
expiryMinutes = 5   #Controls interval to monitor ( Monitor last 5 minute stream )
monitorInterval = 1 #Control duration for report generation (per minute)
```

5. Run the script using ```python main.py```. Enter the keyword to search when prompted 

Program will analyze the tweets matching the keywords and generate the report on metioned intervals.

# Output:

![Alt text](images/screenshot.png?raw=true "Output Terminal")

Use Ctrl+C for exiting the program and close the stream API connection