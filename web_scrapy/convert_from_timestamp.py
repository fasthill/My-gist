#  Unix timestampe 
import datetime

# 현재 local 시간 표시(년월일시간)를 timestamp 표시로 변환
timestamp = datetime.datetime(2023, 1, 9, 15, 30, 40).timestamp() #2023년 1월 9일 15시 30분 40초 Local time.

def datefromtimestamp(timestamp): # timestamp표시를 년월일시간표시로 변환
  date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d:%H:%M:%S') # GMT(UTC) 시간 표시로 변환
  # date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d:%H:%M:%S') # 로컬 시간 표시로 변환
  return date

print(datefromtimestamp(timestamp))  
# 2023-01-09:06:30:40  #: UTC로 변환되어 표시됨. 9시간 차이
