# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:21:53 2018

@author: xqk9qq
"""

import library as lib
import sys, getopt

if __name__ == "__main__":
    
    value=''
    cover_path=''
    auto_flag=0
    cover_flag=0
    unit_flag = 0
    opts, args = getopt.getopt(sys.argv[1:], "a:d:s:", ["list"])
    
    if len(opts)<2 and len(opts)>0:
        
        for opt, value in opts:
            if opt =='-a':
                Unit_D = lib.UnitGenerator(value,value)
                Unit_D.U_Add()
            elif opt=='-d':
                Unit_D = lib.UnitGenerator(value,'')
                Unit_D.U_Delete()
            elif opt=='-s':
                Unit_D = lib.UnitGenerator(value,'')
                Unit_D.U_Start()
            elif opt=='--list':
                Unit_D = lib.UnitGenerator(value,'')
                Unit_D.U_List()               
            else:
                print('\nWrong Options!\n')
                sys.exit()
    else:
        print('\nWrong Options!\n')
        sys.exit()    
       

