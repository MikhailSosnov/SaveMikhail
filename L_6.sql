select * from employees;
6.1.
select salary from employees group by salary;
select department_id from employees group by department_id order by department_id desc;
select department_id, min(salary), max(salary), min(hire_date), max(hire_date), count(*)
from employees group by department_id order by department_id desc;
61.2.
select first_name, substr(first_name,1,1), count (*) from employees;
select substr(first_name,1,1), count(*) from employees group by substr(first_name,1,1) having count(*)>=4 order by substr(first_name,1,1);
6.3.
select * from employees;
SELECT department_id, sum(department_id), salary, count(salary), sum(salary) FROM employees group by department_id, salary;
6.4.
select to_char(hire_date,'day'), count(*) from employees group by to_char(hire_date,'day');
6.5.
select department_id, count(*), sum(salary) from employees group by department_id 
having count(*)>5 and sum(salary)>30000 order by department_id; 
6.6.
select * from countries;
select region_id, sum(length(country_name)) from countries group by region_id having sum(length(country_name))>50 order by region_id;
6.7.
select * from employees;
select job_id, sum(round(salary)), count(*) from employees group by job_id order by job_id;
6.8.
select department_id from employees group by department_id 
having count (distinct job_id)>1;
6.9.
select department_id, job_id, avg(salary)  
from employees group by department_id, job_id having avg(salary)>10000 order by department_id, job_id;
6.10.
select manager_id, round(avg(salary)) from employees where nvl(commission_pct,'0')='0' group by manager_id having (avg(salary)>6000 and avg(salary) <9000);
select commission_pct, nvl(commission_pct,'0') from employees where  nvl(commission_pct,'0')<>'0';
6.11.
select max(salary) from employees;
select round(max(avg(salary)),-3) from employees 
group by department_id;
insert into employees (employee_id, first_name, last_name, email, hire_date, job_id) 
values (1001, 'Vovan', 'Prosvirnin', 'vova@mail.ru', '17.07.08', 1002);