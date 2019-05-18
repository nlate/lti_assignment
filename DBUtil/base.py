from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser

# create an engine
config = configparser.ConfigParser()
config.read('config.ini')
host_name = config['MYSQL']['sql_db_server'];
port = int(config['MYSQL']['sql_db_port']);
db_name = config['MYSQL']['sql_db_name']
username = config['MYSQL']['sql_db_user']
password = config['MYSQL']['sql_db_password']

url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(username, password, host_name, port, db_name)
engine = create_engine(url)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

Base = declarative_base()