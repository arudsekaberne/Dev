import pytz
from datetime import datetime


# 1. Find local datetime timezone
cur_datetime = datetime.today()
ext_datetime = cur_datetime.astimezone()
ext_timezone = ext_datetime.tzinfo

print("Current Datetime: {}".format(cur_datetime))
print("Extended Datetime: {}".format(ext_datetime))
print("Timezone: {}".format(ext_timezone))

# 2. Convert datetime to another timezone

ist_timezone = pytz.timezone("Asia/Calcutta")
pst_timezone = pytz.timezone("America/Los_Angeles")

ist_datetime = ist_timezone.localize(cur_datetime)
pst_datetime = ist_datetime.astimezone(pst_timezone)

print("IST Date Time: {}".format(ist_datetime))
print("PST Date Time: {}".format(pst_datetime))