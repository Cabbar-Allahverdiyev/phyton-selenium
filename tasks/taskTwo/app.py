class App :
    def __init__(self,stdList=[]):
        self.stdList=stdList


    def add(self,student):
        self.stdList.append(student)
        return self.stdList

    def delete(self,*args) :
        for student in args:
            for std in self.stdList:
                if(std.name == student.name and std.surName == student.surName):
                    self.stdList.remove(std)
        
    def writeConsole(self):
        for std in self.stdList :
            print(f"{std.name} {std.surName}")
            return self.stdList

    def findStudentIndex(self,student):
        for i in range(len(self.stdList)) :
            std=self.stdList[i]
            if(std.name == student.name and std.surName == student.surName):
                return i
                

