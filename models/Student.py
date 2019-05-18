'''
Created on May 16, 2019

@author: NLATE
'''
from sqlalchemy.orm import sessionmaker
import configparser
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from DBUtil.base import Base, Session, engine

class Student(Base):
    __tablename__ = 'Student'
    id = Column('student_id', Integer, primary_key = True)
    name = Column(String(100))
    class_id = Column(Integer)
    created_on = Column(Date)
    updated_on = Column(Date)
    Base.metadata.create_all(engine)    
    
    def __init__(self, _id, name, class_id, created_on, updated_on):
        '''
            General description :
            This class has definition for functions that provides add /update/ delete \
             search by entities in database for Student.
        '''
        self.id = _id
        self.name = name
        self.class_id = class_id
        self.created_on = created_on
        self.updated_on = updated_on