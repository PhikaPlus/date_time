import time

# 1: time() -------------------------------------------
# returns the number of seconds passed since epoch.
# epoch in UNIX system: January 1, 1970, 00:00:00
print("Seconds since January 1, 1970 =", time.time())

# 2: ctime() ------------------------------------------
# number of seconds --> understandable time
# تبدیل عدد خام به زمان قابل فهم انسان
seconds = time.time()
local_time = time.ctime(seconds)
print(local_time)   # Wed Feb 13 00:17:09 2019

# 3: sleep() ------------------------------------------
# suspends (delays) execution of code for seconds.
# مکث یا توقف در روند اجرای برنامه
print("time before sleep:", time.ctime(time.time()))
time.sleep(5)       # suspends 5 seconds
print("time after sleep:", time.ctime(time.time()))

# 4: localtime() --------------------------------------
# time structure (struct_time Class)
# خروجی این تابع یک ساختار زمانی است
t1 = time.localtime()
t2 = time.localtime(8979654)
print("local time:    ", t1)
print("unknown time:  ", t2)
print("year:    ", t2.tm_year)      # get year number
print("tm_hour: ", t2.tm_hour)      # get hour number, etc


# time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27,
#                  tm_hour=7, tm_min=49, tm_sec=29,
#                  tm_wday=3, tm_yday=361, tm_isdst=0)

# tm_wday:  day of week, range [0, 6], Monday is 0
# tm_yday:  day of year, range [1, 366]
# tm_isdst: time saving, 0,1 or -1

# 5: UTC (Coordinated Universal Time) or GMT ----------------
# ساعت جهانی یا گرینویچ
result = time.gmtime()
print("result:  ", result)
print("tm_year: ", result.tm_year)
print("tm_hour: ", result.tm_hour)

# 6: make time (the inverse function of localtime()) --------
# time --> seconds
# تبدیل زمان به ثانیه
t = (2018, 12, 28,      # date
     8, 44, 4,          # hour
     4, 362, -1)        # other info
local_time = time.mktime(t)
print("Local time:", local_time)

# 7: localtime() VS mktime() -------------------------------
seconds = 1545925769
t = time.localtime(seconds)

# returns struct_time
print("t1: ", t)

# returns seconds from struct_time
print("s:", time.mktime(t))

# 8: format output time ------------------------------------
time_string = time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime())
print(time_string)

# 9: asctime() ---------------------------------------------
# The strftime() function takes struct_time as an argument and 
# returns a string representing it based on the format code used.
# خروجی قابل فهم و از نوع رشته ای
t = (2018, 12, 28, 
     8, 44, 4, 
     4, 362, 0)

result = time.asctime(t)
print("Result:", result)
print("type:  ", type(result))

# strptime() ------------------------------------------------
# The strptime() function parses a string representing time
# and returns struct_time.

time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")

print(result)
