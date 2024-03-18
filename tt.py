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

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,
                       consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

text = "hello💀"
client.create_tweet(text=text)
print(f"tweet send >> {text}")
