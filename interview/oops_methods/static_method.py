class Student:
    name = 'vilas patil'

    def __init__(self,mobile,email):
        self.mobile_no = mobile
        self.email_id = email

    def contact_info(self):
        print('name: ',self.name)
        print('contact number: ',self.mobile_no)
        print('email address: ',self.email_id)
        # return self.name,self.mobile_no,self.email_id

    @staticmethod
    def profession():
        print("python developer")


obj = Student('9993332221','patilstheroyals@gmail.com')
obj.contact_info()

Student.profession()