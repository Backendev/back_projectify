import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
from g_token import TokenGen
import os
from data import Data
from datetime import datetime
load_dotenv()

# d = Data()
# gt = TokenGen()
# print(f'resultUs = {d.get_user(user=u"Adan")}')
# print(f'resultPass = {d.get_user(user=u"Adan",passd="1234")}')
# print(f'resultId = {d.get_user(user=u"Adani",idu="2")}')
# print(f'result = {d.new_user(u"Adanisos",u"1234")}')
# gt.change_secret()
# message = {"Adanis":"1234"}
# print(f'result Token = {gt.gen_token(message)}')
# print(f'result Token = {gt.get_token()}')
# print(f'result Token Des= {gt.get_desc_token(gt.get_token())}')
date_cust = datetime(2022,1,1)
date_now = datetime.now()
print(date_now.strftime("%Y-W%V-%w"))
week = int(date_cust.strftime("%V"))
day = int(date_cust.strftime("%w"))
month = int(date_cust.strftime("%m"))
year = int(date_cust.strftime("%Y"))
print(f"Day {day} - Month {month} - year {year} - Week {week}")
if (month == 1 and week > 1):
    year = year - 1
print(f"Day {day} - Month {month} - year {year} - Week {week}")
if day == 0:
    day = 7
print(date_cust)
print(date_cust.strftime("%Y-W%V-"+str(day)))
date_start = datetime(2020,1,1)
date_end = datetime(2020,2,17)
week_start = int(date_start.strftime("%V"))
month_start = int(date_start.strftime("%m"))
year_start = int(date_start.strftime("%Y"))
week_end = int(date_end.strftime("%V"))
month_end = int(date_end.strftime("%m"))
year_end = int(date_end.strftime("%Y"))
list_weeks = []
diference_weeks = 0
if year_start < year_end:
    year_diference = year_end - year_start
    year_temp = year_start
    print(f"Diferencia años {year_diference}")
    if year_diference > 0:
        for i in range(0,year_diference+1):
            print(i)
            print(year_temp)
            if year_temp == year_start:
                print(f'Inicio {year_temp}')

            if year_temp == year_end:
                print(f'Fin {year_end}')
            year_temp += 1
else:
    print(f'Inicio 2 {year_start}')
    init = 1
    if (month_start == 1 and week_start > 4):
        list_weeks.append(str(year_start-1)+"-W"+str(week_start))
    else:
        list_weeks.append(str(year_start)+"-W"+str(week_start))
        init = 2
    ended_week = week_end
    for i in range(init,ended_week+1):
        print(i)
        list_weeks.append(str(year_start)+"-W"+str(i))
    print(list_weeks)



