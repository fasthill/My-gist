#  Unix timestampe 
import datetime, pytz

# 현재 local 시간 표시(년월일시간)를 timestamp 표시로 변환
KST = pytz.timezone('Asia/Seoul')
# timestamp = datetime.datetime(2023, 1, 9, 20, 25, 40, tzinfo=KST).timestamp() #2023년 1월 9일 15시 30분 40초 Local time.
timestamp = datetime.datetime.now(pytz.timezone('Asia/Seoul')).timestamp()

print("timestamp: {}, seoul time: {}".format(timestamp, datetime.datetime.now(pytz.timezone('Asia/Seoul'))))

def datefromtimestamp(timestamp): # timestamp표시를 년월일시간표시로 변환
    date = datetime.datetime.utcfromtimestamp(timestamp) # GMT(UTC) 시간 표시로 변환
#     date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d:%H:%M:%S') # GMT(UTC) 시간 표시로 변환
#     date = datetime.datetime.fromtimestamp(timestamp, tz=pytz.utc).strftime('%Y-%m-%d:%H:%M:%S') # UTC 표준시간
#     date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d:%H:%M:%S') # 로컬 시간 표시로 변환
    return date

def week_day(date):
#     days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    days = ['월', '화', '수', '목', '금', '토', '일']
    day = date.weekday()
    return days[day]

dt = datefromtimestamp(timestamp) # UTC 표준시간. datetime format
print("UTC 표준시간", dt)  

# tzone = pytz.timezone('US/Eastern')
tzone = pytz.timezone('Asia/Seoul')
loc_dt = dt.astimezone(tzone)
print("서울 표준시간", loc_dt)  # UTC 표준시간 형식으로 표현되어 로컬시간(서울)이 24시간으로 표현이 되지 않음.(+9시간으로 표현)

year = dt.year
month = dt.month
weekday = week_day(dt)
day = dt.day
hour = dt.hour
print("UTC: {}년, {}월 {}일 {}요일 {}시".format(year, month, day, weekday, hour))

loc_dt = dt + datetime.timedelta(hours=9) # UTC 와 KST 시간차인 9시간 보상. 24시간을 표시하기 위하여 진행
year = loc_dt.year
month = loc_dt.month
weekday = week_day(loc_dt)
day = loc_dt.day
hour = loc_dt.hour
print("서울 표준시간: {}년, {}월 {}일 {}요일 {}시".format(year, month, day, weekday, hour))

print(loc_dt.astimezone(KST).strftime('%Y-%m-%d, %H:%M:%S %p'))

''' 결과
timestamp: 1673272980.485173, seoul time: 2023-01-09 23:03:00.485173+09:00
UTC 표준시간 2023-01-09 14:03:00.485173
서울 표준시간 2023-01-09 14:03:00.485173+09:00
UTC: 2023년, 1월 9일 월요일 14시
서울 표준시간: 2023년, 1월 9일 월요일 23시
2023-01-09, 23:03:00 PM
'''
