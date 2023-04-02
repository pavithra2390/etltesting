import pandas as pd
import pytest
from sqlalchemy import create_engine
import numpy as np
engine = create_engine("mysql+pymysql://root:sqldb@localhost:3306/test_schema?charset=utf8mb4")
#conn = engine.connect()

source = 'SELECT * FROM source_data'
target = 'SELECT * FROM dim_stores'

with engine.begin() as conn:
   df = pd.read_sql_query(target,engine)

print(df)

##Store id
# check if column exists
def test_col_exists_store_id():
    assert 'store_id' in df.columns

# check for nulls
def test_null_check_store_id():
    assert np.where(df['store_id'].isnull())
    
# check values are unique
def test_unique_check_store_id():
    assert pd.Series(df['store_id']).is_unique
    

#Store name
# check if column exists
def test_col_exists_store_name():
    name="store_name"
    assert name in df.columns

# check for nulls
def test_null_check_store_name():
    assert np.where(df['store_name'].isnull())
    
# check values are unique
def test_unique_check_store_name():
    assert pd.Series(df['store_name']).is_unique
    
#Country code
# check if column exists
def test_col_exists_country_code():
    name="country_code"
    assert name in df.columns

# check for nulls
def test_null_check_country_code():
    assert np.where(df['country_code'].isnull())
    
# check values are unique
def test_unique_check_contry_code():
    assert pd.Series(df['country_code']).is_unique