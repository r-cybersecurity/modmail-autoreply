from config import *
import praw


ooto_message = "Hello, r/cybersecurity is currently participating in a blackout and will not be accessible for 48h. Please monitor https://cybersecurity.page for updates, thanks!"
ooto_subreddit = "cybersecurity"

reddit = praw.Reddit(
    client_id=praw_client_id,
    client_secret=praw_client_secret,
    refresh_token=praw_refresh_token,
    user_agent="r-cybersecurity/modmail-autoreply",
)

subreddit = reddit.subreddit(ooto_subreddit)

replied_conversations = []
for conversations in subreddit.mod.stream.modmail_conversations(state="inbox"):
    conversation_id = conversations.id

    if conversation_id in replied_conversations:
        print(f"Skipped reply to {conversation_id} as autoreply already fired")
        continue

    # want to do more to analyze or reply? here are the ModmailConversation docs:
    # https://praw.readthedocs.io/en/stable/code_overview/models/modmailconversation.html
    message = subreddit.modmail(conversation_id, mark_read=True)
    message.reply(body=ooto_message, author_hidden=True)
    message.archive()
    
    print(f"Replied to {conversation_id} and archived")
    replied_conversations.append(conversation_id)