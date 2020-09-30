#! /usr/bin/python3
# -*- coding: utf-8 -*-

class Vars:

    def variable(self,var):
        try:
            datavar = var
        except NameError:
            datavar = None
        
        if datavar != None:
            return 1
        return 0

        