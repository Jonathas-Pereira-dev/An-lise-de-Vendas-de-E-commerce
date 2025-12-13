select
o.order_id,
o.order_date,
c.customer_name,
o.total_amount
from {{ ref('stg_orders') }} o
join {{ ref('stg_customers') }} c
on o.customer_id = c.customer_id