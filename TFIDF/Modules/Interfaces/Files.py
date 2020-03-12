#!/usr/bin/env python

# Reading and checking names of files
def ReadingNamesOfFiles(names_of_files, new_files):
    names = input("Enter file(s) name(s): ")
    names = names.split()
    if len(names) == 0:
        print("There is no files for adding")
    for name in names:
        if (name in names_of_files) or (name in new_files):
            print("This file is already in list: " + name)
        else:
            new_files.append(name)
    names = ""

def CheckingFiles(new_files, new_texts):
    not_a_file=[]
    for file_name in new_files:
        try:
            text = ReadingFile(file_name)
            if len(text.split()) == 0:
                print("This file is empty: " + file_name)
                not_a_file.append(file_name)
            else:
                new_texts.append(text)    
        except:
            print("There is not such file: " + file_name)
            not_a_file.append(file_name)
    Cleaning(new_files, not_a_file)

# Reading text from file
def ReadingFile(file_name):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    return text

# Deleting not existing and empty files
def Cleaning(new_files, not_a_file):
    for name in not_a_file:
        new_files.remove(name)
    not_a_file = []

# Adding new files in corpus
def AddingFiles(names_of_files, texts):
    new_files=[]
    new_texts=[]
    ReadingNamesOfFiles(names_of_files, new_files)
    CheckingFiles(new_files, new_texts)
    AddingItem(names_of_files, new_files)
    AddingItem(texts, new_texts) 

def AddingItem(items, new_items):
    for item in new_items:
        items.append(item)
    new_items = []