#! /usr/bin/python3
# -*- coding: utf-8 -*-

from file.file import Files
from file.debug import Debug
from file.imfile import Imfile

class Main(Files,Imfile):

    config = {
        "codeError":[" 500 "," 503 "],
        "fileExtension":"_log",
        # "date":"21/Sep/2020",
        # "time":"05:27"
    }

    def __init__(self):
        self.conf = Main.config
        super().__init__(self.conf)
 

    def sech(self):
        se = self.search()
        # self.debugN(se)
        objImfile = Imfile(se)
        # arAttr = se.keys()
        # print(arAttr)
        # for sl in se:
        #     arAttr = list(se[sl].keys())
        #     print(arAttr)
            
        #     print(se[sl]["URL"])
        #     self.de_sech(se[sl])      

    def de_sech(self,func):
        for fun in func:
            self.debugN(func[fun])


if __name__ == "__main__":
    # OF = Main([" 500 "," 503 "],".txt");
    OF = Main();
    OF.sech()