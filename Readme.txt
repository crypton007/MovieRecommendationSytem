I have used PostgresSql as schema and relation was already so used a relational database.
PostgresSql is easy to use and is one of the best relational database, additionally it is easy to install and set up as well in comparision to mysql therefore I used PostgresSql.


Tables created:

movies
ratings
links
tags
genome_links
genome_scores
genre
movie_genres
userRecommendations
similaruserids

Query :
For tables movies, ratings, links, tags, genome_links, genome_scores

CREATE TABLE TableName
(
	ColumnName DataType
	PRIMARY KEY(columnName)
);

To copy data from csv to the tables above

COPY TableName
From 'PATH'
DELIMITERS ',' CSV HEADER ;

genre table contains all unique genres with genreid

create table genre
(
    id serial PRIMARY KEY,
    genre VARCHAR ( 50 )
); 

INSERT INTO genres (genres) (select distinct unnest(string_to_array(genres,'|')) genres from movies_ratings);

movie_genre is pivot table having many to many relationship with genre and movies tables

INSERT INTO movie_genre (movieid, genreid)
SELECT m.movieid, g.id
FROM movies m
CROSS JOIN unnest(string_to_array(m.genre, '|')) WITH ORDINALITY arr(genre, ordinal)
JOIN genre g ON g.genre = arr.genre;



Materialized View created :
Topmovies : To store weighted rating of all movies using IMDB formula.


Query 

 SELECT round(avg(r.rating)::numeric, 2) AS avg_rating,
    count(r.userid) AS user_count,
    round((count(r.userid)::double precision / (count(r.userid) + 1000)::double precision * avg(r.rating) + 1000::double precision / (count(r.userid) + 1000)::double precision * 3.53::double precision)::numeric, 2) AS weightedrating,
    r.movieid,
    m.title,
    m.genre
   FROM ratings r
     LEFT JOIN movies m ON r.movieid = m.movieid
  GROUP BY r.movieid, m.title, m.genre
 HAVING count(r.userid) 
  ORDER BY (round((count(r.userid)::double precision / (count(r.userid) + 1000)::double precision * avg(r.rating) + 1000::double precision / (count(r.userid) + 1000)::double precision * 3.53::double precision)::numeric, 2)) DESC;



Index Created
* allmovie Index on table Movie