#!/usr/bin/env python

import math

# Creating matrix of texts' cosine similarity
def CosineSimilarity(dictionary, files_amount):
    cosine=[]
    for i in range(0, files_amount):
        similarity = []
        for j in range(i+1, files_amount):
            similarity.append((Cosine(dictionary[i], dictionary[j])))
        if similarity != []:
            cosine.append(similarity)
    return cosine

# Counting cosine similarity between 2 texts
def Cosine(text1, text2):
    numerator = 0
    denominator = 0
    for word in text1:
        if word in text2:
            numerator += (text1[word]*text2[word])
    denominator_part1 = Denominator(text1)
    denominator_part2 = Denominator(text2)
    denominator = denominator_part1 * denominator_part2
    cosine = numerator / denominator
    cosine = round(cosine, 7)
    return cosine

# Counting denominator
def Denominator(text):
    denominator = 0
    for word in text:
        denominator += math.pow(text[word], 2)
    denominator = math.sqrt(denominator)
    return denominator