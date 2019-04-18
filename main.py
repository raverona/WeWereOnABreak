import praw
import logging

from reddit_comment_template import reddit_comment_template

reddit = praw.Reddit('WeWereOnABreakBot')

subreddit = reddit.subreddit('WeWereOnABreakBot')

logger = logging.getLogger("main")

for comment in subreddit.stream.comments():
    if "slept with someone else" in comment.body.lower():
        comment_body = reddit_comment_template.substitute(
            message="WE WERE ON A BREAK",
            gif_link="https://media1.giphy.com/media/xUOwGaK4KQ9Z6WZqso/giphy.gif")
        try:
            comment.reply(comment_body)
        except BaseException as exception:
            logger.error("Could not submit reply: " + str(exception))
