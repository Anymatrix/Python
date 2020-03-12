#!/usr/bin/env python

# Creating table of texts' cosine similarity
def CreateTable(cos, files_amount):
    table = []
    for i in range(0, files_amount):
        line = []
        if i < files_amount-1: 
            CollectingLine(cos, line, i)
            for value in cos[i]:
                line.append(value)
        else:
            CollectingLine(cos, line, i) 
        table.append(line)  
    return table               

# Creating line from table
def CollectingLine(cos, line, i):
    for j in range(0, i):
        value = cos[j]
        line.append(value[i-(j+1)])
    line.append(1)

# Printing table of texts' cosine similarity
def PrintTable(cos, names_of_files, files_amount):
    table=CreateTable(cos, files_amount)   
    out = " " * 5 +  "Similarity"
    for name in names_of_files:
        out += OutName(name)
    print(out)
    for i in range(0, files_amount):
        out = OutName(names_of_files[i])
        for value in table[i]:
                value_str = str(value)
                out += (15 - len(value_str)) * " " + value_str
        print(out)

# Formating text's name for output
def OutName(name):
    if len(name)<15:
        out_name = (15 - len(name)) * " " + name
    else:
        out_name = " " + name[:14]
    return out_name