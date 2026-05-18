from BusinessLogic.core import core
class core_controller:

    def __init__(self):
        self.core_class = core()

    def analyse_behaviour(self,filename):
        '''analyse user behaviour based on csv data'''
        return self.core_class.analyse(filename)