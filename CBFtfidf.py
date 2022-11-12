# content based filtering with tfidf vectorizer

## https://github.com/AlexanderNixon/Machine-learning-reads/blob/master/Movie-content-based-recommender-using-tf-idf.ipynb

import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from itertools import combinations
# import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# import data
ratings_df       = pd.read_csv('../ml-25m/ratings.csv')
movies_df        = pd.read_csv('../ml-25m/movies.csv')
tags_df          = pd.read_csv('../ml-25m/tags.csv')
genome_scores_df = pd.read_csv('../ml-25m/genome-scores.csv')
genome_tags_df   = pd.read_csv('../ml-25m/genome-tags.csv')

# data preparation

# initial dataset only includes users who rate at least 20 movies
def movies_least_ratings(df):
    # filters movies based on there ratings
    # movies: 59047
    # movies with at least 5 ratings: 32720
    # remaing ratings: 24945870 
    # ratings_available_df = pd.merge(ratings_df, movie_enough_ratings_df)
    groupby_movies_df = df.groupby(['movieId']).size()
    filtered_movies_df = groupby_movies_df[groupby_movies_df >= 5].reset_index()[['movieId']]

    return filtered_movies_df

def weighted_average_score(df, k = 0.8):
    n_views = df.groupby('movieId', sort = False).movieId.count()
    ratings = df.groupby('movieId', sort = False).rating.mean()
    scores = ((1-k) * (n_views/n_views.max()) + k * (ratings/ratings.max())).to_numpy().argsort()[::-1]
    df_deduped = df.groupby('movieId', sort = False).agg({'title': 'first', 'genres': 'first', 'ratings': 'mean'})

    return df_deduped.assign(views = n_views).iloc[scores]

def tfidfVectorization():
    tf = TfidfVectorizer(analyzer=lambda s: (c for i in range(1,4) for c in combinations(s.split('|'), r=i)))
    tfidf_matrix = tf.fit_transform(movies_df['genres'])

    return tfidf_matrix

def cosSimilarity(df):
    cosine_sim = cosine_similarity(df)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=movies_df['title'], columns=movies_df['title'])

    return cosine_sim_df

def CBF_recommendation(movies, M, items, k):
    ix = M.loc[:,movies].to_numpy().argpartition(range(-1,-k,-1))
    closest = M.columns[ix[-1:-(k+2):-1]]
    closest = closest.drop(movies, errors='ignore')
    print(pd.DataFrame(closest).merge(items).head(k))

def to_CBF(movieList):
    cosine_sim_df = cosSimilarity(tfidfVectorization())
    CBF_recommendation(movieList, cosine_sim_df, movies_df[['title', 'genres']], 10)

# to_CBF('2001: A Space Odyssey (1968)')