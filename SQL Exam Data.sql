----------------------------------------------EMPLOYEES--------------------------------------------------

insert into employees values (1, 'Maslov Denis',       to_date('01.01.2001','DD.MM.YYYY'), 'M', 50, 100000, NULL, NULL);
insert into employees values (2, 'Ivanov Fedor',       to_date('13.04.2002','DD.MM.YYYY'), 'M', 45, 80000, 1, 2);
insert into employees values (3, 'Vlasov German',      to_date('03.11.2007','DD.MM.YYYY'), 'M', 39, 75000, 1, 3);
insert into employees values (4, 'Fedorov Sergey',     to_date('01.08.2005','DD.MM.YYYY'), 'M', 41, 82000, 1, 5);
insert into employees values (5, 'Andreev Oleg',       to_date('10.06.2008','DD.MM.YYYY'), 'M', 35, 78000, 1, 6);
insert into employees values (6, 'Pavlova Svetlana',   to_date('10.09.2010','DD.MM.YYYY'), 'F', 39, 75000, 1, 1);
insert into employees values (7, 'Zakharova Anna',     to_date('11.05.2005','DD.MM.YYYY'), 'F', 48, 75000, 1, 4);
insert into employees values (8, 'Moiseev Stepan',     to_date('10.10.2010','DD.MM.YYYY'), 'M', 35, 52000, 2, 2);
insert into employees values (9, 'Smirnova Ekaterina', to_date('01.12.2012','DD.MM.YYYY'), 'F', 30, 45000, 2, 2);
insert into employees values (10, 'Kulikov Alexandr',  to_date('01.09.2009','DD.MM.YYYY'), 'M', 32, 60000, 3, 3);
insert into employees values (11, 'Alexeev Ivan',      to_date('25.07.2013','DD.MM.YYYY'), 'M', 27, 53000, 4, 5);
insert into employees values (12, 'Sorokin Ivan',      to_date('05.07.2015','DD.MM.YYYY'), 'M', 25, 45000, 4, 5);
insert into employees values (13, 'Romanov Maxim',     to_date('22.06.2007','DD.MM.YYYY'), 'M', 30, 55000, 4, 5);
insert into employees values (14, 'Kovalenko Petr',    NULL, 'M', 22, 32000, 5, 6);
insert into employees values (15, 'Filatov Andrey',    to_date('01.06.2009','DD.MM.YYYY'), 'M', 24, 40000, 6, 1);
insert into employees values (16, 'Savenko Inna',      to_date('01.02.2007','DD.MM.YYYY'), 'F', 25, 45000, 6, 1);
insert into employees values (17, 'Dorofeeva Irina',   to_date('10.11.2010','DD.MM.YYYY'), 'F', 27, 48000, 7, 4);
insert into employees values (18, 'Ivaaaaanov Fedor',       to_date('13.04.2002','DD.MM.YYYY'), 'M', 45, 80000, 1, 2);
insert into employees values (19, 'Ivaaaaaaaanov Fedor',       to_date('13.04.2002','DD.MM.YYYY'), 'M', 45, 80000, 1, 2);
insert into employees values (20, 'Ivaaaanov Fedor',       to_date('13.04.2002','DD.MM.YYYY'), 'M', 45, 80000, 1, 2);

commit;

--------------------------------------------DEPARTMENTS-------------------------------------

insert into departments values (1, 'HR',            1);
insert into departments values (2, 'Sales',         1);
insert into departments values (3, 'IT',            2);
insert into departments values (4, 'Accounting',    1);
insert into departments values (5, 'Manufacturing', 3);
insert into departments values (6, 'Shipping',      3);

commit;

--------------------------------------------LOCATIONS-------------------------------------

insert into locations values (1, 'Northwest');
insert into locations values (2, 'South'    );
insert into locations values (3, 'East'     );

commit;
