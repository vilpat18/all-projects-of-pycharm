class Mobile:
    def __init__(self):
        self.model = 'Nokia 1600'

    def set_value(self,m):
        self.model = m


obj = Mobile()
print(obj.model)

obj.set_value('samsung')
print(obj.model)

