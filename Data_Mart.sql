Data_Mart
CREATE TABLE customer_transactions
 (trx_date date,
  payment_type varchar (30),
  city_code varchar2 (3),
  total_amount number,
  description varchar2 (100));
DESC customer_transactions;
DROP TABLE customer_transactions;
SELECT * FROM customer_transactions;

CREATE TABLE payment_total_month
 (year number,
  balance_debt number,
  january number,
  february number,
  march number,
  april number,
  may number,
  june number,
  july number,
  august number,
  september number,
  october number,
  november number,
  december number);
DESC payment_total_month;  

CREATE TABLE city_code_name
 (city_code varchar2 (3),
  city_name varchar2 (50),
  code_name varchar2 (50),
  valid_from_dttm date,
  valid_to_dttm date);
DESC city_code_name;  
DROP TABLE city_code_name;
SELECT * FROM city_code_name;

DESC calendar_dates;

select * from calendar_dates;
SELECT * FROM city_code_name;
SELECT * FROM payment_total_month;
SELECT * FROM customer_transactions order by trx_date;
select * from CALENDAR_DATES order by issue_date;


CREATE OR REPLACE VIEW dm_revenue_v AS SELECT c_d.issue_date ISSUE_DATE, c_c_n.city_name, c_t.payment_type from calendar_dates c_d 
JOIN customer_transactions c_t on c_d.issue_date=c_t.trx_date JOIN city_code_name c_c_n on c_t.city_code=c_c_n.city_code;

SELECT * from calendar_dates c_d 
JOIN customer_transactions c_t on c_d.issue_date=c_t.trx_date JOIN city_code_name c_c_n on c_t.city_code=c_c_n.city_code;




SELECT * From dm_revenue_v order by issue_date;



