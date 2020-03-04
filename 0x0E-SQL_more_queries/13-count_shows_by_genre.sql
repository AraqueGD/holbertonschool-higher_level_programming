-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT t_v_g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres t_v_g
INNER JOIN tv_show_genres
ON t_v_g.id = tv_show_genres.genre_id
GROUP BY t_v_g.name
ORDER BY number_of_shows DESC;
