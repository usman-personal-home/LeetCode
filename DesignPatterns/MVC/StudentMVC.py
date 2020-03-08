class StudentModel:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number


class StudentView:
    def __init__(self):
        pass

    def printStudent(self, name, number):
        print("Student: ")
        print("Name: " + name)
        print("Roll No: " + str(number))


class StudentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def setStudentName(self, name):
        self.model.setName(name)

    def setStudentNumber(self, number):
        self.model.setNumber(number)

    def updateView(self):
        self.view.printStudent(self.model.getName(), self.model.getNumber())


if __name__ == '__main__':

    sm = StudentModel("usman",  23)
    sv = StudentView()
    sc = StudentController(sm, sv)
    sc.updateView()

    sc.setStudentName("Joe")
    sc.setStudentNumber(25)
    sc.updateView()





