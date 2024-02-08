-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(r.rate) AS rating
FROM tv_shows As s 
INNER JOIN tv_show_ratings AS r ON s.id = r.show_id
INNER JOIN tv_show_genres As t ON s.id = t.show_id
INNER JOIN tv_genres AS g ON t.genre_id = g.id
GROUP BY name
ORDER BY rating DESC;