class school :
    def __init__(self,stud_or_teacher_name, stander):
        self.stud_or_teacher_name=stud_or_teacher_name
        self.stander=stander

class teacher(school):
    def __init__ (self ,stud_or_teacher_name, stander,teacher_id ,subjact,time):
        super().__init__(stud_or_teacher_name, stander)
        self.subjact=subjact
        self.time=time
        self.teacher_id=teacher_id

    def info(self):
        print(f"the name is {self.stud_or_teacher_name} ")
        print(f"the stander is {self.stander} ")
        print(f"the teacher_id is {self.teacher_id} ")
        print(f"the subjact is {self.subjact} ")
        print(f"the time is {self.time} ")


vardan=school("vardan","12")
vijay=teacher("vijay sir","12",'2240','BA','10:00 to 11:00 am')
vijay.info()