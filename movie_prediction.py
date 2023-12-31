# -*- coding: utf-8 -*-
"""Movie_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bkMHA3YEBhFDhCmddJOgp9TYULp_SlMi

**Import Library**
"""

import pandas as pd

import numpy as np

"""**Import Dataset**"""

df=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Movies%20Recommendation.csv')

df.head()

df.info()

df.shape

df.columns

"""**Get Features Selection**"""

dff=df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

dff.shape

dff

x=dff['Movie_Genre'] +' '+ dff['Movie_Keywords'] +' '+ dff['Movie_Tagline'] +' ' + dff['Movie_Cast'] +' '+ dff['Movie_Director']

x

x.shape

"""**Get Features Text Conversion to Tokens**"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf=TfidfVectorizer()

x=tfidf.fit_transform(x)

x.shape

print(x)

"""**Get Similarity Score using Cosine Similarity**"""

from sklearn.metrics.pairwise import cosine_similarity as cs

Sim_score=cs(x)

Sim_score

Sim_score.shape

"""**Get Movie Name as Input from user and Validate for Closest Spelling**"""

fmn=input('Enter your favourite movie name:')

All_movies_Title_List=df['Movie_Title'].tolist()

import difflib as d

Movie_Rec=d.get_close_matches(fmn,All_movies_Title_List)

print(Movie_Rec)

close_match=Movie_Rec[0]

print(close_match)

Index_of_close_match_movie=df[df.Movie_Title==close_match]['Movie_ID'].values[0]

#getting a similar movies list
Rec_score=list(enumerate(Sim_score[Index_of_close_match_movie]))

len(Rec_score)

"""**Get all movies sort based wrt Favourite Movies**"""

Sort_sim_movies=sorted(Rec_score,key=lambda x:x[1],reverse=True)
print(Sort_sim_movies)

#Movies name based on their indexes
print('Top 10 Movies Suggested for you:\n')
i=1
for movie in Sort_sim_movies:
  index=movie[0]
  title_from_index=df[df.index==index]['Movie_Title'].values[0]
  if(i<11):
    print(i,'.',title_from_index)
    i+=1