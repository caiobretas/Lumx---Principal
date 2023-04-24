-- select gas, gasprice, gasused, cumulativegasused from finance.movements_crypto
-- where hash = '0x7c24480588332a88bc41a0503027a201054fa8c330e6284e2482e19301d219bd';


-- truncate table finance.movements_crypto

create table if NOT EXISTS  finance.book  (
address varchar(100) not null PRIMARY KEY,
name varchar(50),
is_lumx boolean,
is_conversion boolean,
is_primarysale boolean,
is_secondarysale boolean
);