11-3.1.
select * from employees;
select * from departments;
select * from locations;
create table emp1000 as (select first_name, last_name, salary department_id from employees);
11-3.2.
create view v1001 as 
(select e.first_name, e.last_name, e.salary, d.department_name, l.city from 
employees e join departments d on (e.department_id=e.department_id) join 
locations l on (d.location_id=l.location_id)); 
desc v1001
select * from v1001;
11-3.3
alter table emp1000 add (city varchar2 (20));
desc emp1000;
11-3.4.
Alter synonym syn1001 compile;
11-3.5.
Create synonym syn1001 for v1001;
select * from syn1001;
commit;
11-3.6-8.
drop synonym syn1001;
drop view v1001;
desc v1001;
drop table emp1000;
11-3.9.
create sequence  seq1000 increment by 4 start with 12  maxvalue 200 cycle;
select seq1000.nextval from dual;
commit;

11-3.10.
alter sequence  seq1000 nomaxvalue nocycle;

11-3.11.
desc employees;
insert into employees (employee_id, last_name, email, hire_date,job_id) values
(seq1000.nextval, 'Ivanov', 'okgp@mail.ru', '01.03.98', 'AD_VP');
insert into employees (employee_id, last_name, email, hire_date,job_id) values
(seq1000.nextval, 'Peykin', 'Hr@mail.ru', '01.03.11', 'AD_VP');
select * from employees;
commit;


