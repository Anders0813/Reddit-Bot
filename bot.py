import praw
import requests
import time
import webbrowser

reddit = praw.Reddit("bot1", user_agent="windows:com.example.myredditapp:v1.0.0 (by u/Anders0813)")
#for submission in reddit.subreddit("learnpython").hot(limit=10):
    #print(submission.title)
subreddit = reddit.subreddit('all')
count = 0
for submission in subreddit.hot(limit=10):
    try:
        count += 1
        print(30*'_')
        #print("{}: {}   Score: {}".format(count , submission.title.encode('ascii', 'ignore'), submission.score))
        print(submission.title.encode('ascii', 'ignore').decode('ascii'))
        print(submission.upvote_ratio)
            #r = requests.put('http://10.0.0.130/api/9JVUTcSARgvlMjdaDnjvU4DPyffF7zgvZ5DAnIN6/groups/1/action', data = '{"on": false}')
            #time.sleep(.300)
            #r = requests.put('http://10.0.0.130/api/9JVUTcSARgvlMjdaDnjvU4DPyffF7zgvZ5DAnIN6/groups/1/action', data = '{"on": true}')
            #webbrowser.open(submission.url)  # Go to example.com
    except praw.exceptions.PRAWException as e:
        pass


#if submission.link_flair_text == 'DD':
