#! /usr/bin/python3
# -*- coding: utf-8 -*-

import time

class Search:

    arTimeDate = {}
    nameMouth = {
        "Aug":"08",
        "Sep":"09"
    }

    def __init__(self):
        self.arTimeDate = self.arTimeDate

    def dataTime(self,string):
        if string:
            str = string.replace("[","")
            strExp = str.split(":")
            date = strExp[0]
            date = self.dataDate(strExp[0])
            timeArray = strExp[1:]
            times = ":".join(timeArray)
            attrTime = "{} {}".format(date, times)
            timeUnix = int(time.mktime(time.strptime(attrTime, '%Y-%m-%d %H:%M:%S')))
            self.arTimeDate = {
                "date":date,
                "time":times,
                "time_unix":timeUnix
            }
        return self.arTimeDate

    def dataDate(self,string):
        if string:
            strd = string.split("/")
            return "{}-{}-{}".format(strd[2],self.nameMouth[strd[1]],strd[0])

    def requestHandler(self,string):
        if string:
            return {"REQUEST_HANDLER":string}
