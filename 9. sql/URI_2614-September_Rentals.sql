SELECT customers.name, rentals.rentals_date from customers
JOIN rentals ON customers.id=rentals.id_customers
WHERE EXTRACT(MONTH FROM rentals.rentals_date) = 09;