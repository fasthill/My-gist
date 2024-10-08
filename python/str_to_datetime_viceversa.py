import datetime

datetime_str = '09/19/22 13:55:26'
datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

'''
datetime_object
datetime.datetime(2022, 9, 19, 13, 55, 26)
'''

date_str = '09-19-2022'
date_object = datetime.datetime.strptime(date_str, '%m-%d-%Y').date()

'''
date_object
datetime.date(2022, 9, 19)
'''

time_str = '13::55::26'
time_object = datetime.datetime.strptime(time_str, '%H::%M::%S').time()

'''
time_object
datetime.time(13, 55, 26)
'''

# dataframe datetime 으로 전환
MATCHING_DAYS['date_all'] =  pd.to_datetime(MATCHING_DAYS['date_all'],format='%Y-%m-%d').dt.date


# from https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime

datetime_object = datetime.datetime(2022, 1, 5)
date_time = datetime_object.strftime("%m/%d/%Y, %H:%M:%S")  # datetime to string
print("date and time:",date_time)
