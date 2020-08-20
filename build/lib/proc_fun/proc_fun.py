#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 23:43
# @Version : 1.0
# @File    : proc_fun.py
# @Author  : Jingsheng Tang
# @Version : 1.0
# @Contact : mrtang@nudt.edu.cn   mrtang_cs@163.com
# @License : (C) All Rights Reserved

import win32com.client
import os

def check_exsit(process_name):
    '''
    check if a process is exist
    '''
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:return 1
    else:return 0

def kill_process(process_name):
    '''
    kill a process by name
    '''
    if os.system('taskkill /f /im ' + process_name)==0:return 1
    else:return 0

