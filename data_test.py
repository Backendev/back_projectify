import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
from g_token import TokenGen
import os
from data import Data
from datetime import datetime
from data_aux import DataAux
load_dotenv()
# def weeks_for_year(month_start,week_start,week_end,year):
#     init = 1
#     list_weeks_temp =[]
#     if (month_start == 1 and week_start > 4):
#         list_weeks_temp.append(str(year-1)+"-W"+str(week_start))
#     else:
#         list_weeks_temp.append(str(year)+"-W"+str(week_start))
#         init = 2
#     ended_week = week_end
#     for i in range(init,ended_week+1):
#         list_weeks_temp.append(str(year)+"-W"+str(i))
#     # print(f"List Week TTT {list_weeks_temp}")
#     return list_weeks_temp



d = Data()
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

# date_cust = datetime(2022,1,1)
# date_now = datetime.now()
# print(date_now.strftime("%Y-W%V-%w"))
# week = int(date_cust.strftime("%V"))
# day = int(date_cust.strftime("%w"))
# month = int(date_cust.strftime("%m"))
# year = int(date_cust.strftime("%Y"))
# print(f"Day {day} - Month {month} - year {year} - Week {week}")
# if (month == 1 and week > 1):
#     year = year - 1
# print(f"Day {day} - Month {month} - year {year} - Week {week}")
# if day == 0:
#     day = 7
# print(date_cust)
# print(date_cust.strftime("%Y-W%V-"+str(day)))
# date_start = datetime(2021,1,1)
# date_end = datetime(2023,2,13)
# week_start = int(date_start.strftime("%V"))
# da = DataAux()
# list_r = da.weeks_range(date_start,date_end)
# print(list_r)

d.new_report("2","aplication analisys","2024-W3","90")




