SELECT products.name, providers.name, categories.name from products
JOIN providers on products.id_providers = providers.id
JOIN categories on products.id_categories = categories.id
WHERE providers.name='Sansul SA' and categories.name='Imported';