-- Task 20: Script that Display the max temperature of each state ordered by State name

SELECT state, MAX(value) AS max_temp
FROM temperature
GROUP BY state
ORDER BY state;
