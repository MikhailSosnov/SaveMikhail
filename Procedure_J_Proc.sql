set serveroutput on;
CREATE OR REPLACE PROCEDURE J_PROC IS
 CURSOR Cur_J is
  select j.job_id, j.job_title, j.min_salary
   from jobs j
  where min_salary>=15000; 
  J_ID varchar2 (10);
  J_TITLE varchar2 (35);
  J_MIN_SALARY number (6);
BEGIN

 OPEN Cur_J;
  LOOP
   FETCH Cur_J
    INTO J_ID, J_TITLE, J_MIN_SALARY;     
    EXIT WHEN Cur_J%NOTFOUND;  
    dbms_output.put_line('Номер '||J_ID||' Профессия '||J_TITLE||'Мин.Зарплата '||J_MIN_SALARY);
   END LOOP;   
  CLOSE Cur_J;
END;

EXEC J_Proc;
