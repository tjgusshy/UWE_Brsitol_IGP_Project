"""
ETL Script Documentation
========================

Overview:
---------
This script performs ETL (Extract, Transform, Load) operations for student engagement and demographic data. It reads cleaned and merged CSV files, connects to a MySQL database using credentials stored in a .env file, and loads the data into corresponding database tables. The script is modular and robust, with error handling and logging for database operations.

Process Breakdown:
------------------
1. **Environment Setup**
   - Loads environment variables from a `.env` file using `python-dotenv` for secure credential management.
   - Sets up logging for process tracking and error reporting.

2. **Database Connection**
   - Reads MySQL credentials (`Db_username`, `P_password`, `H_host`, `DB_name`) from the `.env` file.
   - Creates a SQLAlchemy engine for MySQL database connection.
   - Handles connection errors gracefully.

3. **Data Extraction**
   - Reads cleaned and pre-processed CSV files from the `python_folder/eda.ipynb`:
     - `students_info.csv`: Student demographic and engagement summary.
     - `merged_weeks.csv`: Merged weekly engagement data.
     - `demo_week_2.csv`, `demo_numeric.csv`, `Retrospective.csv`, `Retro_numeric.csv`: Additional demographic and retrospective survey data.

4. **Data Loading**
   - Loads each DataFrame into the MySQL database using `to_sql` with `if_exists='replace'` to overwrite existing tables.
   - Handles and logs any errors during the loading process.

5. **Error Handling**
   - Uses try-except blocks to catch and log database connection and data loading errors.

6. **Modularity**
   - Each major step (connection, extraction, loading) is clearly separated for maintainability.

.env File Usage:
----------------
- The script uses the `.env` file to securely store sensitive database credentials. Example `.env` file:

    Db_username=your_mysql_username
    P_password=your_mysql_password
    H_host=localhost
    DB_name=your_database_name

- This approach keeps credentials out of the codebase and supports best practices for security and configuration management.

Best Practices:
---------------
- Sensitive information is never hardcoded; always use environment variables.
- Logging is enabled for traceability and debugging.
- Data is loaded in a reproducible and idempotent way (tables are replaced each run).
- All file paths are relative to the project structure for portability.

"""

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


demo_week = pd.read_csv('python_folder/merged_demography.csv')
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