import tweepy
import datetime
from keys import *

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Python dates are formatted YYYY,M,D
today = datetime.date.today()

game_dates_2324 = [datetime.date(2023,9,2),datetime.date(2023,9,9),datetime.date(2023,9,16),datetime.date(2023,9,23),datetime.date(2023,10,7),datetime.date(2023,10,14),datetime.date(2023,10,21),datetime.date(2023,10,28),datetime.date(2023,11,4),datetime.date(2023,11,11),datetime.date(2023,11,18),datetime.date(2023,11,25)]

opponents_2324 = ["Indiana","Youngstown State","Western Kentucky","Notre Dame","Maryland","Purdue","Penn State","Wisconsin","Rutgers","Michigan State","Minnesota","Michigan"]

i = 0
while i < len(game_dates_2324):
    if today <= game_dates_2324[i]:
        break
    i += 1

days_until = game_dates_2324[i] - today

if days_until.days == 0: 
    message = f"IT'S GAMEDAY! The Ohio State Buckeyes are kicking off against {opponents_2324[i]} today."
elif days_until.days == 1:
    message = f"There is {days_until.days} day until The Ohio State Buckeyes kickoff against {opponents_2324[i]}."
else:
    message = f"There are {days_until.days} days until The Ohio State Buckeyes kickoff against {opponents_2324[i]}."


print(message)

client.create_tweet(text=message)
