SELECT name, trunc(((score.math*2)+(score.specific*3)+(score.project_plan*5))/10,2) as avg 
FROM candidate
JOIN score on score.candidate_id=candidate.id
ORDER BY avg DESC;