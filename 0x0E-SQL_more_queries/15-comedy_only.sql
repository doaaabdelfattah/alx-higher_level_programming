-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT c.title
FROM tv_genres AS a
INNER JOIN tv_show_genres AS b ON a.id = b.genre_id
INNER JOIN tv_shows AS c ON b.show_id = c.id
WHERE a.name = "comedy"
ORDER BY c.title ASC;