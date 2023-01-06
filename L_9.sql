9.1.
select manager_id,to_char(null) job_id, to_number(null) department_id, sum(salary) 
from employees 
group by manager_id
union
select to_number(null), job_id, to_number(null), sum(salary)
from employees group by job_id
union
select to_number(null), to_char(null), department_id, sum(salary)
from employees 
group by department_id;

9.2.
select * from employees;
select department_id, manager_id from employees where manager_id=100
union
select department_id, manager_id from employees where manager_id<>145 and manager_id<>201;

select * from employees;
select department_id, manager_id from employees where manager_id=100
union
select department_id, manager_id from employees where manager_id not in (145, 201);

9.3.
select first_name, last_name, salary from employees where upper(first_name) like '_A%'
intersect 
select first_name, last_name, salary from employees where
upper(last_name) like '%S%';

9.4.
select * from locations;
select * from countries;
select location_id, postal_code, city from locations where
country_id in (select country_id from countries where country_name in ('Italy', 'Germany'))
union all
select location_id, postal_code, city from locations where to_char(postal_code) like '%9%';

9.5.
select * from countries;
select * from regions;
select country_id id, country_name country, region_id region from countries where length(country_name)>8
union
select country_id, country_name, region_id from countries where
region_id not in (select region_id from regions where region_name = 'Europe')
order by country desc;

