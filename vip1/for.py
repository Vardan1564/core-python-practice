class teacher:
    def __init__(self,tr_name,stander):
         self.tr_name=tr_name
         self.stander=stander

    def info(self):
         print(f"teacher : {self.tr_name}")
         print(f"stander : {self.stander}")

class stander_8(teacher):
     def __init__(self,tr_name,subject):
          teacher.__init__(self,tr_name,stander="8")
          self.subject=subject
     def info(self):
          teacher.info(self)
          print(f"subject : {self.subject}")


class subject_gj(stander_8):
     def __init__(self, tr_name,class_nm):
          stander_8.__init__(self,tr_name,subject="gujrati")
          self.class_nm=class_nm

     def info(self):
          stander_8.info(self)
          print(f"class name : {self.class_nm}")

c=subject_gj("vijay","10")
c.info()
          
        