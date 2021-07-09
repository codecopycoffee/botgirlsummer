import tweepy
import datetime

consumer_key = 'placeholder_key_123'
consumer_secret = 'placeholder_secret_345'
access_token = 'placeholder_token_678'
access_token_secret = 'placeholder_token_secret_910'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def chirp():
	if datetime.date.today().weekday() == 0:
		msg = 'Oh man, Monday again!? Okay, we\'re gonna get through this. Drink some water, take deep breaths, and stay calm! #mondaymotivation #botgirlsummer #hotgirlsummer'
	if datetime.date.today().weekday() == 1:
		msg = 'Taco Tuesday? Heck yeah! Nourish your body with your favorite food today, even if that isn\'t tacos (but let\'s be real... it\'s probably tacos). #tacotuesday #botgirlsummer #hotgirlsummer'
	if datetime.date.today().weekday() == 2:
		msg = 'Hump day? More like bump day - play your fave jams today and dance like no one\'s watching! They\'re probably not watching. I mean, maybe close your blinds? #wednesdaywisdom #botgirlsummer #hotgirlsummer'
	if datetime.date.today().weekday() == 3:
		msg = 'It\'s THIRSTday, time go get hydrated! Grab your fave glass, mug, bottle, or even a freakin\' goblet if you want to, it\'s your life, just make sure you fill that sucker up all the way and enjoy some water! #thursdaythoughts #botgirlsummer #hotgirlsummer'
	if datetime.date.today().weekday() == 4:
		msg = 'TGIF amiright?? Cheers to the freakin\'n weekend, beautiful! You are a superstar and don\'t you dare forget it! #fridayfeeling #botgirlsummer #hotgirlsummer'
	if datetime.date.today().weekday() == 5:
		msg = 'It\'s Saturday, you absolute legend. You know what you should do today? Go follow @dglewisofficial and read his latest blog post over on https://dglewisofficial.com. #saturYAY #botgirlsummer #hotgirlsummer'
	if datetime.date.today().weekday() == 6:
		msg = 'It\'s self care sunday! Make sure to do something nice for yourself today, even if it\'s just reminding yourself what a wonderful person you are. :) #sundayfunday #botgirlsummer #hotgirlsummer'

	api.update_status(msg)

chirp()
