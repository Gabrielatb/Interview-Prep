# Implementing call center with three levels of employees


#hierarchy of people who would answer the call: respondent --> manager --> director


#dispatch call goes to respondent see if respondent is available then manager then director


#employee is a superclass of director, manager, and respondent
from datetime import datetime

class Employee(object):
    def take_call():
    def end_call():
    def is_available():
    def pass_call():

class Director(Employee):

    def __init__(self, id):
        self.rank = 3
        self.id = id_

class Manager(Employee):

    def __init__(self, id):
        self.rank = 2
        self.id = id_

class Respondent(object):

    def __init__(self, id):
        self.rank = 1
        self.id = id_

class Call(object):

    def __init__(self, caller):
        self.caller = caller
        self.start_time = datetime.now()
        self.end_time = None
        self.employee = None

    def employee_on_line():
    def end_call(self):
    def duration():



class CallCenter(object):
    def __init__(self, num_respondents=10, num_managers=4, num_directors=2):
        self.employees = 
        self.call_database = dict()
        self.call_queues = [list(), list(), list()]

    def answer_call(self, caller):
        call = Call(caller)
        self.call_database[call.start_time] = call
        self.dispatch_call_2(self, call)

    def dispatch_call(self, call):
        employee = get_avaiable_employee(call)
        if employee is not None:
            employee.take_call(call)
            call.emplpyee_on_line(employee)
        else:
            self.call_queues[call.rank] = call






class CallCenter(object):