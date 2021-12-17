SELECT d.name,round(SUM((a.hours*150*(1+w.bonus/100))),1) as salary FROM attendances as a JOIN doctors as d
ON a.id_doctor=d.id JOIN work_shifts as w ON a.id_work_shift=w.id
WHERE a.id_doctor=d.id and a.id_work_shift=w.id
GROUP BY d.name
ORDER BY salary DESC;