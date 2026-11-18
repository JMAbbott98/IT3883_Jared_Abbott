
SELECT day_of_week, AVG(temperature_value) AS average_temp
FROM assignment5table WHERE day_of_week IN ('Thursday', 'Sunday')
GROUP BY day_of_week;


insert into assignment5table(day_of_week, temperature_value)
values 