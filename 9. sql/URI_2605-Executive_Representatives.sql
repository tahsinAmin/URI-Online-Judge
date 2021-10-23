SELECT  products.name, providers.name from products
JOIN providers on products.id_providers=providers.id
JOIN categories on products.id_categories=categories.id
WHERE categories.id=6;