class Tester():

    def __init__(self, name='name', deadline=True):
        self.tester_name = name
        self.tester_deadline = deadline

    def work_hard(self, deadline=True):
        if deadline == True:
            print(self.tester_name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.tester_name, 'Можно отдыхать')


tester_1 = Tester(name='tester_1')
tester_2 = Tester(name='tester_2')

tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'
