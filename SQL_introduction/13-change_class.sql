-- Remove underperformers
DELETE FROM second_table
WHERE score <= 5
