# WeWereOnABreakBot

## What is it?

WeWereOnABreakBot is a Reddit bot made to reply comments with [Friends](https://en.wikipedia.org/wiki/Friends) quotes.

## How To Run

1. Create a file named `praw.ini` on the root of the repository
2. Fill the file with the following information:
   ```text
   [WeWereOnABreakBot]
   client_id=yourclientid
   client_secret=yourclientsecret
   password=yourpassword
   username=yourusername
   bot_name=yourbotname
   bot_version=yourbotversion
   bot_author=yourbotauthor
   user_agent=%(bot_name)s:v%(bot_version)s (by u/%(bot_author)s)
   ```
3. Run `main.py`