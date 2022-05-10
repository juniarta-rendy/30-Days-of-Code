class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        
        if avg <= 100 and avg >= 90:
            return 'O'
        elif avg < 90 and avg >=  80:
            return 'E'
        elif avg < 80 and avg >= 70:
            return 'A'
        elif avg < 70 and avg >= 55:
            return 'P'
        elif avg < 55 and avg >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()