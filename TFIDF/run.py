#!/usr/bin/env python

import sys
from Modules.Interfaces import Files
from Modules.Interfaces import UI
from Modules.Interfaces import SimilarityTable as ST
from Modules.Algorithms import TFIDF
from Modules.Algorithms import Cos

# Creating and processing corpus of texts
def CorpusCreation():
    names_of_files = []
    texts = []
    tf_list = []

    common_dictionary = {}
    Files.AddingFiles(names_of_files, texts)
    common_dictionary = {}
    files_amount = len(names_of_files)
    for text in texts:
        processed_text=TFIDF.TextProcessing(text)
        tf = TFIDF.TF(processed_text)
        tf_list.append(tf)
        TFIDF.WordCounter(tf, common_dictionary)
    idf = TFIDF.IDF(common_dictionary, files_amount)
    tfidf = TFIDF.TFIDF(tf_list, idf)
    cos_tf = Cos.CosineSimilarity(tf_list, files_amount)
    cos_tfidf = Cos.CosineSimilarity(tfidf, files_amount)
    print ("Type \'h\' for help, or enter another command")
    Menu(names_of_files, texts, files_amount, tf_list, idf, tfidf, cos_tf, cos_tfidf)

def Menu(names_of_files, texts, files_amount, tf_list, idf, tfidf, cos_tf, cos_tfidf):
    ans = UI.Answer()
    if ans=='h':
        UI.Help()
    elif ans=='1':
        print("TF for text:")
        UI.TextInfo(names_of_files, tf_list)
    elif ans=='2':
        print("TF for all texts:")
        UI.CorpusInfo(names_of_files, files_amount, tf_list)
    elif ans=='3':
        print("IDF:")
        print(idf)
    elif ans=='4':
        print("TF*IDF for text:")
        UI.TextInfo(names_of_files, tfidf)
    elif ans=='5':
        print("TF*IDF for all texts")
        UI.CorpusInfo(names_of_files, files_amount, tfidf)
    elif ans=='6':
        print("Cosine similarity of texts by TF")
        ST.PrintTable(cos_tf, names_of_files, files_amount)
    elif ans=='7':
        print("Cosine similarity of texts by TF*IDF")
        ST.PrintTable(cos_tfidf, names_of_files, files_amount)
    elif ans=='c':
        print("Removing texts' corpus and creating a new one")
        CorpusCreation()
    else:
        print("Exit from program\n")
        exit()
    Menu(names_of_files, texts, files_amount, tf_list, idf, tfidf, cos_tf, cos_tfidf)

CorpusCreation()