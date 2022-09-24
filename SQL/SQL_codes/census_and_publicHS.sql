
-- 1. How many public high schools are in each zip code? 
-- select zip_code, count(school_id)
-- from HS_table
-- GROUP by zip_code
-- order by zip_code ASC;

-- 2. How many public high schools are in each state?
-- select state_code, count(school_id)
-- from HS_table
-- GROUP by state_code
-- order by state_code ASC;

-- 3. Trying to get the min/max value for locale_code, but i'm getting a null value for max
--    found out that there's a NULL ROWS  
-- SELECT school_id, school_name, locale_code
-- FROM HS_table
-- WHERE locale_code like 'n%';

-- 4. We can do searching the local_code of these school_name with null's and replace it but will not do it for now.
--    I will just drop it.
-- UPDATE HS_table
-- set locale_code = NULL
-- WHERE locale_code = 'NULL';

-- 5. Now we can querry min and max 
-- SELECT min(locale_code), max(locale_code) as maxumim
-- FROM HS_table;

-- 6. The locale_code column in the high school data corresponds to `various levels of urbanization`. 
--    Using the CASE statement to display the corresponding locale_text and locale_size in our query result.
-- SELECT  school_name, locale_code,
-- -- 
-- -- Urbanization level
-- CASE 
-- WHEN locale_code <= 13 THEN 'City'
-- WHEN locale_code <= 23 THEN 'Suburb'
-- -- 
-- WHEN locale_code <= 33 THEN 'Town'
-- WHEN locale_code <= 43 THEN 'Rural'
-- END AS 'Urbanization_level',
-- --   
-- --  note that all locale_codes ends with interger 1,2 ,and 3.
-- --  substring for city and suburb
-- CASE WHEN  locale_code <=23 THEN
-- -- last 2 incdeces 
-- CASE substr(locale_code, 2, 2) 
-- WHEN '1' THEN 'Large'
-- WHEN '2' THEN 'Midsize'
-- WHEN '3' THEN 'Small'
-- END 
-- -- 
-- -- substring for town and rural
-- WHEN locale_code >=31 THEN 
-- CASE substr(locale_code, 2, 2)
-- WHEN '1' THEN 'Fringe'
-- WHEN '2' THEN 'Distant'
-- WHEN '3' THEN 'Remote'
-- ELSE 'No data'
-- END
-- -- 
-- END AS 'Size'
-- -- 
-- -- 
-- FROM HS_table;

-- 7. What is the minimum, maximum, and average median_household_income of the nation?
-- replace null value first 
-- 	UPDATE census_table
-- 	SET median_household_income = NULL
-- 	WHERE median_household_income = 'NULL';
-- 	-- 
-- 	SELECT avg(median_household_income) as average,
-- 	       min(median_household_income) as minimum,
-- 		   max(median_household_income) as maximum
-- 	FROM census_table;

-- 8. What is the minimum, maximum, and average median_household_income for each state?
-- SELECT state_code,
-- 	   avg(median_household_income) as average,
--        min(median_household_income) as minimum,
-- 	   max(median_household_income) as maximum
-- FROM census_table
-- GROUP by state_code;




-- ###### Join/with analysis: #######

-- 1. Do characteristics of the zip-code area, such as median household income, influence students’ performance in high school?
--    divide the median_household_income into income ranges (e.g., <$50k, $50k-$100k, $100k+) and find the average exam scores for each.
--    left join two tables by zip_code
-- SELECT       
-- -- 1 	   	   
-- CASE 
-- WHEN median_household_income <50000 THEN '$50k less than'
-- WHEN median_household_income >= 50000 AND median_household_income <= 100000 THEN '$50-100k'
-- WHEN median_household_income > 100000 THEN '$100k above'
-- ELSE 'No data available'
-- END AS 'Income bracket',
-- -- 2
-- ROUND(AVG(pct_proficient_math),0)    AS 'AVG pct_proficient_math ',
-- -- 3
-- ROUND(AVG(pct_proficient_reading),0) AS 'AVG pct_proficient_reading'
-- -- 
-- FROM census_table
-- LEFT JOIN HS_table
-- on census_table.zip_code = HS_table.zip_code
-- -- 
-- GROUP by 1
-- order by 1
-- ;


-- 2. On average, do students perform better on the math or reading exam? 
-- Find the number of states where students do better on the math exam, and vice versa.
-- 
-- ### TEMPORARY TABLE ###
-- WITH temp_table as (
-- SELECT 
-- --1
-- state_code, 
-- --2
-- ROUND(AVG(pct_proficient_math), 0) AS 'Math Results', 
-- --3
-- ROUND (AVG(pct_proficient_reading), 0) AS 'Reading Results', 
-- --4
-- CASE 
-- WHEN ROUND(AVG(pct_proficient_math), 0) > ROUND (AVG(pct_proficient_reading), 0) THEN 'Math'
-- WHEN ROUND (AVG(pct_proficient_reading), 0) > ROUND(AVG(pct_proficient_math), 0) THEN 'Reading'
-- ELSE 'No Exam Data'
-- END AS 'Highest_Subject'
-- --
-- FROM HS_table
-- GROUP by 1)
-- -- ;
-- 
-- -- ### QUERY from TEMPORARY TABLE  ### 
-- SELECT 
-- Highest_Subject,
-- COUNT(*) as 'state_code count'
--  
-- FROM temp_table
-- GROUP by Highest_Subject
-- ORDER by 2 DESC
-- ;


-- 3. What is the average proficiency on state assessment exams for each zip code, and how do they compare to other zip codes in the same state?
-- ### TEMPORARY TABLE 2  ### 
-- WITH temp_table2 AS (
-- SELECT 
-- HS_table.state_code as 'State', 
-- ROUND(AVG(pct_proficient_math), 0) AS 'State_Math_Avg', 
-- ROUND (AVG(pct_proficient_reading), 0) AS 'State_Reading_Avg', 
-- MAX(pct_proficient_math) AS 'Max Math Score', MIN(pct_proficient_math) AS 'Min Math Score',
-- MAX(pct_proficient_reading) AS 'Max Reading Score', MIN(pct_proficient_reading) AS 'Min Reading Score'
-- FROM HS_table
-- GROUP BY 1)
-- 
-- -- ### QUERY on TEMPORARY TABLE 2 ###	 
-- SELECT 
-- temp_table2.state, 
-- HS_table.zip_code,
-- temp_table2.State_Math_Avg,
-- ROUND(AVG(pct_proficient_math), 0) AS 'Zip_Math_Avg', 
-- temp_table2.State_Reading_Avg, 
-- ROUND(AVG(pct_proficient_reading), 0) AS 'Zip_Reading_Avg'
-- -- 
-- FROM HS_table
-- JOIN temp_table2
-- ON HS_table.state_code = temp_table2.state
-- GROUP BY 2; 
-- -- 

