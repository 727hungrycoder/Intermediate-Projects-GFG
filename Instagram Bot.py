from instapy import InstaPy

session = InstaPy(username="your username", password="your password")
session.login()
session.like_by_tags(["dance", "mercedes"], amount=10, interact=True)
session.set_dont_like(["naked", "murder", "nsfw"])
session.set_do_comment(True, percentage=100)
session.set_comments(["Nice", "Amazing", "Super"])
session.set_do_follow(enabled=True, percentage=100)
session.set_user_interact(amount=1, randomize=True, percentage=100)
session.end()
