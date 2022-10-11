-- ormal code
-- 1 groupby sum
-- SELECT state_code, 
-- 	   city, 
-- 	   sum(pct_asian) 
-- 
-- FROM HS_table
-- GROUP by state_code, city
-- ;




-- 2 window function 
-- SELECT state_code, 
-- 	   city, 
-- 	   sum(pct_asian) OVER (PARTITION by state_code) as pct_asian_total_per_state
-- 
-- FROM HS_table
-- ;




-- 3 cumulative sum
-- SELECT 
-- -- 	   school_id,
-- -- 	   state_code, 
-- -- 	   city,
-- -- 	   pct_asian,
-- -- 	   sum(pct_asian) over (order by school_id) as cumulative_sum,
-- -- 	   avg(pct_asian) over (order by school_id) as cumulative_avg,
-- -- 	   count(pct_asian) over (order by school_id) as cumulative_count
-- -- 
-- -- from HS_table
-- -- ;