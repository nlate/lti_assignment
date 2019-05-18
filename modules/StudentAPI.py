'''
Created on May 16, 2019

@author: NLATE
'''
from flask import Blueprint, jsonify, request
from DBUtil.Student import StudentDAO
import time

# blueprint declaration
studentAPI = Blueprint('studentAPI', __name__)
studentDB = StudentDAO()


@studentAPI.route('/student/all', methods=['GET'])
def get_all_student():
    try:
        data = list(studentDB.get_students())
        print(data)
        return jsonify({"message": "Students data retrieved successfully", "status": "success", "data" : data}), 200
    except Exception as e:
        jsonify({"message": str(e), "status": "failed"}), 404


@studentAPI.route('/student/<string:_id>', methods=['GET'])
def get_student_by_id(_id):
    try:
        print("student data")
        data = studentDB.get_student_by_id(_id)
        return jsonify({"message": "Students data retrieved successfully", "status": "success", "data" : data}), 200
    except Exception as e:
        jsonify({"message": str(e), "status": "failed"}), 404


@studentAPI.route('/student/add', methods=['POST'])
def add_student():
    try:
        data = request.json
        if data.get("id") is None or data.get("name") or data.get("class_id"):
            return jsonify({"message": "Mandatory fields name, id, class_id missing in the request", "status": "failed"}), 404
        else:
            data["created_on"] = None
            data["updated_on"] = None
            res = studentDB.add_student(data)
            return jsonify({"message": "Students data retrieved successfully", "status": "failed"}), 200
    except Exception as e:
        jsonify({"message": str(e), "status": "failed"}), 404    


@studentAPI.route('/update/student', methods=['PUT'])
def update_student():
    try:
        print("student data")
        
        return jsonify({"message": "Students data updated successfully", "status": "failed"}), 200
    except Exception as e:
        jsonify({"message": str(e), "status": "failed"}), 404


@studentAPI.route('/remove/student/<string:_id>', methods=['DELETE'])
def delete_student(_id):
    try:
        print("student data")
        data = studentDB.delete_student(_id)
        if data is True:
            return jsonify({"message": "Students data deleted successfully", "status": "Success"}), 200
        else:
            return jsonify({"message": "Student with id {} data deleted successfully".format(_id), "status": "Failed"}), 404
    except Exception as e:
        jsonify({"message": str(e), "status": "failed"}), 404