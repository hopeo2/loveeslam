import os
from datetime import datetime, timezone
import pytz
import tweepy
import aladhan
import time
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler


load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")


location = aladhan.City("Tehran", "IR")
client_aladhan = aladhan.Client(location)

adhans = client_aladhan.get_today_times()


print("run))")
print("======================================")


def convert_to_24h(time_str, is_pm=False):
    hours, minutes = time_str.split(':')
    hours = int(hours)
    # If it's PM and not 12 PM, add 12 to the hours
    if is_pm and hours != 12:
        hours += 12
    # Format hours back to two digits
    hours = f"{hours:02d}"
    return f"{hours}:{minutes}"


def check_sobh_time():
    adhan_sobh_time = client_aladhan.get_today_times(
    )[0].readable_timing(show_date=False)[0:5]
    city_timezone = pytz.timezone('Asia/Tehran')
    current_time = datetime.now(timezone.utc)
    tehran_time = current_time.astimezone(city_timezone)
    tehran_str = str(tehran_time)
    if str(adhan_sobh_time) == tehran_str[11:16]:
        auth = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret
        )
        auth.set_access_token(
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        api_v1 = tweepy.API(auth)
        client = tweepy.Client(bearer_token=bearer_token,
                               consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)

        # Upload media and get media_id
        media_path = "capitandola1.jpg"
        media = api_v1.media_upload(filename=media_path)
        media_id = media.media_id
        text = "💀کاپیتان دولا راست شو .. نماز صبحه " + str(adhan_sobh_time)
        client.create_tweet(text=text, media_ids=[media_id])
        print(f"tweet send >> {text}")


def check_zohr_time():
    adhan_zohr_time = client_aladhan.get_today_times(
    )[1].readable_timing(show_date=False)[0:5]
    city_timezone = pytz.timezone('Asia/Tehran')
    current_time = datetime.now(timezone.utc)
    tehran_time = current_time.astimezone(city_timezone)
    tehran_str = str(tehran_time)
    final_time = convert_to_24h(adhan_zohr_time, is_pm=True)
    if str(final_time) == tehran_str[11:16]:
        auth = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret
        )
        auth.set_access_token(
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        api_v1 = tweepy.API(auth)
        client = tweepy.Client(bearer_token=bearer_token,
                               consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)


        # Upload media and get media_id
        media_path = "capitandola.jpg"
        media = api_v1.media_upload(filename=media_path)
        media_id = media.media_id
        text = "💀کاپیتان دولا راست شو .. نماز ظهره " + str(final_time)
        client.create_tweet(text=text, media_ids=[media_id])
        print(f"tweet send >> {text}")


def check_asr_time():
    adhan_asr_time = client_aladhan.get_today_times(
    )[2].readable_timing(show_date=False)[0:5]
    city_timezone = pytz.timezone('Asia/Tehran')
    current_time = datetime.now(timezone.utc)
    tehran_time = current_time.astimezone(city_timezone)
    tehran_str = str(tehran_time)
    final_time = convert_to_24h(adhan_asr_time, is_pm=True)
    if str(final_time) == tehran_str[11:16]:
        auth = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret
        )
        auth.set_access_token(
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        api_v1 = tweepy.API(auth)
        client = tweepy.Client(bearer_token=bearer_token,
                               consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)


        # Upload media and get media_id
        media_path = "capitandola.jpg"
        media = api_v1.media_upload(filename=media_path)
        media_id = media.media_id
        text = "💀کاپیتان دولا راست شو .. نماز عصره " + str(final_time)
        client.create_tweet(text=text, media_ids=[media_id])
        print(f"tweet send >> {text}")


def check_magh_time():
    adhan_magh_time = client_aladhan.get_today_times(
    )[3].readable_timing(show_date=False)[0:5]
    city_timezone = pytz.timezone('Asia/Tehran')
    current_time = datetime.now(timezone.utc)
    tehran_time = current_time.astimezone(city_timezone)
    tehran_str = str(tehran_time)
    final_time = convert_to_24h(adhan_magh_time, is_pm=True)
    if str(final_time) == tehran_str[11:16]:
        auth = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret
        )
        auth.set_access_token(
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        api_v1 = tweepy.API(auth)
        client = tweepy.Client(bearer_token=bearer_token,
                               consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)

        # Upload media and get media_id
        media_path = "capitandola.jpg"
        media = api_v1.media_upload(filename=media_path)
        media_id = media.media_id
        text = "💀کاپیتان دولا راست شو .. نماز مغربه " + str(final_time)
        client.create_tweet(text=text, media_ids=[media_id])
        print(f"tweet send >> {text}")


def check_isha_time():
    adhan_isha_time = client_aladhan.get_today_times(
    )[4].readable_timing(show_date=False)[0:5]
    city_timezone = pytz.timezone('Asia/Tehran')
    current_time = datetime.now(timezone.utc)
    tehran_time = current_time.astimezone(city_timezone)
    tehran_str = str(tehran_time)
    final_time = convert_to_24h(adhan_isha_time, is_pm=True)
    if str(final_time) == tehran_str[11:16]:
        auth = tweepy.OAuth1UserHandler(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret
        )
        auth.set_access_token(
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        api_v1 = tweepy.API(auth)
        client = tweepy.Client(bearer_token=bearer_token,
                               consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)

        # Upload media and get media_id
        media_path = "capitandola.jpg"
        media = api_v1.media_upload(filename=media_path)
        media_id = media.media_id
        text = "💀کاپیتان دولا راست شو .. نماز عشاعهه " + str(final_time)
        client.create_tweet(text=text, media_ids=[media_id])
        print(f"tweet send >> {text}")


if __name__ == "__main__":
    sched = BackgroundScheduler()
    sched.add_job(check_sobh_time, 'interval', seconds=53)
    sched.add_job(check_zohr_time, 'interval', seconds=54)
    sched.add_job(check_asr_time, 'interval', seconds=55)
    sched.add_job(check_magh_time, 'interval', seconds=56)
    sched.add_job(check_isha_time, 'interval', seconds=57)
    sched.start()
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # Gracefully shut down the scheduler
        sched.shutdown()
