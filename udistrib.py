# -*- coding: utf-8 -*-
"""
Spyder Editor
####################################################################

Siemens QA Tools Shortcut
 
####################################################################
This is a temporary script file.
"""
import library as lib
import sys, getopt
            
if __name__ == "__main__":
    
    value=''
    cover_path=''
    auto_flag=0
    cover_flag=0
    unit_flag = 0
    opts, args = getopt.getopt(sys.argv[1:], "v:uc:d", ["check"])
    
    if len(opts)<5 and len(opts)>0:
        for opt, value in opts:
            if opt =='-v':
                version = value
            elif opt=='-u':
                unit_flag = 1
            elif opt=='-c':
                cover_path = value
                cover_flag = 1
            elif opt=='-d':
                delete_u_flag = 1
  #          elif opt == '--check':
                
            else:
                print('\nWrong Options!\n')
                sys.exit()
    else:
        print('\nWrong Options!\n')
        sys.exit()    
    
    udistrib=lib.Distributor(version, cover_path, cover_flag)
    udistrib.udistrib() 
    
    if delete_u_flag == 1 and cover_flag == 1 and cover_path != version:
        Unit_D = lib.UnitGenerator(udistrib.Version,'')
        Unit_D.U_Delete()
    
    if unit_flag ==1 and cover_path != version:
        Unit_A = lib.UnitGenerator(udistrib.Version_old, udistrib.Version_old)
        Unit_A.U_Add()
        
        
    
 #re.findall(r"\d+\.?\d*",cover_path) >= re.findall(r"\d+\.?\d*",version)
    
    
    
        




##################################################################




