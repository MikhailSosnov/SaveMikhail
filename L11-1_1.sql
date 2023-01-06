11_1.1.
select * from employees;
create table friends as (select first_name, last_name, commission_pct from employees where commission_pct is not null);

select * from friends;
drop table friends;
create table friends (id, name, surname) as (select first_name, last_name, commission_pct from employees where commission_pct is not null);
create table friends1 (id, name, surname, email not null) as (select first_name, last_name, commission_pct, email from employees where commission_pct is not null);

11.2.
alter table friends add (email varchar2(25) default 'no email');
commit;

desc employees;

desc friends;

11_1.5
alter table friends rename column id to friends_id;

select * from friends;
drop table friends;
11_1.6.

create table friends 
(id number (6)  unique, 
name varchar2 (15), 
surname varchar (15), 
email varchar2 (25), 
salary number  (8,2) default 8000, 
sity varchar2 (15), 
birthday date default sysdate);

desc friends;
INSERT INTO friends (id, Name, surname, email, salary, sity, birthday) VALUES 
(4, 'Nina', 'Ivakina', 'Nina@mil.ru', 9000, ' Rostov', '08.06.1988');

commit;

INSERT INTO friends (id, Name, surname, email, sity) VALUES 
(9, 'Nina', 'Ivakina', 'Nina@mil.ru', ' Rostov');

commit;

alter table friends drop column salary;

rollback;

alter table friends set unused column ebirthday;
alter table friends set unused column birthday;

desc friends;

alter table friends drop unused columns;

alter table friends read only;

savepoint t1;

select * from friends;

delete friends;

alter table friends read write;
drop table friends;
;


