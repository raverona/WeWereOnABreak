import praw

reddit = praw.Reddit('WeWereOnABreakBot')

subreddit = reddit.subreddit('all')
counter = 0

for comment in subreddit.stream.comments():
    if "slept with someone else" in comment.body.lower():
        comment.reply("[WE WERE ON A BREAK!](https://media1.giphy.com/media/xUOwGaK4KQ9Z6WZqso/giphy.gif)")
