11-2_1.
CREATE TABLE address 
(id number (6) constraint ad_id_un unique, 
country varchar2 (20), 
city varchar2 (20));

desc address;

drop table address;

select * from address;

11-2.2.
create table friends 
(id number (6), 
name varchar2 (20) check (length(name)>3),
email varchar2 (25),
address_id number (6) references address(id) on delete set null,
birthday date);


11-2.3.
alter table friends modify (id unique);

11-2.4.
alter table friends add primary key (id);

11-2.5.
create index fr_email_in on friends(email);

11-2.6.
alter table friends modify (email not null);

11-2.7.
drop table friends;
11-2.8.
drop table address;

desc friends;
drop table friends;