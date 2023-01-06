select * from employees;
8.1.
select * from employees e where length(first_name) >(select avg(length(first_name)) from employees);
select avg(length(first_name)) from employees;
8.2.
select * from employees e where salary >(select avg(salary) from employees);
8.3.
select * from employees;
select * from  departments;
select * from locations;

select l.city, sum(salary), count(*) from employees e join 
departments d on (e.department_id=d.department_id) join 
locations l on (d.location_id=l.location_id) group by city
having sum(salary)=(select min(sum(salary)) from
employees e join 
departments d on (e.department_id=d.department_id) join 
locations l on (d.location_id=l.location_id) group by city);
8.4.
select * from employees where manager_id in 
(select employee_id from employees where salary>15000);
8.5.
select * from employees;
select * from departments;
select * from employees e right join departments d on (e.department_id=d.department_id);
select distinct d.department_id, department_name from employees e right join departments d on (e.department_id=d.department_id)
where e.first_name is Null order by department_id;
8.6.
select * from employees e1 left join employees e2 on (e1.employee_id = e2.manager_id) where e2.manager_id is null order by e1.employee_id;

select * from employees where employee_id not in 
(select manager_id from  employees where manager_id is not null);
8.7.
select e1.manager_id, e1.first_name from employees e1 join employees e2 on 
(e1.manager_id=e2.manager_id) 
group by e2.manager_id 
having count(*)>6; 

select * from employees e where (select count (*) 
from employees
where manager_id=e.employee_id)>6;

8.8.
select * from employees;
select * from departments;
select * from employees e join departments d on (e.department_id=d.department_id)
where department_name ='IT';

select * from employees e 
where e.department_id = (select d.department_id from 
departments d where department_name='IT');

8.9.
select manager_id, hire_date from employees where to_char(hire_date, 'yy')<'05'and 
manager_id in (select employee_id from employees where to_char(hire_date, 'yy')='05');

8.10.
select * from employees where (manager_id in (select employee_id from employees where to_char(hire_date, 'month')='сент€брь')) and
(job_id in (select job_id from jobs where length(job_title)>15));

