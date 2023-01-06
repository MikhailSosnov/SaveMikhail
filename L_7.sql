7.1.
select region_name, count(*) 
from employees e
join departments d on (e.department_id=d.department_id)
join locations l on (d.location_id=l.location_id)
join countries c on (l.country_id=c.country_id)
join regions r on (c.region_id=r.region_id)
group by region_name;

7.2.
select e.first_name, e.last_name, 
d.department_name, 
e.job_id, l.street_address, c.country_name, r.region_name
from employees e
join departments d on (e.department_id=d.department_id)
join locations l on (d.location_id=l.location_id)
join countries c on (l.country_id=c.country_id)
join regions r on (c.region_id=r.region_id);

7.3. 
select emp2.first_name, count(*)
from employees emp1 
join employees emp2 on (emp1.manager_id=emp2.employee_id) group by emp2.first_name having count (*)>6;

7.4.
select d.department_name, count(*) from employees e 
join departments d  on (e.department_id = d.department_id) group by d.department_name having count(*)>=30 order  by d.department_name;

7.5.
select d.department_id, department_name from employees e 
right join departments d  on (e.department_id = d.department_id) where first_name is null order by d.department_id;

7.6. 
select * from employees where manager_id=100;
select * from employees emp1 right join employees emp2 on (emp1.employee_id = emp2.manager_id) where to_char(emp1.hire_date, 'yy')='05' and 
to_char(emp2.hire_date,'yy')>'05';

7.7.
select * from countries;
select * from regions;
select * from regions r join countries c on r.region_id=c.region_id;

7.8.
select * from employees;
select * from jobs;
select e.first_name, e.last_name, e.salary FROM employees e join jobs j on e.job_id=j.job_id where e.salary<min_salary+1000;

7.9.
select * from employees;
select * from departments;
select * from locations;
select * from countries;
select * from employees e join departments d on (e.department_id=d.department_id)
join locations l on (d.location_id=l.location_id)
join countries c on (l.country_id=c.country_id)
join regions r on (c.region_id=r.region_id);

select e.first_name, e.last_name, c.country_name from employees e join departments d on (e.department_id=d.department_id)
join locations l on (d.location_id=l.location_id)
join countries c on (l.country_id=c.country_id)
join regions r on (c.region_id=r.region_id);

select e.first_name, e.last_name, c.country_name from employees e join departments d on (e.department_id=d.department_id)
join locations l on (d.location_id=l.location_id)
right join countries c on (l.country_id=c.country_id)
join regions r on (c.region_id=r.region_id); В конце таблицы - нет информеации о сотруднике.

select e.first_name, e.last_name, c.country_name from employees e 
full outer join departments d on (e.department_id=d.department_id)
full outer join locations l on (d.location_id=l.location_id)
full outer join countries c on (l.country_id=c.country_id)
full outer join regions r on (c.region_id=r.region_id);

7.10. 
select e.first_name, e.last_name, c.country_name from employees e cross join countries c;

7.11.
select region_name,count(*) 
from employees e, departments d, locations l, countries c, regions r 
where (e.department_id=d.department_id)
or (d.location_id=l.location_id)
or (l.country_id=c.country_id)
or (c.region_id=r.region_id)
group by region_name;

7.12.
select d.department_id, department_name from employees e, departments d 
where (e.department_id(+) = d.department_id)and first_name is null order by d.department_id;
