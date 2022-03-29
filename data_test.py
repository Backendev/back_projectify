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
date_start = datetime(2021,1,1)
date_end = datetime(2021,1,13)
# week_start = int(date_start.strftime("%V"))
da = DataAux()
list_r = da.weeks_range(date_start,date_end)
print(f'list_r {list_r}')

# d.new_report("2","aplication analisys","2024-W3","90")
# d.get_reports()
# d.new_project("2021-2-15","2022-3-15","test2")
date = da.validate_date("13-2-2021")
date = da.validate_date("2021-3-31")
print(date)
text = "f_@@@ghyu"
text = da.validate_text(text)
print(text)
text_number = "222"
text_week = "2022-W8"
number = da.validate_number(text_number)
week = da.validate_week(text_week)
print(f'Number {number} - Week {week}')
text_number = "22aa2"
text_week = "2022-Wd8"
number = da.validate_number(text_number)
week = da.validate_week(text_week)
print(f'Number {number} - Week {week}')

dict_result = {"name":"ed","year":"3","week":"2020-W7"}
list_params = {"name":"text","year":"number","week":"week"}
res,errors = da.validate_params(dict_result,list_params)
print(res)
print(errors)
dict_result = {"name":"","year":"as","week":"2020-hg"}
res,errors = da.validate_params(dict_result,list_params)
print(res)
print(errors)

user = d.get_user_id("1")
print(f"User {user}")
text = "1223"
cipher = da.cipher_pass(text)
# print(cipher)
print(f'Cipher {cipher}')
cipher = da.decipher_pass(cipher)
print(f'DesCipher {cipher}')
# date_start = datetime(2020,1,1)
# week_start = int(date_start.strftime("%V"))
# print(week_start)

date = datetime(2020,1,1)
week_start = int(date.strftime("%V"))
print(f"Date - {str(week_start)}")

res = da.week_range_month(date)
print(f"Lista weeks month {str(res)}")





