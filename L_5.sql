select * from employees;
select * from departments;
5.1.
select * from employees where first_name like'%b%' or first_name like'%B%';
select * from employees where instr(upper(first_name),'B')>0;
5.2.
select * from employees where first_name like '%a%a%';
5.3.
select * from departments where Department_Name like '% %';
5.4.
select first_name, substr(first_name,2, length(first_name)-2) from employees;
5.5
select * from employees where length(substr(job_id,'_'))>3;
select job_id, length(substr(job_id,instr(job_id,'_')))-1 from employees;
select job_id, substr(job_id,instr(job_id,'_')) from employees where length(substr(job_id,instr(job_id,'_')))-1>=3 and substr(job_id,instr(job_id,'_'))<>'_CLERK';
5.6.
select * from employees;
select first_name, hire_date, substr(to_char(hire_date),1,2) from employees where substr(to_char(hire_date),1,2)='01' ;
5.8.
select first_name, hire_date, substr(to_char(hire_date),7,2) from employees where substr(to_char(hire_date),7,2)='08' ;
select to_char(sysdate) from dual;
select 'Tomorrow is '||(to_number(next_day(sysdate,1))-to_number(sysdate)) from dual;
select 'Tomorrow is '||next_day('19.07.22', 1) from dual;
select to_number(next_day(sysdate,1) - sysdate) from dual;
select case 
when to_number(next_day(sysdate,1) - sysdate)=7 then 'Пн' when to_number(next_day(sysdate,1) - sysdate)=6 then 'Вт' when to_number(next_day(sysdate,1) - sysdate)=5 then 'Ср'
when to_number(next_day(sysdate,1) - sysdate)=4 then 'Чт' when to_number(next_day(sysdate,1) - sysdate)=3 then 'Пт' when to_number(next_day(sysdate,1) - sysdate)=2 then 'Сб'
when to_number(next_day(sysdate,1) - sysdate)=1 then 'Вс'
end from dual;
select to_char (sysdate+1) "Инфо" from dual;
select to_char (sysdate+1, 'fm"Tomorrow is "Ddspth "Day of " Month') as "Инфо" from dual;
5.9.
select first_name||'  ' || to_char (hire_date) from employees;
5.10.
select first_name, salary, to_char(salary*1.2, '$999,999.99') from employees;
5.11. 
select sysdate from dual;
5.12.
select first_name, salary, to_char(salary+12345.55, '$999,999.999') from employees ;
5.13-5.14. 
select first_name, hire_date,-( hire_date-to_date('18.09.09')), -trunc(months_between(hire_date, to_date('18.09.09'))),salary, commission_pct, to_char((salary+nvl(commission_pct,0)), '$99,999.99')  from employees;
5.15.
select first_name as "Имя", last_name as "Фамилия",
case when to_char(length(first_name))=to_char(length(last_name)) then 'same lenght'
when to_char(length(first_name))<>to_char(length(last_name))then 'diferent lenght' end from employees;
select * from employees where to_char(length(first_name))=to_char(length(last_name));
5.16.
select * from employees;
select first_name, nvl(commission_pct,0),nvl2(commission_pct,'Yes','No') from employees;
5.17.
select first_name, nvl(commission_pct,0),nvl2(commission_pct,'Yes','No'), manager_id,
coalesce (commission_pct,commission_pct,manager_id,salary) from employees;
Проба
select case when trim(to_char(manager_id))='(null)' then '0' else to_char(manager_id) end from employees; не работает
select to_char(manager_id) from employees;
select  * from employees where trim(to_char(manager_id))='(null)';
5.18.
select first_name as "Имя", salary, lpad(case when salary<5000 then 'Low level' when salary>=5000 and salary<10000 then 'Normal level'
when salary>=10000 then 'High level' end, 20, ' ') from employees;
5.19.
select * from regions;
select * from locations;
select * from employees;
select * from countries;
select country_id, country_name, region_id, Decode(Region_id, 1, 'Europe', 2, 'America', 3, 'Asia', 4, 'Africa') from countries;
5.20
select country_id, country_name, region_id, Case When Region_id=1 then 'Europe' When Region_id=2 then 'America' When Region_id=3 then 'Asia'
 When Region_id=4 then 'Africa' end from countries;
 5.21.
 select * from employees;
 select first_name, salary, commission_pct, case 
when salary<10000 and nvl(commission_pct,0)=0 then 'Very bad' 
 when salary<10000 and nvl(commission_pct,0)<>0 then 'Bad' 
 when salary>=10000 and salary<15000 and nvl(commission_pct,0)=0 then 'Not bad'
 when salary>=10000 and salary<15000 and nvl(commission_pct,0)<>0 then 'Normal'
 when salary>=15000 and nvl(commission_pct,0)=0 then 'Good'
 when salary>=15000 and nvl(commission_pct,0)<>0 then 'Very good' Else 'Hernja'
 end from employees;
 






