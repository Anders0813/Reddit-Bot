import praw
reddit = praw.Reddit("bot1", user_agent="windows:com.example.myredditapp:v1.0.0 (by u/Anders0813)")
for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)
