(SELECT name as type, (price + 20.0) as price FROM products WHERE type='A' ORDER BY id DESC) 
UNION ALL
(SELECT name as type, (price + 70.0) as price FROM products WHERE type='B' ORDER BY id DESC)
UNION ALL
(SELECT name as type, (price + 530.5) as price FROM products WHERE type='C' ORDER BY id DESC);