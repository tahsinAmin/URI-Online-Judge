SELECT products.id, products.name from products
JOIN categories on products.id_categories=categories.id
WHERE categories.name like 'super%';