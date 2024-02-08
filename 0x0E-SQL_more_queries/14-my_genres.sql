-- lists all genres of the show Dexter.
SELECT a.name
FROM tv_genres AS a
INNER JOIN tv_show_genres AS b ON a.id = b.genre_id
INNER JOIN tv_shows AS c ON b.show_id = c.id
WHERE c.title = "Dexter"
ORDER BY a.name ASC;
