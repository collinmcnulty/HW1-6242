import time
import tweepy
import json
def loadKeys(key_file):
    # TODO: put in your keys and tokens in the keys.json file,
    #       then implement this method for loading access keys and token from keys.json
    # rtype: str <api_key>, str <api_secret>, str <token>, str <token_secret>

    # Load keys here and replace the empty strings in the return statement with those keys
    json_data = open(key_file).read()
    data = json.loads(json_data)
    return data['api_key'],data['api_secret'],data['token'],data['token_secret']


KEY_FILE = 'keys.json'
OUTPUT_FILE_FOLLOWERS = 'followers.csv'
OUTPUT_FILE_FRIENDS = 'friends.csv'
ROOT_USER = 'PoloChau'
NO_OF_FOLLOWERS = 10
NO_OF_FRIENDS = 10


api_key, api_secret, token, token_secret = loadKeys(KEY_FILE)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)


ids = []
x=tweepy.Cursor(api.friends, screen_name="collinmcnulty").pages(1)
for page in x:
    for user in page:
        ids.append(user.screen_name)
    time.sleep(1)

print ids