#three level of employees: respondent, manager, director

#first call goes to respondednt who is free

#if respondent not free call must escalate to manager 

#if manager not available call must go to director


#call center
    #dispatch call




class CallCenter(object):

    def __init__(self, respondents, managers):
        #initialize employees
        self.num_respondent = respondents
        self.num_manager = managers
        self.num_director = 1
        self.calls_pending = []
        self.operator_available = []

        director = Director()
 

    #routes the call to available first employee, if no one is availale
    #saves to queue
    def incoming_call(self, call):
        if employee_available !=[]:
            available_employee = self.operator_available.pop(0)
            pick_up_call(call, available_employee)
        else:
            self.calls_pending.append(call)


    def route_calls(self, call):
        if self.calls_pending != [] and self.employee_available != []:
            call = self.self.call_pending.pop(0)
            employee = self.employee_available.pop(0)
            call.pick_up_call(employee)
                
class Call(object):
    def __init__(self, call_id, call_start):
        self.call_id = call_id
        call_start = call_start
        call_end = None
        resolved_by = None

        #pop from qeueu
    def handle_call(self):

        # return True/False

    def end_call(self, resolved_by, call_end):
        self.call_end = call_end
        self.resolved_by = resolved_by

class Employee(object):
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.position = position
        self.name = name
        self.employee_status = True

class Operator(Employee):
    
    def escalate_manager(self, call):
        self.manager_call_queue.append(call)


class Manager(Employee):
    def __init__(self):
        self.manager_call_queue = []

    def escalate_director(self, call):
        self.director_call_queue.append(call)





class Director(object):
    def __init__(self):
        self.director_call_queue = []












    