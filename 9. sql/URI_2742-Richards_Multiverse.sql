SELECT li.name, round((1.618*li.omega),3) AS "The N Factor" FROM dimensions di
JOIN life_registry li on di.id=li.dimensions_id
WHERE (di.name = 'C774'  OR di.name = 'C875')
AND li.name LIKE 'Richard%' ORDER BY li.omega;