from flask import Flask, render_template
from flask import request, redirect
import recommender as rec #import all objects from recommender.py

app = Flask(__name__) # tells Flask to make THIS script the center of the application


@app.route('/')    # whenever user visits HOSTNAME:PORT/index, this function is triggered: Flask Decorator
@app.route('/index')         # 'index' as name is purely conventiona, could be anything
def index():
    movies=[]
    user_input = dict(request.args)              # copied from github to make it worl
    if 'movielist' in user_input:
        movielist = user_input['movielist']
        ids = list(map(int, movielist.split(',')))
        titles = rec.movieId_to_title(ids)
        movies = zip(titles,ids)
        movies = movielist
        return (request.form['movies'])
    return render_template('index.html', movies_html = movies)


@app.route('/ratings', methods = ['POST','GET'])
def ratings():
    user_input = request.args
    if 'movielist' in user_input:
        movielist = user_input['movies']
        ids = list(map(int, movielist.split(',')))
        titles = rec.movieId_to_title(ids)
        movies = zip(titles,ids)
        movies = movielist
        return (request.form['movies'])
    return render_template('ratings.html', ratings_html=ratings)



@app.route('/recommendations')          # Python decorator modifies the function that is defined ON THE NEXT LINE
def recommender():                      # function HAS TO FOLLOW on the NEXT LINE
    ratings = dict(request.args)        # integrate user-defined input with ratings as an dictionary
                                        # Flask transforms Back-End to Front-End: Key-Event for RESPONSE
    #result = rec.random_recommend(8)    # this is NOT NEEDED anymore
     # this are the ratings input in index-webpage
    recommendations = rec.calculate_best_movies(ratings)# given from users and the function saved in recommender.py
    return render_template('recommendations.html', result_html=recommendations.items())# ratings.items())



if __name__ == '__main__':
    # whatever occurs AFTER this line is executed when we run 'python application.py'
    # however, whatever comes AFTER  this line is NOT executed when we IMPORT application.py

    app.run(debug = True)   # this will start an infinite process, i.e. serving our web page.
    #                        # 'debug = True' displays Back-End errors to the browser, which is useful for local development, NOT for production
                            # Also automatically restarts server upon changes to code.
