#! /usr/bin/python3
# -*- coding: utf-8 -*-
from file.debug import Debug
import csv
import os
import os.path

class Imfile(Debug):

    headers = []
    rows = []
    up = "up"
    upfile = "file"
    namefilecsc = "log_result.csv"
    slov = []

    def __init__(self,kwargs):
        # print(kwargs)
        # print(type(kwargs))
        # self.headers = Imfile.headers
        # if type(kwargs) == dict:
        #     for array in kwargs:
        #         data = kwargs[array]
        #         dataKey = list(data.keys())
        #         if array == 0:
        #             self.headerFile(dataKey) 
        #         self.rowsFile(data) 
        # print(self.rows)
        self.app(kwargs)
        # print(os.path.basename(self.up))
        # print(" as ",os.path.dirname(self.pathFile()))
        # print(self.pathFile())
        self.csv()

    def app(self,kwargs):
        if type(kwargs) == dict:
            for array in kwargs:
                data = kwargs[array]
                if array == 0:
                    dataKey = list(data.keys())
                    self.headerFile(dataKey) 
                self.rows.append(self.rowsFile(data))
        return self.rows 

    def headerFile(self,arraylist):
        if type(arraylist) == list and len(arraylist) > 0:
            self.headers = arraylist
        return self.headers

    # def rowsFile(self,dataRows):
    #     if type(dataRows) == dict and len(dataRows) > 0:
    #         slov = {}
    #         for row in dataRows:
    #             self.debug(row)
    #             slov = {
    #                row: dataRows[row]
    #             }
    #             self.debug(slov)
    #             self.rows.append(slov)
    #     return self.rows

    def rowsFile(self,dataRows):
        if type(dataRows) == dict and len(dataRows) > 0:
            
            corted = []
            # print(dataRows)
            # self.debug(dataRows)
            for row in dataRows:
                corted.append(dataRows[row])
        return tuple(corted)


    def pathFile(self):
        return os.getcwd();

    def listFiles(self):
        return os.listdir();

    def upfiles(self):
        # pathUp = os.path.join(os.path.dirname(self.pathFile()),self.up)
        UF = "{}/{}".format(self.up,self.upfile)
        return os.path.join(self.pathFile(),UF)

    def csv(self):
        filecsv = "{}/{}".format(self.upfiles(),self.namefilecsc)
        # print(self.headers)
        # print(self.rows)
        try:
            with open(filecsv,"w+") as file_csv:
                f_csv = csv.writer(file_csv)
                f_csv.writerow(self.headers)
                f_csv.writerows(self.rows)
                # f_csv = csv.DictWriter(file_csv,self.headers)
                # f_csv.writeheader()
                # f_csv.writerows(self.rows)
        except FileNotFoundError:
            file = open(filecsv, "w+")
            file.close()
        return True
        