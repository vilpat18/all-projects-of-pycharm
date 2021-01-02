class Basic_Student_Info:
    def __init__(self):
        self.name = input("Enter name: ")
        self.roll_no = int(input("Enter roll no: "))

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def get_name(self, name):
        self.name = name

    @property
    def get_roll_number(self):
        return self.roll_number


    @get_roll_number.setter
    def get_roll_number(self,roll_no):
        self.roll_no = roll_no



if __name__=="__main__":

    Basic_Student_InfoObj= Basic_Student_Info()








