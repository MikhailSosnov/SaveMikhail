with T1 as (select * from employees e where employee_id  between 100 and 105), 
T2 as (select * from departments d where department_id=90) select department_name from t2;
select * from employees;
select * from departments;

with T1 as (select * from employees e where employee_id  between 100 and 120), 
T2 as (select * from departments d where department_id between 50 and 60) 
select * from t1, t2;

with T1 as (select * from employees e where employee_id  between 100 and 105), 
T2 as (select * from departments d where department_name='Executive') 
select * from t1, t2;

with T1 as (select * from employees e where employee_id  between 100 and 120), 
T2 as (select * from departments d where department_id between 50 and 60), T3 as (select * from locations where location_id=1400)
select * from t1, t2, t3;

select * from locations;