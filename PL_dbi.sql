select * from jobs;
set serveroutput on;

CREATE OR REPLACE PROCEDURE bc_pr
  (V1 in varchar2,
  V2 in varchar2)
IS
BEGIN
  FOR tab IN (SELECT table_name from all_tables where owner=V1)
    LOOP 
      EXECUTE IMMEDIATE 'CREATE TABLE ' || tab.table_name||V2||
      ' AS SELECT * FROM ' || tab.table_name;
     END LOOP; 
EXCEPTION
  when others then
  DBMS_OUTPUT.PUT_LINE(SQLCODE);
  DBMS_OUTPUT.PUT_LINE(SQLERRM);
END;

variable v1 varchar2(50);
variable V2 varchar2(50);

exec bc_pr ('HR', '_bkp');

select * from employees_bkp;

select * from all_tables where owner='HR';
  