1.
desc regions;
desc countries;
desc jobs;
desc 
2.
select * from regions;
select * from employees;
desc employees;
select employee_id, email, hire_date, hire_date-7 "One week before hire_date" from employees;
select employee_id, first_name||'('||job_id||')' "Our_employees", last_name, hire_date from employees;
select distinct first_name, last_name, hire_date from employees;
select distinct first_name from employees;
select * from jobs;
select job_title, 'min=2800, max=4000' "Info", max_salary "Max salary", max_salary*2-4000 "New salary" from jobs;, 
select 'Peter''s dog is very clever' from dual;
select q'<Peter's dog is very clever>' from dual;
select 100*365.25*24*60 from dual;

3._1.
select * from employees where first_name = 'David';
3._2.
select * from employees where Job_id LIKE 'F%';
3._3.
select first_name, last_name, salary, department_id from employees where department_id=50 and salary>4000;
3._4.
select * from employees where department_id in (20, 30);
3._5.
select * from employees where first_name like '_a%a';
3._6.
select * from employees where department_id in(50, 80) and (commission_pct is not null) order by email  desc;
3._7.
select * from employees where first_name like '%n%n%';
3._8.
select * from employees where length(first_name)>4 order by department_id desc nulls last;
3._9.
select * from employees where salary between 3000 and 7000 and (commission_pct is null) and (job_id in ('PU_CLERK', 'ST_MAN', 'ST_CLERK'));
3._10.
select * from employees where first_name like  '%\%%' escape '\';

select * from employees;

insert into employees (employee_id, first_name, last_name, email, hire_date, job_id) values (8888, 'Ha%er', 'Petrov', 'rota@mail.ru', '02.12.02', 'PU_CLERK');

desc employees;
3._11.
select job_id, first_name, salary from employees where employee_id>=120 and job_id!='IT_PROG' order by job_id, first_name desc;

5._1.
select * from employees where lower(first_name) like lower('%b%');
5._2. 
select * from employees where first_name like '%a%a%';
5.3.
select * from departments;
select * from departments where 


3.1.
select * from employees where length(first_name)>10;
3.2.
select * from employees;
select * from employees where mod(salary, 1000)=0;
select * from employees where mod(salary, 1000)<>0;
3.3. 
select phone_number, substr(phone_number,1,3) from employees where phone_number like '___.___.____';
3.4.
select * from employees where (first_name like '%m') and (length(first_name)>5);
3.5.
select * from nls_session_parameters;
select next_day( to_date('09.08.22'),5)+5 from dual;
3.6. 

