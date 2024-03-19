# def convert_to_24h(time_str, is_pm=False):
#     hours, minutes = time_str.split(':')
#     hours = int(hours)
#     # If it's PM and not 12 PM, add 12 to the hours
#     if is_pm and hours != 12:
#         hours += 12
#     # Format hours back to two digits
#     hours = f"{hours:02d}"
#     return f"{hours}:{minutes}"

# # Example usage:
# def final():
#     final_time = convert_to_24h("12:13", is_pm=True)
#     print(final_time)  # Output: 18:30


# final()
import tweepy
import os

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

twitter_auth_keys = {
    "consumer_key": os.getenv("CONSUMER_KEY"),
    "consumer_secret": os.getenv("CONSUMER_SECRET"),
    "access_token": os.getenv("ACCESS_TOKEN"),
    "access_token_secret": os.getenv("ACCESS_TOKEN_SECRET"),
    "access_bearer_token": os.getenv("BEARER_TOKEN")
}

auth = tweepy.OAuth1UserHandler(
    twitter_auth_keys['consumer_key'],
    twitter_auth_keys['consumer_secret']
)
auth.set_access_token(
    twitter_auth_keys['access_token'],
    twitter_auth_keys['access_token_secret']
)

api_v1 = tweepy.API(auth)

client_v2 = tweepy.Client(consumer_key=twitter_auth_keys['consumer_key'], consumer_secret=twitter_auth_keys['consumer_secret'], access_token=twitter_auth_keys[
                          'access_token'], access_token_secret=twitter_auth_keys['access_token_secret'], bearer_token=twitter_auth_keys['access_bearer_token'])

# Upload media and get media_id
media_path = "capitandola.jpg"
media = api_v1.media_upload(filename=media_path)
media_id = media.media_id

client_v2.create_tweet(text="Your tweet text here", media_ids=[media_id])
print(f"tweet send >>")
