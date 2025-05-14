import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as matplot
from sqlalchemy import create_engine, text
import os
import sqlalchemy.exc
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)





#Create a connection string
connection_string = f'mysql+{db_name}://{username}:{password}@{host}/{db_name}'

db_connection = create_engine(connection_string)