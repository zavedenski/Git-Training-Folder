from additionalFile import *

person = Worker()

print("Welcome to Visitors Registration form")
print("If you are looking for workers, please fill this field.")

employer = Recruiter()
employer.putData()

mathes = 0
for i in range(len(employer.skills)):
    for j in range(len(person.skills)):
        if employer.skills[i] == person.skills[j]:
            mathes += 1

putDataIntoFile(employer.nameOfCompany, employer.email, employer.experience, employer.degree, mathes)
