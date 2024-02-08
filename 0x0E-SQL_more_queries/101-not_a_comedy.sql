--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT distinct title
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS t ON s.id = t.show_id
LEFT JOIN tv_genres AS g ON t.genre_id = g.id
WHERE title NOT IN 
(
SELECT title
FROM tv_shows AS s
INNER JOIN tv_show_genres AS t ON s.id = t.show_id
INNER JOIN tv_genres AS g ON t.genre_id = g.id
WHERE name = "Comedy")
ORDER BY title ASC;

