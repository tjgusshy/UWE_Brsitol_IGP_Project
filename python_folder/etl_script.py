import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as matplot
from sqlalchemy import create_engine, text
import os
import sqlalchemy.exc
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# create an engine that will be used to connect to mysql server
username = os.getenv('Db_username')  # Your MySQL username
password = os.getenv('P_password')  # Your MySQL password (leave empty if none)
host = os.getenv('H_host')  # Your MySQL host (e.g., localhost or an IP address)
db_name = os.getenv('DB_name')  # The database where the table exists

# Create a connection string
try:
    connection_string = f'mysql+mysqldb://{username}:{password}@{host}/{db_name}'
    db_connection = create_engine(connection_string)
except Exception as e:
    logging.error(f"Error connecting to the database: {e}")
    raise

# # read in the merged data set from csv file
students_info = pd.read_csv('python_folder/students_info.csv')
print(students_info.shape)
# # # # writing into mysql database
students_info.to_sql('students_info', con=db_connection, if_exists='replace', index=False)


# # # # # writing into mysql database
merged_weeks = pd.read_csv('python_folder/merged_weeks.csv')
print(merged_weeks.shape)

try:
    merged_weeks.to_sql('merged_weeks', con=db_connection, if_exists='replace', index=False)
except Exception as e:
    logging.error(f"Error writing to the database: {e}")
    raise


demo_week = pd.read_csv('python_folder/demo_week_2.csv')
# # # writing into mysql database


# # # read in the resources data set from csv file

try:
   demo_week.to_sql('demography', con=db_connection, if_exists='replace', index=False)
except Exception as e:
    logging.error(f"Error writing to the database: {e}")
    raise


demo_numeric = pd.read_csv('python_folder/demo_numeric.csv')
print(demo_numeric.shape)
# # # writing into mysql database

# # # read in the resources data set from csv file
try:
   demo_numeric.to_sql('demo_numeric', con=db_connection, if_exists='replace', index=False)
except Exception as e:
    logging.error(f"Error writing to the database:{e}")
    raise

Retrospective = pd.read_csv('python_folder/Retrospective.csv')

# writing into mysql database
Retrospective.to_sql('retrospective', con=db_connection, if_exists='replace', index=False)  
# read in the 

retro_numeric = pd.read_csv('python_folder/retro_numeric.csv')

# writing into mysql database
retro_numeric.to_sql('retro_numeric', con=db_connection, if_exists='replace', index=False)
# read in the