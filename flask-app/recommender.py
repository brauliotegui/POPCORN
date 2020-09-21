"""Machine-Learning Code that returns movie recommendations"""
import numpy as np
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle5 as pickle

MOVIES = pd.read_csv('ml-latest-small/movies.csv')
RATINGS = pd.read_csv('ml-latest-small/ratings.csv')
DF = pd.merge(RATINGS, MOVIES, left_on='movieId', right_on='movieId')

MIDS = RATINGS['movieId'].unique()
MIDS = pd.DataFrame(MIDS)
MOVIES_DF = pd.merge(MIDS, MOVIES, left_on=0, right_on='movieId')

# better:
with open("nmf_model.pkl", 'rb') as file:
    m = pickle.load(file)
P = m.components_

def calculate_best_movies(result_html):
    ''' doc '''
    column_names = ['title', 'rating']
    user_input = pd.DataFrame(result_html, columns=column_names)

    r_true = DF.pivot(index='userId', columns='movieId', values='rating')
    r_true.fillna(2.5, inplace=True)
    m = NMF(max_iter=500, n_components=21)
    m.fit(r_true)
    P = m.components_

    user_ratings = pd.merge(MOVIES_DF, user_input, left_on='title', right_on='title', how='left')
    new_user = user_ratings['rating'].fillna(2.5)
    new_u = np.array(new_user).reshape(1, -1)
    profile = m.transform(new_u)
    result = np.dot(profile, P)
    MOVIES_DF['recom'] = result.T

    result = MOVIES_DF.sort_values('recom', ascending=False)['title'].head(5)
    return result

def similar_users_recommender(result_html):
    ''' doc '''
    column_names = ['title', 'rating']
    user_input = pd.DataFrame(result_html, columns=column_names)

    user_ratings = pd.merge(MOVIES_DF, user_input, left_on='title', right_on='title', how='left')
    query = user_ratings['rating']
    query = np.array(query)

    m_matrix = DF.pivot_table(values='rating', index='userId', columns='movieId')
    m_matrix.loc['e'] = query
    m_matrix = m_matrix.sub(m_matrix.mean(axis=0), axis=1)
    m_matrix.fillna(0, inplace=True)

    cosim = cosine_similarity(m_matrix)[-1]
    cosim = pd.DataFrame(cosim)
    top10 = cosim.sort_values(by=[0], ascending=[False]).head(11)  #order by most similar users
    similar_users = list(top10.index)
    similar_users = similar_users[1:]

    users_r = m_matrix.loc[similar_users, :]
    movie_ratings_avg = users_r.mean()
    movie_ratings_avg = pd.DataFrame(movie_ratings_avg)

    rec_movies = movie_ratings_avg.sort_values(by=[0], ascending=[False]).head(10)
    rec_movies = pd.merge(rec_movies, MOVIES, left_on='movieId', right_on='movieId', how='left')

    result = rec_movies['title']
    return result

def movieId_to_title(ids):
    ''' Given a list of movieIds, returns a corresponding list of movie titles.'''
    return MOVIES.set_index('movieId').loc[ids]['title'].tolist()
