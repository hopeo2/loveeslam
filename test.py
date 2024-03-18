import aladhan
import pytz
from datetime import datetime, timezone


location = aladhan.City("Tehran", "IR")
client_aladhan = aladhan.Client(location)

adhans = client_aladhan.get_today_times()

adhan_sobh_time = client_aladhan.get_today_times()[0].readable_timing(show_date=False)[0:5]
adhan_what_time = client_aladhan.get_today_times()[2].readable_timing(show_date=False)[0:5]
adhan_sobh_timee = adhans[2].get_en_name()

city_timezone = pytz.timezone('Asia/Tehran')
current_time = datetime.now(timezone.utc)
tehran_time = current_time.astimezone(city_timezone)
tehran_str = str(tehran_time)

print(tehran_str, tehran_str[11:16])

print(tehran_str[11:16] == adhan_sobh_time)


def convert_to_24h(time_str, is_pm=False):
    hours, minutes = time_str.split(':')
    hours = int(hours)
    # If it's PM and not 12 PM, add 12 to the hours
    if is_pm and hours != 12:
        hours += 12
    # Format hours back to two digits
    hours = f"{hours:02d}"
    return f"{hours}:{minutes}"


final_time = convert_to_24h(adhan_what_time, is_pm=True)
print(adhan_what_time, adhan_sobh_timee, final_time)

