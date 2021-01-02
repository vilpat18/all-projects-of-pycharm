from utils.basic_information import Basic_Student_Info

class basic_info:
    def __init__(self):
        basic_student_infoobj = Basic_Student_Info()
    def __str__(self):
        return "Name:{}| Roll_no:{}".format(self.name,self.roll_no)

if __name__ == "__main__":
    basic_infoobj = basic_info()
    print(basic_infoobj)
