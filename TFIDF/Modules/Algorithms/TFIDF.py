#!/usr/bin/env python

import math

# Processing of text 
def TextProcessing(text):
    processed_text=[]
    table=str.maketrans('[]{}()<>/|\\\'\",.:;!?&@#$%^*-_+=`~', '                                ')
    processed_text=text.translate(table)
    processed_text=processed_text.lower().split()
    return processed_text

# Calculating TF
def TF(processed_text):
    tf = {}
    total_length=len(processed_text)
    WordCounter(processed_text, tf)
    for word in tf:        
        tf[word] = (1.0*tf[word])/total_length
        tf[word] = round(tf[word], 7)
    return tf

# Calculating IDF            
def IDF(dictionary, files_amount):
    idf = {}
    for word in dictionary:
        idf[word] = (1.0 * files_amount) / dictionary[word]
        idf[word] = math.log(idf[word])
        idf[word] = round(idf[word], 7)
    return idf

# Calculating TF*IDF
def TFIDF(tf_list, idf):
    tfidf=[]
    for tf in tf_list:
        tfidf_for_text = {}
        for word in tf:
            value = tf[word]*idf[word]
            value = round(value, 7)
            tfidf_for_text[word] = value
        tfidf.append(tfidf_for_text)
    return tfidf

# Creating a dictionary in format word:key, where key is amount of in document(s)
def WordCounter(text, dictionary):
    for word in text:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word] = 1  