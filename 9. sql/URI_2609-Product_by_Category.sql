SELECT categories.name as name, SUM(products.amount) AS sum FROM products
JOIN categories on products.id_categories = categories.id
GROUP BY categories.name;