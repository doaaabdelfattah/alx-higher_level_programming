-- lists all genres of the show Dexter.
SELECT a.name
FROM tv_genres AS a
INNER JOIN tv_show_genres AS b
ON a.id = b.genre_id
WHERE b.show_id IN (
SELECT id FROM tv_shows
WHERE title = "Dexter")
ORDER BY a.name ASC;