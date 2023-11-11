from datetime import datetime


# 1. Find local datetime timezone
cur_datetime = datetime.today()
ext_datetime = cur_datetime.astimezone()
ext_timezone = ext_datetime.tzinfo

print("Current Datetime: {}".format(cur_datetime))
print("Extended Datetime: {}".format(ext_datetime))
print("Timezone: {}".format(ext_timezone))
