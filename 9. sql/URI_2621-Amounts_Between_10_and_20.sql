SELECT  products.name from products
JOIN providers on products.id_providers=providers.id
WHERE products.amount <= 20 and products.amount >= 10 and providers.name like 'P%';