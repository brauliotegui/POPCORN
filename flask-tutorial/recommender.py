"""Machine-Learning Code that returns movies"""
import numpy as np
from sklearn.decomposition import NMF
import pandas as pd


def calculate_best_movies(result_html):
    column_names = ['title', 'rating']
    user_input = pd.DataFrame(result_html, columns = column_names)

    movies = pd.read_csv('movies.csv')
    r = pd.read_csv('ratings.csv')
    df = pd.merge(r, movies, left_on = 'movieId', right_on = 'movieId')
    Rtrue = df.pivot(index = 'userId', columns = 'movieId', values = 'rating')
    Rtrue.fillna(2.5, inplace = True)
    m = NMF(max_iter = 500, n_components=21)
    m.fit(Rtrue)
    P = m.components_

    Ids = r['movieId'].unique()
    ID = pd.DataFrame(Ids)
    movie_info = pd.merge(ID, movies, left_on = 0, right_on = 'movieId')
    user_ratings = pd.merge(movie_info, user_input, left_on = 'title', right_on = 'title', how = 'left')
    new_user = user_ratings['rating'].fillna(2.5)
    nu = np.array(new_user).reshape(1, -1)
    profile = m.transform(nu)
    result = np.dot(profile, P)
    movie_info['recom'] = result.T

    result = movie_info.sort_values('recom', ascending=False)['title'].head(5)
    return result
