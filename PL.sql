
set serveroutput on;
select * from jobs;
begin
dbms_output.put_line('Получлось!');
end;
desc jobs;

DECLARE
J_JD varchar2 (10);
J_TITLE varchar2 (35);
j_MIN_SALARY number (6);
Create or replace procedure Input_J is
 CURSOR Cur_J is
  select j.job_id, j.job_title, j.min_salary
   from jobs j
  where min_salary>=15000; 
BEGIN
 OPEN Cur_J
  LOOP
   FEYCH Cur_J
    INTO J_JD, J_TITLE, J_MIN_SALARY;
    EXIT WHEN Cur_J%NOTFOUND;
  END LOOOP
  dbms_output.put_line('Получлось!');
CLOSE Cur
END
  
 exec J_Proc; 
 
 exec bc_pr ('HR', '_bkp');
  