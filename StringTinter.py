# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:13:49 2021

@author: scaparas
"""
#A simple script for tinting the print output
#Useful for helping with legibility

#ANSI escape code colors
class bcolors:
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

#tint colors a String inserted. It is more readable and can be autocompleted with Shift+Space.
def tint(string_to_insert, color):
    tinted_string = f"{color}{string_to_insert}{bcolors.ENDC}".format(
            color = color, string_to_insert = string_to_insert)
    return tinted_string