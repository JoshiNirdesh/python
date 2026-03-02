class Student :

    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks

    def avgMarks(self):
        avg=0
        for val in self.marks:
            avg +=val
        print("Average",avg/len(self.marks))

s1 = Student("Nirdesh",[10,10,10])
s1.avgMarks()