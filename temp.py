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

####################################################################

# Configuration Class

####################################################################

class Configuration(object):

    config_file_name='Config.ini'
    
    def __init__(self):
    
        cfg = configparser.ConfigParser()
        cfg.read(self.config_file_name)    
          
        self.DT_PATH = cfg.get('ENVIRONMENT VARIABLE','DT_PATH')
        self.NX_PATH = cfg.get('ENVIRONMENT VARIABLE','NX_PATH')
        self.UNIT_PATH = cfg.get('ENVIRONMENT VARIABLE','UNIT_PATH')
        self.LOG_CHECK = cfg.getint('HISTORY','LOG_CHECK')
        self.IP_PLATFORMS = cfg.get('BUILD OPTIONS','IP_PLATFORMS')
        self.GROUP_PLATFORMS = cfg.get('BUILD OPTIONS','GROUP_PLATFORMS')
        self.POPULATE_OPTIONS = cfg.get('BUILD OPTIONS','POPULATE_OPTIONS')
        self.UNIT_OPTIONS = cfg.get('BUILD OPTIONS','UNIT_OPTIONS')
        self. MODULE = cfg.get('BUILD OPTIONS','MODULE')
    
###################################################################

# Distribution Class

###################################################################        

class Distribution(Configuration):
    
    def __init__(self):
        Configuration.__init__(self)
        self.Version=input('The Distribution Version: ')
    
 
#    def udistrib(self,PF):
        
    
    
    
###################################################################


'''
if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "DUCAPG")
    np.opt=opts
    print('-D')
'''


##################################################################




