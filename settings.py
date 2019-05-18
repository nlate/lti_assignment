'''
Created on May 16, 2019

@author: NLATE
'''
import os, configparser
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

config = configparser.ConfigParser()  
config.read('config.ini') 
host_name = config['MYSQL']['sql_db_server'];
port = int(config['MYSQL']['sql_db_port']);
db_name = config['MYSQL']['sql_db_name']
username = config['MYSQL']['sql_db_user']
password = config['MYSQL']['sql_db_password']

url = 'mysql://{}:{}@{}:{}/{}'.format(username, password, host_name, port, db_name)

db = SQLAlchemy(url)