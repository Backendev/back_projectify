from datetime import datetime


class DataAux():
    @staticmethod
    def weeks_for_year(month_start,week_start,week_end,year):
        init = 1
        list_weeks_temp =[]
        if (month_start == 1 and week_start > 4):
            list_weeks_temp.append(str(year-1)+"-W"+str(week_start))
        else:
            list_weeks_temp.append(str(year)+"-W"+str(week_start))
            init = 2
        ended_week = week_end
        for i in range(init,ended_week+1):
            list_weeks_temp.append(str(year)+"-W"+str(i))
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
            print(f"Diferencia años {year_diference}")
            lists_weeks = []
            if year_diference > 0:
                for i in range(0,year_diference+1):
                    print(i)
                    print(year_temp)
                    if year_temp == year_start:
                        list_weeks_temp =[]
                        year_end_temp = datetime(year_temp,12,31)
                        week_end_temp = int(year_end_temp.strftime("%V"))
                        list_weeks_temp = self.weeks_for_year(month_start,week_start,week_end_temp,year_temp)
                        lists_weeks.append(list_weeks_temp)
                    if year_temp == year_end:
                        list_weeks_temp =[]
                        year_start_temp = datetime(year_temp,1,1)
                        week_start_temp = int(year_start_temp.strftime("%V"))
                        list_weeks_temp = self.weeks_for_year(month_start,week_start_temp,week_end,year_temp)
                        lists_weeks.append(list_weeks_temp)
                    if (year_temp != year_end and year_temp != year_start):
                        list_weeks_temp =[]
                        year_start_temp = datetime(year_temp,1,1)
                        week_start_temp = int(year_start_temp.strftime("%V"))
                        month_start_temp = int(year_start_temp.strftime("%m"))
                        year_end_temp = datetime(year_temp,12,31)
                        week_end_temp = int(year_end_temp.strftime("%V"))
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