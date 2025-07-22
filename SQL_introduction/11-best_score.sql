-- All scores aboeve 10
Select score, name
FROM second_table
WHERE score >= 10
ORDER BY score, DESC;
