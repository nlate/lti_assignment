'''
Created on May 16, 2019

@author: NLATE
'''


from flask import Flask, request, json, jsonify, render_template
import configparser
import os
from modules import StudentAPI
from sqlalchemy import create_engine

application = Flask(__name__, static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), './static'))
application.register_blueprint(StudentAPI.studentAPI)


@application.route('/')
def home():
    try:
        print("index")
        return True
        
    except Exception as e:
        pass

if __name__ == '__main__':
    application.run(port=8085, host='0.0.0.0')
