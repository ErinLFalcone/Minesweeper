import os, json, crud, model
import random as r

# Drop the database with dropdb
# Create the database with createdb
os.system('dropdb fgproject')
os.system('createdb fgproject')

# Use db.create_all to create tables

model.db.create_all()

