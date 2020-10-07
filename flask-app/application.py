from flask import Flask, render_template, request
import pickle5 as pickle
from recommender import calculate_best_movies
from recommender import similar_users_recommender
from recommender import movieId_to_title

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    movies = []
    return render_template('index.html')


@app.route('/ratings', methods=['POST', 'GET'])
def ratings():
    user_input = dict(request.form)
    print(user_input)
    if 'movielist' in user_input.keys():
        movielist = user_input['movielist']
        ids = list(map(int, movielist.split(',')))
        titles = movieId_to_title(ids)
        movies = dict(zip(titles, ids))
    else:
        movies = dict()
    pkl_filename = "tmp.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(movies, file)
    print(movies)
    return render_template('ratings.html', movie_list=movies.items())


@app.route('/recommendations', methods=['GET', 'POST'])
def recommender():
    with open("tmp.pkl", 'rb') as file:
        user_input_movies = pickle.load(file)
    user_input_movies = list(user_input_movies)
    user_input_ratings = request.args.getlist('rating_values')
    user_input_ratings = [int(x) for x in user_input_ratings]
    result = calculate_best_movies(user_input_movies, user_input_ratings)
    result2 = similar_users_recommender(user_input_movies, user_input_ratings)
    return render_template('recommendations.html', nmf=result, cosim=result2)

if __name__ == '__main__':

    app.run(debug = True)   # this will start an infinite process, i.e. serving our web page.
    #                        # 'debug = True' displays Back-End errors to the browser, which is useful for local development, NOT for production
                            # Also automatically restarts server upon changes to code.
