-- Genre ID by show
SELECT
  tv_shows.title,
  tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv.shows.id = tv_show_genres.show_id
ORDER BY tv_show_title ASC, tv_show_genre_id ASC;

