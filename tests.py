import unittest
from data import Data
from datetime import datetime
from data_aux import DataAux
from g_token import TokenGen

class Testing(unittest.TestCase):    
        
    def testCipherDecipherToken(self):
        message = {"Adanis":"1234"}
        gt = TokenGen()
        gt.gen_token(message)
        token = gt.get_token()
        result = gt.get_desc_token(gt.get_token())
        assert(message == result)
    
    def testListWeeks(self):
        da = DataAux()
        date_start = datetime(2021,1,1)
        date_end = datetime(2021,1,13)
        res = ['2020-W53', '2021-W1', '2021-W2']
        list_r = da.weeks_range(date_start,date_end)
        assert(res == list_r)
    
    def testFormatDate(self):
        da = DataAux()
        date1 = da.validate_date("3-2-2021")
        date2 = da.validate_date("2021-2-3")
        date3 = da.validate_date("3/2/2021")
        date4 = da.validate_date("3 2 2021")
        result = "2021-2-3"
        assert(result == date1)
        assert(result == date2)
        assert(result == date3)
        assert(result == date4)

    def testValidateText(self):
        da = DataAux()
        text = "f_@@@ghyu"
        text_validate = da.validate_text(text)
        text2 = "f_@@@ghyu´}"
        text_validate2 = da.validate_text(text2)
        assert(text == text_validate)
        assert(text_validate2 == None)
    
    def testValidateNumber(self):
        da = DataAux()
        number = "34567"
        number_validate = da.validate_number(number)
        number2 = "f34s56"
        number_validate2 = da.validate_number(number2)
        assert(number == number_validate)
        assert(number_validate2 == None)

    def testValidateWeek(self):
        da = DataAux()
        week = "2022-W8"
        week_validate = da.validate_week(week)
        week2 = "2022 w3"
        week_validate2 = da.validate_week(week2)
        assert(week == week_validate)
        assert(week_validate2 == None)

    def testParamsValidate(self):
        da = DataAux()
        dict_result = {"name":"ed","year":"3","week":"2020-W7"}
        dict_result2 = {"name":"ed","year":"a","week":"2020 W7"}
        list_params = {"name":"text","year":"number","week":"week"}
        res,errors = da.validate_params(dict_result,list_params)
        res,errors2 = da.validate_params(dict_result2,list_params)
        assert(len(errors) == 0)
        assert(len(errors2) == 2)
    
    def testCipherDecipherText(self):
        da = DataAux()
        text = "1223"
        cipher = da.cipher_pass(text)
        decipher = da.decipher_pass(cipher)
        assert(text == decipher)

    def testWeekRangeMonth(self):
        da = DataAux()
        date = datetime(2020,1,1)
        weeks = ['2020-W1', '2020-W2', '2020-W3', '2020-W4']
        result = da.week_range_month(date)
        assert(weeks == result)

