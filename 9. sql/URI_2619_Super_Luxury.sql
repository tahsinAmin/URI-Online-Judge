SELECT products.name, providers.name, products.price from products
JOIN providers on products.id_providers = providers.id
JOIN categories on products.id_categories = categories.id
WHERE products.price > 1000 and categories.name='Super Luxury';