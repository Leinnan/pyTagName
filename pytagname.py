#!/usr/bin/python2

#-*- coding: utf-8 -*-
import tagpy
import glob
import os
import sys
import re


def setNameToFileByTag(file_path, music_format):
    file_with_tags = tagpy.FileRef(file_path)
    track_nr = ""
    if file_with_tags.tag().track < 10:
        track_nr = "0"
    track_nr += str(file_with_tags.tag().track)
    track_title = file_with_tags.tag().title
    track_artist = file_with_tags.tag().artist
    new_file_name =  track_nr + "." + track_artist + "- " + track_title + "." + music_format
    # remove forbidden chars
    new_file_name = re.sub(r'[>|<|\|/|:|*|||?|$|!]',r'',new_file_name)
    try:    
        os.rename(file_path, new_file_name)
        print file_path
        if not file_path in new_file_name:
            print "\033[32m Succesfull change to: " + new_file_name + "\033[0m"
    except OSError:
        print '\033[31mSomething, something was broken with: \033[0m' + file_path


# start of program
Debug = False

# fixing problems with encoding
reload(sys)
sys.setdefaultencoding('utf-8')

# get the folder with music and music format
if Debug:
    music_root_dir = "/media/wszystko/ZZZZZZZZ/"
    music_format = "mp3"
else:
    music_root_dir = raw_input('Path to folder with music: ')
    music_format = raw_input('Music format: ')
    if music_root_dir[-1] != "/":
        music_root_dir += "/"
        

# get the list of folders in our root directory
folders = glob.glob(music_root_dir + "*/")

# looking for files in subfolders
for folder in folders:
    os.chdir(folder)
    # get list of mp3 files in folder
    music_files = glob.glob("*" + music_format)
    for music_file in music_files:
        setNameToFileByTag(music_file, music_format)
        
# looking for files in root directory
os.chdir(music_root_dir)
music_files = glob.glob("*" + music_format)    
for music_file in music_files:
    setNameToFileByTag(music_file, music_format)
