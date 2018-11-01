#three level of employees: respondent, manager, director

#first call goes to respondednt who is free

#if respondent not free call must escalate to manager 

#if manager not available call must go to director


#call center
    #dispatch call




class CallCenter(object):

    def __init__(self, respondents, managers, director):
        #initialize employees
        self.respondent = respondents
        self.manager = managers
        self.director = directors
        #queue for calls that are awaiting to be answered

        call_queue = []
        respondent_queue = []

    #routes the call to available first employee, if no one is availale
    #saves to queue
    def dispatch_call(self):
        pass

    #when employee if available, assign employee a call, return true we assigned
    #false if not assigned
    def assign_call(self):


class Call(object):
    