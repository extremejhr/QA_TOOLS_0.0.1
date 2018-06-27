# -*- coding: utf-8 -*-
"""
Spyder Editor
####################################################################

Siemens QA Tools Shortcut
 
####################################################################
This is a temporary script file.
"""
###################################################################
#
# Imported Packages
#
###################################################################

import sys, getopt
import os
import pywinauto
import win32gui
import numpy as np
import configparser
import re
####################################################################

# Configuration Class

####################################################################

class Configuration(object):

    config_file_name='Config.ini'
    
    def __init__(self):
    
        cfg = configparser.ConfigParser()
        cfg.read(self.config_file_name)    
          
        self.DT_PATH = cfg.get('ENVIRONMENT VARIABLE','DT_PATH')
        self.D_BATCH_PATH = cfg.get('ENVIRONMENT VARIABLE','UDISTRIB_BATCH_PATH')
        self.U_BATCH_PATH = cfg.get('ENVIRONMENT VARIABLE','UNIT_BATCH_PATH')
        self.NX_PATH = cfg.get('ENVIRONMENT VARIABLE','NX_PATH')
        self.UNIT_PATH = cfg.get('ENVIRONMENT VARIABLE','UNIT_PATH')
        self.LOG_CHECK = cfg.getint('HISTORY','LOG_CHECK')
        self.PLATFORMS = cfg.get('BUILD OPTIONS','PLATFORMS')
        self.POPULATE_OPTIONS = cfg.get('BUILD OPTIONS','POPULATE_OPTIONS')
        self.UNIT_OPTIONS = cfg.get('BUILD OPTIONS','UNIT_OPTIONS')
        self.AUTO_UPDATE = cfg.get('UPDATE','AUTO_UPDATE')
        
        
###################################################################

# Unit Generator

###################################################################
            
class UnitGenerator(Configuration):
     
     def __init__(self, UNIT_PATH_A, NX_PATH_A):
         Configuration.__init__(self)
         self.UNIT_PATH_A = UNIT_PATH_A
         self.NX_PATH_A = NX_PATH_A
         
     def U_Add(self):        
         
         if ('Analysis' in self.NX_PATH_A) == True:
             folder_name='group_build\\'
             print(self.NX_PATH+folder_name+self.NX_PATH_A+'\\init.def')
             self.init_file = open(self.NX_PATH+folder_name+self.NX_PATH_A+'\\init.def','r').readlines()
             print(self.init_file[11])
             if self.init_file[11] =='    PREV_ROOT\n':
                 self.init_file[11]=self.init_file[11].replace('PREV_ROOT','PREV_ROOT '+self.NX_PATH+'ip_build\\'+self.init_file[4][24:])
                 print(self.init_file[11])
                 open(self.NX_PATH+folder_name+self.NX_PATH_A+'\\init.def','w').writelines(self.init_file)
         else:
             folder_name='ip_build\\'
             
         self.command_line = self.DT_PATH+self.U_BATCH_PATH+' add'+' -u -p '+self.NX_PATH+folder_name+self.NX_PATH_A+' '+ self.UNIT_OPTIONS+' '+self.UNIT_PATH+self.UNIT_PATH_A
         
         os.system(self.command_line)
         print("Unit Generated Successfully!")
     
     def U_Delete(self):
        self.command_line = self.DT_PATH+self.U_BATCH_PATH+' delete '+self.UNIT_PATH+self.UNIT_PATH_A
        os.system(self.command_line)
        print(self.UNIT_PATH+self.UNIT_PATH_A)
        
     def U_Start(self):
        self.command_line = self.command_line = self.DT_PATH+self.U_BATCH_PATH+' set '+self.UNIT_PATH+self.UNIT_PATH_A
        os.system(self.command_line)
        print("Unit Started Successfully!")
        
     def U_List(self):
        for root, dirs, files in os.walk(self.UNIT_PATH, topdown = True):
            for name in dirs:
                print(name)
            break

              
###################################################################

# Distribution Class

###################################################################        

class Distributor(Configuration):
    
    def __init__(self,version, cover_path, cover_flag):
       
        Configuration.__init__(self)
             
        self.Cover_Flag = cover_flag
        self.Version0 = version
        self.Version_old = version       
        
        if self.Cover_Flag == 1:
            self.Version = cover_path
        else:
            self.Version = version
               
        if 'Analysis'in self.Version:
            self.NX_PATH1 = self.NX_PATH+'group_build\\'+self.Version
            self.NX_PATH2 = self.NX_PATH+'group_build\\'+self.Version_old
        else:
            self.NX_PATH1 = self.NX_PATH+'ip_build\\'+self.Version
            self.NX_PATH2 = self.NX_PATH+'ip_build\\'+self.Version_old
                   
        self.Command_Line=self.DT_PATH+self.D_BATCH_PATH+' -v'+' "@'+version+'"'+' -p "'+self.PLATFORMS+'" '+self.POPULATE_OPTIONS+' "'+self.NX_PATH1+'"'
              
    def udistrib(self):
        os.system(self.Command_Line)
        print("Distribution has finished!")
        
        if self.Cover_Flag == 1:
            os.rename(self.NX_PATH1,self.NX_PATH2)
            
#########################################################################
#
# E-Mail Automation Check & Distribution
#            
##########################################################################
  