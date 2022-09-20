"""
There is a concept that Jose uses here that he calls letting your errors
"bubble up". This is referring to when you catch all the errors and make
the program super user friendly. Good for when you don't want to bombard
the user with error messages, bad for when you are trying to troubleshoot.
this is why "re-raising" errors is helpful
"""


# Class that stores user data
class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        # Better to first define a classes' properties inside of
        # the __init__ method...
        self.score = 0

    def __repr__(self):
        return f'<User {self.name}>'


# Calculates user's engagement score based on 'clicks' and 'hits'
def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


# Simply prints out notification to user
def send_engagement_notification(user):
    print(f'Notification sent to {user}.')


# Sends an email to user if score exceeds 500
def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        # Including a 'raise' keyword in an except block causes the 
        # terminal to also prints out the traceback
        raise
    # Only runs, if no errors are catched... (On Success Block)
    else:
        if user.score > 500:
            send_engagement_notification(user)


my_user = User('Rolf', {'click': 61, 'hits': 100})
email_engaged_user(my_user)