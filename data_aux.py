from datetime import datetime
import re,os,calendar
import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from dotenv import load_dotenv

class DataAux():

    load_dotenv()


    @staticmethod
    def weeks_for_year(month_start,week_start,week_end,year):
        init = week_start
        list_weeks_temp =[]
        if (month_start == 1 and week_start > 4):
            list_weeks_temp.append(str(year-1)+"-W"+str(week_start))
        else:
            list_weeks_temp.append(str(year)+"-W"+str(week_start))
        ended_week = week_end
        for i in range(init,ended_week+1):
            week = str(year)+"-W"+str(i)
            if not week in list_weeks_temp:
                list_weeks_temp.append(week)
        return list_weeks_temp


    def weeks_range(self,date_start,date_end):
        week_start = int(date_start.strftime("%V"))
        month_start = int(date_start.strftime("%m"))
        year_start = int(date_start.strftime("%Y"))
        week_end = int(date_end.strftime("%V"))
        year_end = int(date_end.strftime("%Y"))
        list_weeks = []
        if year_start < year_end:
            year_diference = year_end - year_start
            year_temp = year_start
            lists_weeks = []
            if year_diference > 0:
                for i in range(0,year_diference+1):
                    year_end_temp = datetime(year_temp,12,31)
                    week_end_temp = int(year_end_temp.strftime("%V"))
                    month_start_temp = 1
                    week_start_temp = 1
                    list_weeks_temp =[]
                    if year_temp == year_start:
                        list_weeks_temp = self.weeks_for_year(month_start,week_start,week_end_temp,year_temp)
                    if year_temp == year_end:
                        list_weeks_temp = self.weeks_for_year(month_start,week_start_temp,week_end,year_temp)
                    if (year_temp != year_end and year_temp != year_start):
                        list_weeks_temp = self.weeks_for_year(month_start_temp,week_start_temp,week_end_temp,year_temp)
                    lists_weeks.append(list_weeks_temp)
                    year_temp += 1
                for j in lists_weeks:
                    for k in j:
                        if not k in list_weeks:
                            list_weeks.append(k)
        else:
            list_weeks = self.weeks_for_year(month_start,week_start,week_end,year_start)
        return list_weeks


    def week_range_month(self,now):
        year = now.year
        print(year)
        month = now.month
        print(month)
        start,end = calendar.monthrange(year,month)
        start = 1
        print(f'Inicio {start} - End {end}')
        date_start = datetime(now.year,now.month,start)
        date_end = datetime(now.year,now.month,end)
        week_start = int(date_start.strftime("%V"))
        week_end = int(date_end.strftime("%V"))
        list_weeks = []
        if (now.month == 1 and week_start > 4):
            list_weeks.append(str(int(now.year) - 1)+"-W"+str(week_start))
        for i in range(1,week_end):
            list_weeks.append(str(now.year)+"-W"+str(i))
        return list_weeks


    @staticmethod
    def cipher_pass(text):
        iv =  'BBBBBBBBBBBBBBBB'.encode('utf-8')
        # key = os.getenv('SECRET_PASS')
        key = os.environ.get('SECRET_PASS',os.getenv('SECRET_PASS'))
        data= pad(text.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        cipher= base64.b64encode(cipher.encrypt(data))
        result = cipher.decode("utf-8", "ignore")
        return result


    @staticmethod
    def decipher_pass(text):
        iv =  'BBBBBBBBBBBBBBBB'.encode('utf-8')
        # key = os.getenv('SECRET_PASS')
        key = os.environ.get('SECRET_PASS',os.getenv('SECRET_PASS'))
        enc = base64.b64decode(text)
        decipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        decipher= unpad(decipher.decrypt(enc),16)
        return decipher.decode("utf-8", "ignore")


    def split_date(self,date):
        sp_date = date.split("-")
        return int(sp_date[0]),int(sp_date[1]),int(sp_date[2])


    def validate_date(self,date):
        date = date.strip()
        date = date.replace("/","-")
        date = date.replace(" ","-")
        patron1 = r"[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}"
        patron2 = r"[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}"
        result1 = re.findall(patron1,date)
        result = None
        if len(result1) == 1:
            date_position = {"year":0,"month":1,"day":2}
            result = self.date_format(date,date_position)
        result2 = re.findall(patron2,date)
        if len(result2) == 1:
            date_position = {"year":2,"month":1,"day":0}
            result = self.date_format(date,date_position)
        return result


    @staticmethod
    def date_format(date,dict_positions):
        date_split = date.split("-")
        year = date_split[dict_positions['year']]
        month = date_split[dict_positions['month']]
        day = date_split[dict_positions['day']]
        result = None
        if (year.isdigit() and month.isdigit() and day.isdigit()):
            if (int(month) <= 12 and int(day) <= 31):
                result = str(year)+"-"+str(month)+"-"+str(day)
        return result
        

    @staticmethod
    def validate_result(result,text):
        if len(result) > 0 and result[0] == text:
            result = text
        else:
            result = None
        return result
    

    def validate_text(self,text):
        patron = r"[A-Za-z]*[A-Za-z-_*+@.0-9]*"
        result = re.findall(patron,text)
        if len(text) == 0:
            result = []
        return self.validate_result(result,text)
        
    
    def validate_number(self,text):
        patron = r"[0-9]*"
        result = re.findall(patron,text)
        return self.validate_result(result,text)
        
    
    def validate_week(self,text):
        patron = r"[0-9]{4}-W[0-9]{1,2}"
        result = re.findall(patron,text)
        return self.validate_result(result,text)


    def validate_params(self,request_data,dict_params):
        dict_types = {
            "text":self.validate_text,
            "number":self.validate_number,
            "week":self.validate_week,
            "date":self.validate_date}
        errors_types = {
            "text":"No debe estar vacio y Debe comenzar con una letra y solo puede contener los siguientes caracteres numeros o -_*+@.",
            "number":"Debe ser un valor numerico",
            "week":"debe tener el siguiente formato [YYYY-W(numerico 1 o 2)] ejemplo 2020-W7",
            "date":"puede tener los siguientes formatos [YYYY-MM|M-DD|D] 2020-2-3 o 2020-02-03 [YYYY MM|M DD|D] 2020 02 03 o 2020 2 3 [YYYY/MM|M/DD|D] 2020/02/03 o 2020/2/3 [MM|M-DD|D-YYYY] 3-2-2020 o 03-02-2020 [MM|M DD|D YYYY] 03 02 2020 o 3 2 2020 [MM|M/DD|D/YYYY] 03/02/2020 o 3/2/2020"}
        list_results = {}
        errors = []
        for k,v in dict_params.items():
            result = dict_types[v](request_data[k])
            list_results[k] = result
            if result == None:
                errors.append("El parametro "+str(k)+" "+str(errors_types[v]))
        return list_results,errors







