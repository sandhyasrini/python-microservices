from flask import Flask, Blueprint, jsonify
from app import models

employees = Blueprint('employees', __name__)

@employees.route('/getAll', methods=['GET'])
def getEmployees():
    return models.employee.getEmployees() , 200