SELECT * FROM job_history;
SELECT * FROM job_history where months_between (end_date, start_date)>=40;
SELECT employee_id, first_name, 
replace (phone_number,'.', '-') FROM employees;
SELECT upper (last_name), lower(email), initcap(job_id) FROM employees;
SELECT employee_id, concat (first_name,salary) FROM employees;
SELECT round(hire_date, 'yyyy') FROM employees;
SELECT rpad(first_name, 10, '$'), lpad (first_name,2,'a')) FROM employees;
SELECT first_name, instr (first_name, 'a',1,2) FROM employees where instr (first_name, 'a',1,2)<>0;
select trim ('!' from '!!!HELLO!!My!! Frend!!!!!') from dual;
SELECT * FROM employees;
SELECT first_name, salary, salary*3.1415, round (salary*3.1415, 1), trunc (salary*3.1415, -3)/1000  FROM employees;
SELECT first_name, hire_date, add_months(hire_date, 6),last_day (hire_date)  FROM employees;




