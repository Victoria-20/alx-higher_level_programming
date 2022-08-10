-- import in hbtn_0c_0 database this table temperatures.sql
mysqldump hbtn_0c_0 < temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC


