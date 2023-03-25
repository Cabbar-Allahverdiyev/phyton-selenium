import app
import student


stdList=[]
application =app.App(stdList)
student1=student.Studnet("Cabbar","Allahverdiyev")
student2=student.Studnet("Seymur","Veliyev")
student3=student.Studnet("Cingiz","Quliyev")
application.add(student1)
application.add(student2)
application.add(student3)

application.delete(student2,student1)

application.writeConsole()
#print(application.findStudentIndex(student3))


