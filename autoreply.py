from config import *
import praw
from pprint import pprint

reddit = praw.Reddit(
    client_id=praw_client_id,
    client_secret=praw_client_secret,
    refresh_token=praw_refresh_token,
    user_agent="r-cybersecurity/modmail-autoreply",
)

subreddit = reddit.subreddit("cybersecurity")

dedupe = []
for message_bus in subreddit.mod.stream.modmail_conversations(state="inbox"):
    message_id = message_bus.id

    if message_id in dedupe:
        print(f"Skipped reply to {message_id} as autoreply already fired")
        continue

    message = subreddit.modmail(message_id, mark_read=True)
    message.reply(body="Hello, r/cybersecurity is currently participating in a blackout and will not be accessible for 48h. Please monitor https://cybersecurity.page for updates, thanks!", author_hidden=True)
    message.archive()
    
    print(f"Replied to {message_id} and archived")
    dedupe.append(message_id)