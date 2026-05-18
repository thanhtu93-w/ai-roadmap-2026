class student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def show(self):
        print(self.name,self.age,self.score)

s1 = student ("thanh tú",22,5)
s1.show()