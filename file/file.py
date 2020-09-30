#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
from file.search import Search
from file.debug import Debug
from file.vars import Vars

class Files(Search,Debug):

    # fileExtension = "_log"
    name = ""
    fileСontents = []
    resultCode = {}
    fileNum = 0;
    conf = {}
    objVars = Vars()
    # codeError [" 500 "," 503 "]

    def __init__(self,config):
        self.config = config

    def __getattr__(self, attr):
        self.attr = self.config[attr]
        self.conf[attr] = self.attr
        return self.attr

    def tpath(self):
        return os.getcwd();

    def file(self):
        files = self.listFiles();
        ita = -1
        for fl in files:
            if self.fileExtension !="":
                flsplit = fl.split(self.fileExtension)
            else:
                flsplit = fl
            if len(flsplit) > 1:
                ita +=1
                if self.fileNum == ita:
                    self.nameFile(flsplit[ita])
                
        return self.name
        
    def nameFile(self,name):
        self.name = name
        return self.name;

    def listFiles(self):
        return os.listdir();

    def exists(self,file):
        return os.path.exists(file)

    def openFile(self,ret="rt"):
        dataFile = []
        file = "{}/{}{}".format(self.tpath(),self.name,self.fileExtension)
        if self.exists(file) == True:
            with open(file,ret) as fred:
                dataFile = fred.read()
        return dataFile;

    def iterFile(self,ret="rt"):
        self.file()
        file = "{}/{}{}".format(self.tpath(),self.name,self.fileExtension)
        if self.exists(file) == True:
            with open(file,ret) as fred:
                for file_line in fred:
                    self.fileСontents.append(file_line)
        return self.fileСontents

    def listDataString(self,string):
        return string.split(" ")

    def search(self):
        self.iterFile()
        numberCodeStatus = ""

        if type(self.fileСontents) == list and len(self.fileСontents) > 0:
            iter = -1
            for string in self.fileСontents:
                stringList = self.listDataString(string)
                arDateTime = self.dataTime(stringList[3])
                requestHandler = self.requestHandler(stringList[6])
                for code in self.codeError:
                    numberCode = string.find(code)
                    if numberCode > 0: 
                        iter +=1
                        numberCodeStatus = numberCode
                        # self.dateResult = self.dataDate(self.date)
                        # print(arDateTime["date"])
                        # print(self.dateResult)

                        self.resultCode[iter] = {
                                "LIST":stringList,
                                "CODE": numberCodeStatus,
                                "DATE":arDateTime,
                                "REQUEST_HANDLER":requestHandler["REQUEST_HANDLER"],
                                "URL":stringList[10],
                                "METHOD":stringList[5].replace('"','')
                                }
        self.search_filter()
        return self.resultCode

    def search_filter(self):
        self.arResultCode = {}
        action = 0
        try:
            date = self.dataDate(self.date)
            print(date)
        except KeyError:
            date = ""
        try:
            time = self.time
        except KeyError:
            time = ""
        
        if date and time:
            action = 2
        elif date and time == "":
            action = 1

        lenResultCode = len(self.resultCode)
        if action == 1:
            if lenResultCode > 0:
                for code in self.resultCode:
                    if self.resultCode[code]["DATE"]["date"] == date:
                        self.arResultCode[code] = self.resultCode[code]
        elif action == 2:
            if lenResultCode > 0:
                for code in self.resultCode:
                    string = self.resultCode[code]["DATE"]["time"]
                    time_search =  string.find(time)
                    if self.resultCode[code]["DATE"]["date"] == date and time_search >= 0:
                        self.arResultCode[code] = self.resultCode[code]
        else:
            self.arResultCode = self.resultCode
        self.arResultCode
        self.resultCode = [] 
        self.resultCode = self.arResultCode
        self.arResultCode = []
        return self.resultCode

if __name__ == "__main__":
    OF = Files([" 500 "," 503 "]);
    Se = OF.search()
    print(Se)