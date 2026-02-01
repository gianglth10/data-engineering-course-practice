import pandas as pd
from sqlalchemy import create_engine

# Use localhost:5433 for external-to-docker connection
engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

# 1. Ingest Green Taxi
df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
df_green.to_sql(name='green_taxi_data', con=engine, if_exists='replace', chunksize=100000)

# 2. Ingest Zones
df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql(name='zones', con=engine, if_exists='replace')