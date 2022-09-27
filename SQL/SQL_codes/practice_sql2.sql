SELECT 
	state_code, 
	pop_total
FROM census_table
GROUP by state_code
ORDER by pop_total DESC
;