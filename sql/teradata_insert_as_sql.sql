     INSERT INTO customer
     SELECT
     name as customer_name,
     address as customer_address,
     phone as customer_phone
     FROM customer_raw cr
     join customer_raw_temp crt
     on cr.name = crt.name;