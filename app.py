from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
from database import db
from model.movies import movies
from sqlalchemy import text
from model.models import Genre,moviesRatingsModel
from model.userRecommendations import UserRecommendations
from model.similarUsers import SimilarUsers
from sqlalchemy.orm import joinedload
import pickle
import redis
# Connect to Redis
redisConnection = redis.Redis(host='localhost', port=6379, db=0)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/moviedatabase'


db.init_app(app)


@app.route('/allmovies',methods=['GET'])
@cross_origin()
def getAllMovies():
    cache_key = "searchResults:"
    data = redisConnection.get(cache_key)
    # print(data)
    # exit()
    if data:
        jsonResult = pickle.loads(data)
    else:
        all_movies = moviesRatingsModel.query.all()
        jsonResult = jsonify([{'movieid': movie.movieid, 'title': movie.title, 'genre': movie.genre} for movie in all_movies])
        redisConnection.set(cache_key,pickle.dumps(jsonResult))
        
    # all_movies = moviesRatingsModel.query.all()
    return jsonResult

@app.route('/titlesearch', methods=['GET'])
@cross_origin()
def searchByTitle():
    title = request.args.get("title")
    cache_key = "results"+title
    data = redisConnection.get(cache_key)
    if not title:
        if data:
            jsonResult = pickle.loads(data)
        else:
            all_movies = moviesRatingsModel.query.all()
            jsonResult = jsonify([{'movieid': movie.movieid, 'title': movie.title, 'genre': movie.genre} for movie in all_movies])
            redisConnection.set(cache_key,pickle.dumps(jsonResult))
    else:
        if data:
            jsonResult = pickle.loads(data)
        else:
            all_movies = moviesRatingsModel.query.filter(moviesRatingsModel.title.ilike(f"%{title}%")).all()
            jsonResult = jsonify([{'movieid': movie.movieid, 'title': movie.title, 'genre': movie.genre} for movie in all_movies])
            redisConnection.set(cache_key,pickle.dumps(jsonResult))
    return jsonResult

# #from materialized view
# @app.route('/allmovies',methods=['GET'])
# @cross_origin()
# def getAllMoviesView():
#     all_movies = moviesRatingsModel.query.all()
#     return jsonify([{'movieid': movie.movieid, 'title': movie.title, 'genre': movie.genre} for movie in all_movies])

# @app.route('/titlesearch/<title>', methods=['GET'])
# @cross_origin()
# def searchByTitle(title):
#     all_movies = moviesRatingsModel.query.filter(moviesRatingsModel.title.ilike(f"%{title}%")).all()
#     return jsonify([{'movieid': movie.movieid, 'title': movie.title, 'genre': movie.genre} for movie in all_movies])

# @app.route('/top',methods=['GET'])
# @cross_origin()
# def top_movies():
#     genre_string = request.args.get('genre', 'All')
#     genres = genre_string.split(',')
#     return "Top movies in the genres: " + str(genres)

@app.route('/genre',methods=['GET'])
@cross_origin()
def getAllGenre():
    allGenre = Genre.query.all()
    return jsonify([{'genre': genre.genre} for genre in allGenre])

@app.route("/topmovies", methods=["GET"])
@cross_origin()
def get_movies_by_genre():
    genre = request.args.get("genre")
    if not genre:
        movieList = moviesRatingsModel.query.filter().options(joinedload(moviesRatingsModel.genresrel)).order_by(moviesRatingsModel.weightedrating.desc()).limit(10).all()
    else:
        genre = tuple(genre.split(','))
        movieList = moviesRatingsModel.query.filter(moviesRatingsModel.genresrel.any(Genre.genre.in_(genre))).options(joinedload(moviesRatingsModel.genresrel)).order_by(moviesRatingsModel.weightedrating.desc()).limit(10).all()

    return jsonify([{'movieid': m.movieid, 'title': m.title, 'weightedrating': m.weightedrating, 'genre':m.genre} for m in movieList])
    # genre_list = genre.split(",")
    
    # # create a query to fetch movieid for the given genres
    # query = text("SELECT movieid FROM movie_genres mg \
    #               JOIN genre g ON mg.genreid = g.id \
    #               WHERE g.genre IN (SELECT unnest(:genre_list))")

    # # execute the query and get the results
    # result = db.engine.execute(query, genre_list=genre_list)
    # movie_ids = [row[0] for row in result]
    

    # return the result in JSON format
    # return jsonify(movie_ids)


    
@app.route("/recommendations", methods=["GET"])
@cross_origin()
def get_movie_recommendations():
    userid = request.args.get("userid")
    result = UserRecommendations.query.filter_by(userid=userid).first()
    if result:
        return jsonify({
            'recommendation_1': result.recommendation_1,
            'recommendation_2': result.recommendation_2,
            'recommendation_3': result.recommendation_3,
            'recommendation_4': result.recommendation_4,
            'recommendation_5': result.recommendation_5,
            'recommendation_6': result.recommendation_6,
            'recommendation_7': result.recommendation_7,
            'recommendation_8': result.recommendation_8,
            'recommendation_9': result.recommendation_9,
            'recommendation_10': result.recommendation_10
        })
    else:
        return jsonify({'message': 'No recommendations found for user {}'.format(userid)}), 404


@app.route("/similaruserids", methods=["GET"])
@cross_origin()
def get_movie_similaruserids():
    userid = request.args.get("userid")
    result = SimilarUsers.query.filter_by(userid=userid).first()
    if result:
        return jsonify({
            'similaruserid_1': result.similaruserid_1,
            'similaruserid_2': result.similaruserid_2,
            'similaruserid_3': result.similaruserid_3,
            'similaruserid_4': result.similaruserid_4,
            'similaruserid_5': result.similaruserid_5,
            'similaruserid_6': result.similaruserid_6,
            'similaruserid_7': result.similaruserid_7,
            'similaruserid_8': result.similaruserid_8,
            'similaruserid_9': result.similaruserid_9,
            'similaruserid_10': result.similaruserid_10
        })
    else:
        return jsonify({'message': 'No similaruserids found for user {}'.format(userid)}), 404