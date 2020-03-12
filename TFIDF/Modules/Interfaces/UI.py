#!/usr/bin/env python

def Answer():
    ans=input("\nYour choise is: ")
    ans=ans.lower()
    print()
    return ans

# Printing help information
def Help():
    print(" "*27 + "HELP")
    print("%-15s%-45s" % ("COMMAND", "VALUE"))
    print("%-15s%-45s" % ("h", "This information"))
    print("%-15s%-45s" % ("1", "TF for text"))
    print("%-15s%-45s" % ("2", "TF for all texts"))
    print("%-15s%-45s" % ("3", "IDF"))
    print("%-15s%-45s" % ("4", "TF*IDF for text"))
    print("%-15s%-45s" % ("5", "TF*IDF for all texts"))
    print("%-15s%-45s" % ("6", "Cosine similarity of texts by TF"))
    print("%-15s%-45s" % ("7", "Cosine similarity of texts by TF*IDF"))
    print("%-15s%-45s" % ("c", "Removing corpus and creating new"))
    print("%-15s%-45s" % ("any other", "Exit from program"))

# Printing tf or tfidf for text
def TextInfo(names_of_files, list):
    name = input("Enter file's name: ")
    if name in names_of_files:
        index = names_of_files.index(name)
        print(list[index])
    else:
        print("There is not such file in list: " + name)

# Printing tf or tfidf for all texts from corpus
def CorpusInfo(names_of_files, files_amount, list):
    for i in range(0, files_amount):
        print(names_of_files[i])
        print(list[i])