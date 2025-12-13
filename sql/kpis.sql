-- Receita total
select sum(total_amount) as receita_total from fact_sales;

-- Ticket médio
select avg(total_amount) as ticket_medio from fact_sales;

-- Receita mensal
select date_trunc('month', order_date) as mes,
sum(total_amount) as receita
from fact_sales
group by mes
order by mes;