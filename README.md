# modmail-autoreply
For those times when you're out of the office for that 'unpaid volunteer' work you do for a for-profit company, this small script will auto-reply to new messages sent to your modmail inbox. You can customize it however you want trivially - it's only 27 lines!

### Quickstart

Assumes you already have Python installed and are comfortable with basics.

1. Clone this repository to your local system
2. Copy `config.example.py` to a new file, `config.py`
3. Obtain Reddit API credentials and place them in `config.py`. Not familiar with how to get API credentials? Use [JC Chouinard's guide](https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/)!
4. Edit the `body` on line 23 with whatever text you want to autoreply to modmail with
5. Run `python3 autoreply.py` and the bot will leave your out-of-office/we-are-blackout reply for as long as the script is running

### Quirks

This bot will ignore ban appeals, moderator discussions, join requests, etc. to *try to* avoid disrupting other discussions. However if you have a long-lived conversation thread and someone makes a new reply, this bot won't care and will throw up the autoreply + archive.

This bot and attempts to *only reply to each conversation thread once*, so if there is a question not answered by your out-of-office message then people can reply and still reach through to moderators.

The conversation thread deduplication is in-memory, so if you close and restart the script it will lose this memory. It also means the memory usage of the program could grow unbounded, however this is unlikely in practice unless your modmail is being *attacked*.
