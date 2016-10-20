#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-10-20 23:05:24
# @Last Modified by:   anchen
# @Last Modified time: 2016-10-20 23:30:35
import argparse

def get_args():
    parser = argparse.ArgumentParser(
            description="A simple argument parser",
            epilog = "This is where you might put example usage"
        )
   
    #group = parser.add_mutually_exclusive_group()

    #reauire argment
    parser.add_argument('-x','--execute',action="store",required=True,help='Help text for option X')

    #optional arguments
    parser.add_argument('-y',help='Help text for option Y',default=False)
    parser.add_argument('-z',help='Help text for option Z',type=int)  

    print(parser.parse_args())   

if __name__ == '__main__':
    get_args()