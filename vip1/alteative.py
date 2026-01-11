class stud:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    @classmethod
    def fromSTR(str,string):
        return str(string.split("=")[0],string.split("=")[1])

        

string="vardan=15"

studant_vip=stud.fromSTR(string)
print(studant_vip.name ,"-_-",studant_vip.roll_no)