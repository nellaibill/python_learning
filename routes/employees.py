from flask import Blueprint,  render_template,redirect,request
import logging
from models.models import Employee
from extensions import db
employees_bp = Blueprint('employees', __name__)


@employees_bp.route('/employees')
def employees():
    employees = Employee.query.all()
    list_Employees = [{"id": emp.id, "name": emp.name, "position": emp.position} for emp in employees]
    return render_template('list_employees.html', employees=list_Employees)


@employees_bp.route('/add_employee_form')
def add_employee_form():
    return render_template('add_employee.html')


@employees_bp.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    position = request.form['position']

    logging.info(f"Adding employee: {name} - {position}")

    try:
        new_employee = Employee(
            name=name,
            position=position
        )

        db.session.add(new_employee)
        db.session.commit()

        logging.info("Employee added successfully")

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error adding employee: {e}")
        return "Error adding employee", 500

    return redirect('/employees')