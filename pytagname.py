#!/usr/bin/python2

#-*- coding: utf-8 -*-
import tagpy
import glob
import os

Debug = True

def setNameToFileByTag(file_path, music_format):
    # print file_path
    file_with_tags = tagpy.FileRef(file_path)
    track_nr =  str(file_with_tags.tag().track)
    track_title = file_with_tags.tag().title
    track_artist = file_with_tags.tag().artist
    new_file_name =  track_nr + "." + track_artist + "- " + track_title + "." + music_format
    # print os.path.exists(file_path)
    # print os.path.exists(new_file_name)
    try:    
        os.rename(file_path, new_file_name)
        print file_path
        if file_path != new_file_name:
            print "\033[32m Succesfull change to: " + new_file_name + "\033[0m"
    except OSError:
        print '\033[31mSomething, something was broken with: \033[0m' + file_path
    # print new_file_name


# first, get the folder with music and music format
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


for folder in folders:
    os.chdir(folder)
    # print "*" + music_format
    # get list of mp3 files in folder
    music_files = glob.glob("*" + music_format)
    # print music_files
    for music_file in music_files:
        setNameToFileByTag(music_file, music_format)
