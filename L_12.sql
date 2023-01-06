12.1.
Create table test200 (id integer, name1 varchar2 (15), name2 varchar2 (15), address1 varchar2 (25), address2 varchar2 (25));
desc test200;
drop table test200;
select * from test200;

insert into test200 values (3, 'olga', 'Petja', 'Kirov', 'Lviv');

insert into test200 values (5, 'Goga', 'Goga', 'Norsk', 'Norsk');
define;
commit;

select id, name1, name2, address1, address2 from test200;

select id, name1, name2, address1, address2 from test200 where id=&v_id;

select id, name1, name2, address1, address2 from test200 where (id=&v_id and 
name1='&v_name1' and address2='&v_address2');

select id, name1, name2, address1, address2 from test200 where 
(upper(name1)=upper('&&v_name') and upper(name2)=upper('&v_name') and address1='&&v_address' and address2='&v_address');

Undefine v_name; 

Undefine v_address;

Undefine v_name v_address;

Define;

grant 