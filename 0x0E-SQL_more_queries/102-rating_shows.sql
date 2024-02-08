--  lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT s.title, SUM(rate) AS rating
FROM tv_shows As s INNER JOIN tv_show_ratings AS r
ON s.id = r.show_id
GROUP BY s.title
ORDER BY rating DESC;