
-- 1. Query pop_total in each zip code (return zip_code, state_code, city, pop_total)
-- 
-- Note: census_table pop_total are counted by zip_code
-- census_table has no city while HS_table has, so I will JOIN these tables to extract necessary COLUMN from both tables
-- I will use zip_code as their joining COLUMN ID.
-- I use left join to retain zip_code from census_table even though there is none in HS_table
-- 
-- SELECT  
-- 		census_table.zip_code,
-- 		census_table.state_code,
-- 		HS_table.city,
-- -- 		HS_table.school_name,	
-- 		census_table.pop_total
-- -- 
-- FROM census_table
-- LEFT JOIN HS_table
-- on census_table.zip_code = HS_table.zip_code
-- -- 
-- -- group by city to eliminate duplicates 
-- -- because there are 2 or more schools in a city and we are not interested in school_name in this query
-- GROUP by HS_table.city
-- ORDER by census_table.pop_total DESC
-- LIMIT 10
-- ;




-- ### WINDOW function ###
-- Runnig total
with temp_table as (
SELECT  
		census_table.zip_code as zip_code,
		census_table.state_code as state_code,
		HS_table.city as city,
-- 		HS_table.school_name,	
		census_table.pop_total as pop_total
-- 
FROM census_table
LEFT JOIN HS_table
on census_table.zip_code = HS_table.zip_code
-- 
-- group by city to eliminate duplicates 
-- because there are 2 or more schools in a city and we are not interested in school_name in this query
GROUP by HS_table.city
ORDER by census_table.pop_total DESC
LIMIT 10 
)

-- ## QUERY from temp_table ##
SELECT *,
sum(pop_total) over (ORDER by state_code)
as 'running_pop_total'
-- 
FROM temp_table
-- GROUP by state_code
;
