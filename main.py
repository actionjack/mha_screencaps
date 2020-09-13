import random
import os
import tweepy
import tempfile
import urllib.request
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

episodeTitles = ['Izuku Midoriya: Origin', 'What It Takes to Be a Hero', 'Roaring Muscles', 'Start Line', 'What I Can Do for Now', 'Rage, You Damn Nerd', 'Deku vs. Kacchan', "Bakugo's Start Line", 'Yeah, Just Do Your Best, Iida!', 'Encounter with the Unknown', 'Game Over', 'All Might', 'In Each of Our Hearts', "That's the Idea, Ochaco", 'Roaring Sports Festival', 'In Their Own Quirky Ways', 'Strategy, Strategy, Strategy', 'Cavalry Battle Finale', 'The Boy Born with Everything',
                 'Victory or Defeat', 'Battle on, Challengers!', 'Bakugo vs. Uraraka', 'Shoto Todoroki: Origin', 'Fight on, Iida', 'Todoroki vs. Bakugo', 'Time to Pick Some Names', 'Bizarre! Gran Torino Appears', 'Midoriya and Shigaraki', 'Hero Killer: Stain vs U.A. Students', 'Climax', 'The Aftermath of Hero Killer: Stain', "Everyone's Internships", 'Listen Up!! A Tale from the Past', 'Gear Up for Final Exams', 'Yaoyorozu: Rising', 'Stripping the Varnish', 'Katsuki Bakugo: Origin', 'Encounter']

randomEpNum = random.randint(1, 36)
randomEpNumStr = str(randomEpNum).zfill(2)

if randomEpNum < 14:
    season = 1
    randomImgNum = random.randint(1, 728)
    randomImgNumStr = str(randomImgNum).zfill(4)
    url = 'https://images.fancaps.net/images/anime/Hero_Academia/ep{}/Hero_Academia_Screenshot_{}.jpg'.format(
        randomEpNumStr, randomImgNumStr)
else:
    season = 2
    randomImgNum = random.randint(1, 716)
    randomImgNumStr = str(randomImgNum).zfill(4)
    url = 'https://images.fancaps.net/images/anime/Hero_Academia/ep{}/ep{}_Screenshot_{}.jpg'.format(
        randomEpNumStr, randomEpNumStr, randomImgNumStr)

keyName = 'ep{}_img{}'.format(randomEpNumStr, randomImgNumStr)
key = keyName.lower() + '.png'

temp_dir = tempfile.gettempdir()
path = os.path.join(temp_dir, key)

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')]
urllib.request.install_opener(opener)

with urllib.request.urlopen(url) as url:
    with open(path, 'wb') as f:
        f.write(url.read())

episodeTitle = episodeTitles[randomEpNum - 1]

api.update_with_media(
    path, status="S{}EP{} | {} #MHA #MyHeroAcademia".format(season, randomEpNumStr, episodeTitle))

# Standard tweet
# api.update_status(status="test tweet")
