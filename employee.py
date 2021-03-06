from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_employee = Blueprint('employee', __name__)
employee_set = [
    {
        "Id": 1,
        "Name": 'Алексей',
        "AnalystSkill": 70,
        "AnalystCapacity": 5,
        "DeveloperSkill": 75,
        "DeveloperCapacity": 100,
        "TesterSkill": 35,
        "TesterCapacity": 200,
        "Salary": 300,
        "Image" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmI-9hjc42YGwKHasnKE_sUekRsGxi_x5-BW_8rIw0V3CD6cR_"
    },
    {
        "Id": 2,
        "Name": 'Андрей',
        "AnalystSkill": 25,
        "AnalystCapacity": 4,
        "DeveloperSkill": 60,
        "DeveloperCapacity": 200,
        "TesterSkill": 90,
        "TesterCapacity": 100,
        "Salary": 200,
        "Image" : "https://s-media-cache-ak0.pinimg.com/originals/e7/8c/1c/e78c1c6f7471c201ea17f3a5b43ab275.jpg"
    },
    {
        "Id": 3,
        "Name": 'Александр',
        "AnalystSkill": 35,
        "AnalystCapacity": 1,
        "DeveloperSkill": 85,
        "DeveloperCapacity": 200,
        "TesterSkill": 75,
        "TesterCapacity": 150,
        "Salary": 400,
        "Image" : "http://www.mens-hairstyle.com/wp-content/uploads/2016/12/Classic-Undercut.jpg"
    },
        {
        "Id": 4,
        "Name": 'Татьяна',
        "AnalystSkill": 95,
        "AnalystCapacity": 5,
        "DeveloperSkill": 25,
        "DeveloperCapacity": 100,
        "TesterSkill": 70,
        "TesterCapacity": 150,
        "Salary": 500,
        "Image" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6gUwi_vuu2c_RKmpgFvUbQyep9JqwY44VhpYDNVMbSorINWl6"
    },
    {
        "Id": 5,
        "Name": 'Мария',
        "AnalystSkill": 60,
        "AnalystCapacity": 2,
        "DeveloperSkill": 35,
        "DeveloperCapacity": 100,
        "TesterSkill": 55,
        "TesterCapacity": 200,
        "Salary": 100,
         "Image" : "http://www.eshorthairstyles.com/wp-content/uploads/2017/04/19.Celebrity-Short-Hair-2016.jpg"
    },
    {
        "Id": 6,
        "Name": 'Дмитрий',
        "AnalystSkill": 30,
        "AnalystCapacity": 1,
        "DeveloperSkill": 90,
        "DeveloperCapacity": 100,
        "TesterSkill": 45,
        "TesterCapacity": 100,
        "Salary": 300,
        "Image" : "https://www.tatacliq.com/que/wp-content/uploads/2017/11/square-face.jpg"
    },
    {
        "Id": 7,
        "Name": 'Вероника',
        "AnalystSkill": 80,
        "AnalystCapacity": 7,
        "DeveloperSkill": 20,
        "DeveloperCapacity": 200,
        "TesterSkill": 75,
        "TesterCapacity": 100,
        "Salary": 350,
        "Image" : "https://data.whicdn.com/images/108843757/large.jpg"
    },
    {
        "Id": 8,
        "Name": 'Екатерина',
        "AnalystSkill": 65,
        "AnalystCapacity": 4,
        "DeveloperSkill": 75,
        "DeveloperCapacity": 100,
        "TesterSkill": 45,
        "TesterCapacity": 100,
        "Salary": 200,
         "Image" : "https://hairstylecamp.com/wp-content/uploads/2015/12/sweet-sixteen-hairstyles-for-Girls-18.jpg"
    }
]
employee_class = {
    "Id": int,
    "Name": str,
    "AnalystSkill": int,
    "AnalystCapacity": int,
    "DeveloperSkill": int,
    "DeveloperCapacity": int,
    "TesterSkill": int,
    "TesterCapacity": int,
    "Salary": int
}

@app_employee.route('/', methods=['GET'])
def get_employee_set():
    return jsonify(employee_set)

@app_employee.route('/', methods=['POST'])
def create_employee():
    if not request.json:
        abort(400)
    employee = { 'Id': employee_set[-1]['Id'] + 1 if len(employee_set) else 1 }
    create_record(employee_class, request, employee)
    employee_set.append(employee)
    return jsonify(employee), 201

@app_employee.route('/<int:employee_id>', methods = ['GET'])
def get_employee(employee_id):
    employees = list(filter(lambda t: t['Id'] == employee_id, employee_set))
    if len(employees) == 0:
        abort(404)
    return jsonify(employees[0])

@app_employee.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employees = [employee for employee in employee_set if employee['Id'] == employee_id]
    if len(employees) == 0 or not request.json:
        abort(404)
    employee = employees[0]
    update_record(employee_class, request, employee)
    return jsonify(employee)

@app_employee.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employees = [employee for employee in employee_set if employee['Id'] == employee_id]
    if len(employees) == 0:
        abort(404)
    employee_set.remove(employees[0])
    return jsonify({'Result': True})
