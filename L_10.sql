10.1.-10.
select * from employees;

create table locations2 as (select * from locations where 1=2);

select * from locations;
insert into locations2 (location_id, street_address, city) values (1000, ' FFFFFF', 'Rostov');

select * from locations2;
select * from countries;

insert into locations2 (location_id, street_address, city, country_id) values (1000, ' FFFFFF', 'Rostov', 10);

10.4. 
insert into locations2 (location_id, street_address, city, country_id) 
(select location_id, street_address, city, country_id from locations 
where country_id in (select country_id from countries where country_name = 'Italy'));

delete from locations2;

select * from locations2;

commit;

10.6.
insert into locations2 (location_id, street_address, city, state_province, country_id) 
(select 
location_id, 
street_address,
city,state_province, country_id from locations 
where length(state_province) > 9);

10.8.
create table locations4euro as (select * from locations where 1=1);

select * from locations4euro;

delete from locations2;

select * from locations2;

insert into locations2 (select * from locations );


insert into locations4euro (location_id, street_address, city, state_province, country_id) 
(select location_id, street_address,city, state_province, country_id 
from locations where country_id in (select country_id from countries where 
region_id in (select region_id from regions where region_name='Europe')));



commit;

10.11.
select * from locations2;

desc locations2;

update locations2 set postal_code = substr (city,1,12) where postal_code is null;

rollback;

10.13.
update locations2  set postal_code = 
(select postal_code from locations where location_id=2600) where postal_code is null ;
 rollback;

select * from locations where
location_id = 2600;

desc locations;
commit;

10.15. 
delete from locations2;
select * from locations2;
insert into locations2 (select * from locations );
commit;

delete from locations2 where country_id='IT';
savepoint loc2_1;

update locations2 set street_address='Sezam St. 18' where location_id>2500;
savepoint loc2_2;

rollback loc2_1;

commit;