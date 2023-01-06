2.
CREATE TABLE PLSQL_TEST2_TABLE 
              (USERNAME  VARCHAR2(50),
              ROLE  VARCHAR2(50),
              SCR_EFF_FROM_DATE  DATE,
              SCR_EFF_TO_DATE  DATE,
              CURRENT_FLAG NUMBER);
              
DESC PLSQL_TEST2_TABLE;
select * from PLSQL_TEST2_TABLE;


INSERT INTO PLSQL_TEST2_TABLE (USERNAME, ROLE, SCR_EFF_FROM_DATE) 
                       VALUES ('gfedonov', 'Junior Developer', to_date('01.03.2019', 'DD-MM-YY'));  
INSERT INTO PLSQL_TEST2_TABLE (USERNAME, ROLE, SCR_EFF_FROM_DATE) 
                       VALUES ('gfedonov', 'Middle Developer', to_date('02.05.2020', 'DD-MM-YY'));                       
INSERT INTO PLSQL_TEST2_TABLE (USERNAME, ROLE, SCR_EFF_FROM_DATE) 
                       VALUES ('gfedonov', 'Senior Developer', to_date('01.08.2021', 'DD-MM-YY'));
INSERT INTO PLSQL_TEST2_TABLE (USERNAME, ROLE, SCR_EFF_FROM_DATE) 
                       VALUES ('lkolyakin', 'Junior Developer', to_date('12.02.2018', 'DD-MM-YY'));
INSERT INTO PLSQL_TEST2_TABLE (USERNAME, ROLE, SCR_EFF_FROM_DATE) 
                       VALUES ('lkolyakin', 'Middle Developer', to_date('05.01.2019', 'DD-MM-YY'));
INSERT INTO PLSQL_TEST2_TABLE (USERNAME, ROLE, SCR_EFF_FROM_DATE) 
                       VALUES ('lkolyakin', 'Senior Developer', to_date('06.08.2020', 'DD-MM-YY'));
INSERT INTO PLSQL_TEST2_TABLE (USERNAME, ROLE, SCR_EFF_FROM_DATE) 
                       VALUES ('lkolyakin', 'Senior 2 Developer', to_date('01.05.2021', 'DD-MM-YY')); 
*/



-----------------------------------------------------
SELECT * FROM PLSQL_TEST2_TABLE;

CREATE OR REPLACE PROCEDURE second_task 
(setd out varchar2)
IS 
BEGIN
  
  select username,
         role,
         scr_eff_from_date,
         lead(scr_eff_from_date, 1, '01.01.2030') 
         over (partition by username order by scr_eff_from_date)s,
         current_flag
  from PLSQL_TEST2_TABLE;
-----------------------------------------------------  
SELECT * FROM PLSQL_TEST2_TABLE;

create table pop (id number, name varchar2(20), age number)
insert into pop (id,name,age) values(1,'Den',25)
select * from pop

CREATE OR REPLACE PROCEDURE second_task 
IS
BEGIN
  for s in (select id+2 id, to_char(length(name)) e, age-10 age from pop)
   loop
  insert into pop values (s.id, s.e, s.age);
  end loop;
END;

execute second_task      