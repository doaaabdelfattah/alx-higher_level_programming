--  list all genres not linked to the show Dexter
SELECT DISTINCT name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS t ON s.id = t.show_id
LEFT JOIN tv_genres AS g ON t.genre_id = g.id
WHERE name NOT IN (
SELECT name
FROM tv_shows AS s
INNER JOIN tv_show_genres AS t ON s.id = t.show_id
INNER JOIN tv_genres AS g ON t.genre_id = g.id
WHERE s.title = "Dexter")
ORDER BY name ASC;