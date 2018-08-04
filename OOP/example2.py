# this is a student class that take name 
# and you can his marks and git the average of them
class student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        print("welcome {} in our school".format(name))

    def addmarks(self, mark):
        self.marks.append(mark)

    def getavg(self):
        return sum(self.marks)/len(self.marks)