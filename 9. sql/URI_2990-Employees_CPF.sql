SELECT empregados.cpf, empregados.enome, departamentos.dnome 
FROM empregados
JOIN  departamentos on empregados.dnumero = departamentos.dnumero 
WHERE cpf NOT IN (SELECT cpf_emp FROM trabalha) ORDER BY cpf;