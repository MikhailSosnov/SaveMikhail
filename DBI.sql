DBI
1-2.
CREATE TABLE dbi_employees (id number (6)  primary key, name varchar2(20), hire_date date, gender varchar2 (1), 
age number (3), salary number (9,2), manager_id number (6), department_id number (4) references dbi_departments(id));
drop table dbi_employees;
desc dbi_employees;
desc employees;

CREATE TABLE dbi_departments (id number (4) primary key, department varchar2 (30), location_id number (4) references dbi_locations(id));
drop table dbi_departments;
desc dbi_departments;
desc departments;

CREATE TABLE dbi_locations (id number (4) primary key, location varchar2 (50));
desc dbi_locations;
drop table dbi_locations;
desc locations;

insert into dbi_locations (id, location) (select location_id, substr(trim(city) || ', '|| trim(street_address),1, 50) from locations);
select * from dbi_locations;
select * from locations;
desc locations;

insert into dbi_departments (id , department, location_id) (select department_id, department_name, location_id from departments);
desc departments;
desc dbi_departments;
select * from dbi_departments;

insert into dbi_employees (id, name, hire_date, gender, age, salary, manager_id, department_id) 
           (select employee_id, first_name, hire_date, 'M', '33', salary, manager_id, department_id from employees);
desc dbi_employees;
desc employees;
select * from dbi_employees;
savepoint dbi1;
rollback dbi1;
update dbi_employees set age=trunc(age+salary/1000-12);
update dbi_employees set gender = 'F' where name in 
('Pat', 'Elizabeth','Shanta', 'Karen', 'Neena',  'Diana', 'Shelli', 'Irene', 'Ki', 'Ellen', 'Nanette', 'Louise', 'Lisa', 'Alyssa', 'Kelly', 'Nadite', 'Jenifer', 'Shelley');
commit;
3.  
select * from dbi_employees where (hire_date>'01.01.2007' or hire_date is null) and (name like '%o%' or name is null);
4.
select * from dbi_employees where (gender = 'F' and age<30) or (gender='M' and age between 35 and 45);
5.
select case when name='Lex' then 'Viktor'  else upper(name) end from dbi_employees order by length(name) nulls first;
6.
select * from employees;
savepint sv2;
MERGE INTO dbi_employees d using employees e on (d.id=e.employee_id) WHEN MATCHED THEN update set d.name=e.first_name||' '||e.last_name;
select * from dbi_employees;
commit;
select substr(name,1,instr(name,' '))as "Name", substr(name,instr(name,' '))as "SurName"  from dbi_employees;
commit;
7.
select name "Name", substr(sysdate-age*365.25,7) "Year of birth" from dbi_employees;
select sysdate from dual;
8.
select * from dbi_employees;
select * from dbi_departments;
select e.id, e.name, e.hire_date, e.gender, e.age, e.salary,
e.manager_id,e.department_id, d.department from dbi_employees e join dbi_departments d on e.department_id=d.id;
commit;
9.
select * from dbi_employees where department_id is not null;
10.
select d.department, count(*) from dbi_employees e join dbi_departments d on e.department_id=d.id group by d.department ;
11.
select * from dbi_employees;
select d.department, round(avg(e.salary),2) from dbi_employees e join dbi_departments d on e.department_id=d.id group by d.department order by avg(e.salary) desc;
12.
select * from dbi_employees;

select  e.id, e.name, e.hire_date, e.gender, e.age, e.salary, e.manager_id, e.department_id from dbi_employees e 
where e.id in (select d.manager_id from dbi_employees d);

create view v_shief as (select  e.id, e.name, e.hire_date, e.gender, e.age, e.salary, e.manager_id, e.department_id from dbi_employees e 
where e.id in (select d.manager_id from dbi_employees d));
select * from v_shief;
commit;

13.
select e.id "Id работника", e.name "Имя работника", d.id "Id его менеджера", d.name "Имя его менеджера" from dbi_employees e join dbi_employees d on e.manager_id=d.id order by e.id;

14.
select * from dbi_employees;
select * from dbi_departments;
select * from dbi_locations;

select e.id, e.name, l.location from dbi_employees e join dbi_departments d on e.department_id=d.id join dbi_locations l on d.location_id=l.id;

15. 
ALTER TABLE dbi_locations ADD (city varchar2 (15) DEFAULT 'Moscow');
select * from dbi_locations;
commit;

16. 
select 'South', count(*) from dbi_employees e join dbi_departments d on e.department_id=d.id join dbi_locations l on d.location_id=l.id where substr (l.location,1,5)='South';

select * from dbi_employees e join dbi_departments d on e.department_id=d.id join dbi_locations l on d.location_id=l.id where substr (l.location,1,5)='South';

17.
select * from dbi_employees;
select * from dbi_departments;
select d.department, 'Worker Avg Age > 30' from dbi_employees e 
join dbi_departments d on e.department_id=d.id group by d.department
having avg(e.age)>30;

18.
select * from dbi_employees where salary in (select min(salary) from dbi_employees);
select * from dbi_employees where age in (select min(age) from dbi_employees);

19.
select id, name, hire_date, case when gender ='F' then 'Женский' when gender = 'M' then 'Мужской' end "Пол", age, salary, manager_id, department_id from dbi_employees;
commit;

20.
Create table bsk_employees as (select * from dbi_employees);
select * from bsk_employees;
update bsk_employees set name = 'Alieva Irina' where name='Neena Kochhar';
commit;

21.
desc bsk_employees;

22.
select * from dbi_employees e join bsk_employees d on e.id=d.id;

select id, name, hire_date, age, salary, manager_id, department_id from dbi_employees 
union
select id, name, hire_date, age, salary, manager_id, department_id from bsk_employees;

23.
savepoint sp101;
insert into bsk_employees (select * from bsk_employees where id=101);
select * from bsk_employees;
commit;
select distinct * from bsk_employees order by id;

24.
savepoint sp102;
insert into dbi_employees (select * from dbi_employees where id =102); не возможно вставить дублирующие строки - ограничение по уникальности
select * from dbi_employees;

29.
select * from dbi_employees where age in (select max(age) from dbi_employees);

select * from dbi_employees;
select * from dbi_departments;

select department_id, max(age) from dbi_employees group by department_id;

select department, max(age) from dbi_employees e 
join dbi_departments d on (e.department_id=d.id) group by department order by department;

31.
select * from dbi_employees where ((substr(name,instr(name,' ')) like '%o%' or substr(name,instr(name,' ')) like '%i%' 
or substr(name,instr(name,' ')) like '%e%') and length(substr(name,1,instr(name,' ')))>6);

33.
select substr(name,instr(name,' '))||' '||substr(name,1,instr(name,' ')) from dbi_employees;

