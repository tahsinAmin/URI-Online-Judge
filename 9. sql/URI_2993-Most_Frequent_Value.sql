SELECT amount AS most_frequent_value FROM value_table GROUP BY amount ORDER BY COUNT(amount) DESC LIMIT 1;

-- https://codificandoonline.blogspot.com/2020/07/uri-2993-mais-frequente-sql-postgresql.html