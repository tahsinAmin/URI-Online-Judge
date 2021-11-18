SELECT REGEXP_REPLACE(natural_person.cpf, '([[:digit:]]{3})([[:digit:]]{3})([[:digit:]]{3})([[:digit:]]{2})','\1.\2.\3-\4')
FROM natural_person
JOIN customers ON natural_person.id_customers = customers.id;