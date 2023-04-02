ALTER TABLE dim_stores
ADD street_name varchar(255);
ALTER TABLE dim_stores
ADD pin_code int;

ALTER TABLE dim_stores
ADD lvl1_geog varchar(50);

ALTER TABLE dim_stores
ADD lvl2_goeg varchar(50);

ALTER TABLE dim_stores
ADD lvl3_geog varchar(50);

INSERT INTO dim_stores (street_name, pin_code, lvl1_geog,lvl2_goeg,lvl3_geog)
SELECT street_name, pin_code, lvl1_geog,lvl2_goeg,lvl3_geog FROM source_data;

ALTER TABLE dim_stores
ADD country_code varchar(50);

select * from dim_stores;

UPDATE dim_stores, dim_country,source_data 
SET dim_stores.country_code = dim_country.country_code
WHERE lower(source_data.country_name) = lower(dim_country.country_name);
