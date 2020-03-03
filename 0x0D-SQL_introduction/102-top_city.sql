-- displays the top 3 of cities temperature during July and August ordered by temperature (descending).
SELECT city FROM temperatures, AVG(value) AS avg_tmp WHERE month > 6 AND month < 9 GROUP BY city ORDER BY avg_tmp DESC LIMIT 3;
