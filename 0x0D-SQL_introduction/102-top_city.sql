-- displays the top 3 of cities temperature during July and August ordered by temperature (descending).
SELECT city, AVG(value) AS avg_tmp FROM temperatures WHERE month > 6 AND month < 9 GROUP BY city ORDER BY avg_tmp DESC LIMIT 3;
