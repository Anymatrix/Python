## Overview

This script calculates TF, IDF, TF*IDF and Cosine Similarity for texts.

TF     - Term Frequency
IDF    - Inverse Document Frquency
TF*IDF - the product of two statistics, term frequency and inverse document frequency.
Cosine Similarity - shows proximity between texts. 

## Structure

├── run.py    			- The main script running the program
├── Modules                     - Contains script modules 
│   ├── __init__.py             - Initialization file 
│   ├── Algorithms		- Scripts with algorithms
│   │   ├── __init__.py		- Initialization file
│   │   ├── Cos.py		- Calculates Cosine Similarity
│   │   └── TFIDF.py		- Calculates TF, IDF, TF*IDF
│   └── Interfaces		- Contains scripts with user interfaces
│       ├── __init__.py		- Initialization file
│       ├── Files.py		- Inputing, opening and reading of texts' files 
│       ├── SimilarityTable.py	- Converts Cosine Similarity between texts to human readeble form
│       └── UI.py		- Some user interfaces, such as help and showing results
└── Texts			- Contains texts' examples

## Requirements

This code requires Python version 3.5 and higher.
Tested and work both on Windows and Linux

## Manual

Script starts with following command
``` bash
python3 run.py
```

