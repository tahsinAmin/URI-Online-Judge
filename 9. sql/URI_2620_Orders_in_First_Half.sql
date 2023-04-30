SELECT  customers.name, orders.id from orders
JOIN customers on orders.id_customers = customers.id
WHERE orders.orders_date <= '06-30-2016' and orders.orders_date >= '01-01-2016'
