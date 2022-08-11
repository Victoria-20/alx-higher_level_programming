-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) as average_temperature_July_Aug
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

