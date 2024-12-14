#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:56:22 2024

@author: ykinisha
"""
import os

def read_file(file_name):
    cwd = os.getcwd()
    source = os.path.join(cwd, file_name)
    with open(source) as file:
        data = file.readlines()
    
    return data