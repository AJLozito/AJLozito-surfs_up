#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[2]:


engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[3]:


# Create our session (link) from Python to the DB
session = Session(engine)


# In[4]:


# Deliverable 1: Determine the Summary Statistics for June

# 1. Import the sqlalchemy extract function.
from sqlalchemy import extract

# 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
june_results = []

june_results = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == 6).all()

print(june_results)


# In[5]:


# 3. Convert the June temperatures to a list.
june_temp_list = list(june_results)

june_temp_list = list(np.ravel(june_results))

print(june_temp_list)


# In[6]:


# 4. Create a DataFrame from the list of temperatures for the month of June. 
june_df = pd.DataFrame(june_results, columns = ['date', 'temperature'])
june_df.set_index(june_df['date'], inplace=True)

#Sort the index
june_df = june_df.sort_index()
june_df


# In[7]:


# 5. Calculate and print out the summary statistics for the June temperature DataFrame.
june_df.describe()


# In[8]:


# Deliverable 2: Determine the Summary Statistics for December

# 6. Write a query that filters the Measurement table to retrieve the temperatures for the month of December.
dec_results = []

dec_results = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == 12).all()

print(dec_results)


# In[9]:


# 7. Convert the December temperatures to a list.
june_temp_list = list(june_results)

dec_temp_list = list(np.ravel(dec_results))

print(dec_temp_list)


# In[10]:


# 8. Create a DataFrame from the list of temperatures for the month of December. 
dec_df = pd.DataFrame(dec_results, columns = ['date', 'temperature'])

dec_df.set_index(dec_df['date'], inplace=True)

#Sort the index
dec_df = dec_df.sort_index()

dec_df


# In[11]:


# 9. Calculate and print out the summary statistics for the Decemeber temperature DataFrame.
dec_df.describe()

